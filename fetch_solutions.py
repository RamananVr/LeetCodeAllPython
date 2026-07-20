#!/usr/bin/env python3
"""Fetch English write-ups and Python/SQL solutions from doocs/leetcode.

Strategy: create a shallow, blobless, sparse git working directory limited to the
``solution/`` subtree, walk it locally, copy out the wanted files preserving the
repo layout, then delete the temporary working directory.

Requires ``git`` on PATH. No third-party dependencies.
"""

from __future__ import annotations

import argparse
import csv
import fnmatch
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import build_index

REPO_URL = "https://github.com/doocs/leetcode.git"
SPARSE_SUBTREE = "solution"

# Basename patterns for files we want to mirror.
WANTED_PATTERNS = ("README_EN.md", "Solution*.py", "Solution*.sql")

# Marker for the Chinese-doc link line to strip from each README_EN.md.
CHINESE_DOC_MARKER = "中文文档"


def _lang_kept(lang: str) -> bool:
    """Return True if a code-tab language is Python or SQL (kept), else False.

    Database problems use SQL/MySQL tabs; everything Python-based (incl. pandas)
    is kept, and all other programming languages are dropped.
    """
    lang = lang.strip().lower()
    return lang.startswith("python") or lang == "pandas" or lang in ("sql", "mysql")


def _is_fence(line: str) -> bool:
    s = line.lstrip()
    return s.startswith("```") or s.startswith("~~~")


def _solution_link_prefix(rel_path) -> str:
    """Relative prefix that points a README at ``rel_path`` back to ``solutions/``.

    Upstream links are absolute (``/solution/<range>/<problem>/README_EN.md``),
    which break on GitHub. ``rel_path`` is the file's path relative to the output
    root (e.g. ``README_EN.md`` for the index, ``0000-0099/0001.Two Sum/README_EN.md``
    for a problem). A file that is ``d`` directories deep needs ``../`` * d.
    """
    parts = Path(rel_path).parts
    return "../" * (len(parts) - 1)


def clean_readme(text: str, rel_path=None) -> str:
    """Rewrite a README_EN.md to reference only Python (plus SQL) solutions.

    Removes the Chinese-doc link line and drops every non-Python/SQL ``#### <Lang>``
    code tab (a header immediately followed by a fenced code block), regardless of
    the surrounding ``tabs:start/tabs:end`` markers — this tolerates malformed
    upstream files that use stray markers. Empty ``tabs`` blocks are removed.
    Frontmatter, the problem description, prose, and kept code are untouched.

    When ``rel_path`` (the file's path relative to the output root) is given,
    upstream absolute ``/solution/...`` links are rewritten to repo-relative paths
    so they resolve correctly on GitHub. Idempotent.
    """
    lines = text.splitlines()
    out: list[str] = []
    i, n = 0, len(lines)
    in_fence = False
    fence = ""

    while i < n:
        line = lines[i]

        # Preserve fenced code blocks verbatim (prose/description code, kept tabs).
        if in_fence:
            out.append(line)
            if line.lstrip().startswith(fence):
                in_fence, fence = False, ""
            i += 1
            continue

        if CHINESE_DOC_MARKER in line:
            i += 1
            continue

        if _is_fence(line):
            in_fence, fence = True, line.lstrip()[:3]
            out.append(line)
            i += 1
            continue

        header = re.match(r"^####\s+(\S.*?)\s*$", line)
        if header:
            # Look ahead for a fenced code block (optionally after blank lines):
            # only then is this a language code tab we may filter.
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n and _is_fence(lines[j]):
                close = lines[j].lstrip()[:3]
                j += 1
                while j < n and not lines[j].lstrip().startswith(close):
                    j += 1
                if j < n:  # include the closing fence line
                    j += 1
                if _lang_kept(header.group(1)):
                    out.extend(lines[i:j])
                i = j
                continue

        out.append(line)
        i += 1

    result = "\n".join(out)
    # Drop tabs blocks left empty after filtering (whitespace only between markers).
    result = re.sub(
        r"<!-- tabs:start -->\s*<!-- tabs:end -->\n?", "", result
    )
    # Rewrite upstream absolute /solution/ links to repo-relative paths.
    if rel_path is not None:
        result = result.replace("](/solution/", "](" + _solution_link_prefix(rel_path))
    # Collapse runs of blank lines introduced by removals.
    result = re.sub(r"\n{3,}", "\n\n", result)
    if not result.endswith("\n"):
        result += "\n"
    return result


def _log(msg: str) -> None:
    print(msg, flush=True)


def check_git() -> None:
    """Ensure git is available, else exit with a clear, actionable message."""
    if shutil.which("git") is None:
        _log(
            "ERROR: 'git' was not found on PATH.\n"
            "This tool clones doocs/leetcode with a blobless sparse checkout.\n"
            "Install git (https://git-scm.com/downloads) and retry, or use the\n"
            "documented Git Trees API fallback described in README.md."
        )
        sys.exit(2)


def _run_git(args: list[str]) -> None:
    """Run a git command, raising a readable error on failure."""
    proc = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        cmd = " ".join(["git", *args])
        raise RuntimeError(
            f"git command failed ({proc.returncode}): {cmd}\n{proc.stderr.strip()}"
        )


def sync_repo(workdir: Path) -> Path:
    """Shallow, blobless, sparse clone of doocs/leetcode limited to ``solution/``.

    Returns the path to the materialized ``solution/`` directory.
    """
    _log(f"Cloning {REPO_URL} (shallow, blobless, sparse) into {workdir} ...")
    _run_git(
        [
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            REPO_URL,
            str(workdir),
        ]
    )
    _log(f"Restricting checkout to '{SPARSE_SUBTREE}/' ...")
    _run_git(
        ["-C", str(workdir), "sparse-checkout", "set", "--no-cone", SPARSE_SUBTREE]
    )

    solution_dir = workdir / SPARSE_SUBTREE
    if not solution_dir.is_dir():
        raise RuntimeError(
            f"Expected '{SPARSE_SUBTREE}/' subtree not found after sparse checkout: "
            f"{solution_dir}"
        )
    return solution_dir


def _is_wanted(name: str) -> bool:
    return any(fnmatch.fnmatch(name, pat) for pat in WANTED_PATTERNS)


def select_files(solution_dir: Path, limit: int | None = None) -> list[tuple[Path, Path]]:
    """Walk ``solution/`` and return (src, relative_dest) pairs for wanted files.

    ``relative_dest`` is the path relative to the ``solution/`` root (i.e. the
    leading ``solution/`` segment is stripped), preserving the folder layout.

    ``limit`` caps the number of distinct problem folders processed.
    """
    pairs: list[tuple[Path, Path]] = []
    seen_problem_dirs: set[Path] = set()

    for src in sorted(solution_dir.rglob("*")):
        if not src.is_file():
            continue
        if not _is_wanted(src.name):
            continue

        problem_dir = src.parent
        if limit is not None and problem_dir not in seen_problem_dirs:
            if len(seen_problem_dirs) >= limit:
                # Skip files from new problem folders once the limit is reached.
                continue
        seen_problem_dirs.add(problem_dir)

        rel = src.relative_to(solution_dir)
        pairs.append((src, rel))

    return pairs


def copy_out(
    pairs: list[tuple[Path, Path]],
    out: Path,
    overwrite: bool,
    dry_run: bool,
) -> dict[str, int]:
    """Mirror selected files under ``out``. Returns counts for the summary."""
    counts = {"py": 0, "sql": 0, "readme": 0, "skipped": 0, "failed": 0}

    for src, rel in pairs:
        dest = out / rel
        kind = (
            "readme"
            if src.name == "README_EN.md"
            else "py"
            if src.suffix == ".py"
            else "sql"
        )

        # The master index (solutions/README_EN.md, depth 1) is the source of truth
        # for search-index.json, so always refresh it — otherwise newly added
        # problems would never appear in the index on a default (skip-existing) run.
        is_master_index = src.name == "README_EN.md" and len(rel.parts) == 1

        if dest.exists() and not overwrite and not is_master_index:
            counts["skipped"] += 1
            continue

        if dry_run:
            counts[kind] += 1
            continue

        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src.name == "README_EN.md":
                cleaned = clean_readme(src.read_text(encoding="utf-8"), rel_path=rel)
                dest.write_text(cleaned, encoding="utf-8")
            else:
                shutil.copy2(src, dest)
            counts[kind] += 1
        except OSError as exc:
            counts["failed"] += 1
            _log(f"WARN: failed to copy {src} -> {dest}: {exc}")

    return counts


def clean_existing_tree(out: Path) -> dict[str, int]:
    """Apply clean_readme in place to every README_EN.md under ``out``."""
    counts = {"changed": 0, "unchanged": 0, "failed": 0}
    if not out.is_dir():
        _log(f"ERROR: output directory not found: {out}")
        return counts

    for path in sorted(out.rglob("README_EN.md")):
        try:
            original = path.read_text(encoding="utf-8")
            cleaned = clean_readme(original, rel_path=path.relative_to(out))
            if cleaned != original:
                path.write_text(cleaned, encoding="utf-8")
                counts["changed"] += 1
            else:
                counts["unchanged"] += 1
        except OSError as exc:
            counts["failed"] += 1
            _log(f"WARN: failed to clean {path}: {exc}")

    return counts


def write_manifest(pairs: list[tuple[Path, Path]], out: Path, dry_run: bool) -> None:
    """Write manifest.csv describing problem, category, and relative file path."""
    if dry_run:
        return
    manifest = out / "manifest.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["problem", "category", "file"])
        for _src, rel in pairs:
            parts = rel.parts
            # e.g. ('0000-0099', '0005.Longest Palindromic Substring', 'README_EN.md')
            category = parts[0] if len(parts) > 1 else ""
            problem = parts[-2] if len(parts) >= 2 else ""
            writer.writerow([problem, category, rel.as_posix()])
    _log(f"Wrote manifest: {manifest}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Mirror English write-ups and Python/SQL solutions from doocs/leetcode."
        )
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("solutions"),
        help="Output directory for the mirrored tree (default: ./solutions).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only process the first N problem folders (for testing).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be copied without writing files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files (default: skip existing).",
    )
    parser.add_argument(
        "--keep-workdir",
        action="store_true",
        help="Do not delete the temporary git working directory (for debugging).",
    )
    parser.add_argument(
        "--clean-existing",
        action="store_true",
        help=(
            "Skip the git sync; instead rewrite existing --out/**/README_EN.md in "
            "place to reference only Python/SQL solutions (removes other languages "
            "and the Chinese-doc link)."
        ),
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        default=None,
        help="Use this path for the git working dir instead of a temp dir.",
    )
    parser.add_argument(
        "--index-out",
        type=Path,
        default=Path("search-index.json"),
        help="Path to write the search index JSON (default: ./search-index.json).",
    )
    parser.add_argument(
        "--no-index",
        action="store_true",
        help=(
            "Do not (re)build the search index after fetching/cleaning. By default "
            "search-index.json is regenerated from the updated index table so newly "
            "fetched problems are searchable on the website."
        ),
    )
    return parser.parse_args(argv)


def rebuild_index(out: Path, index_out: Path, dry_run: bool = False) -> None:
    """Regenerate the website search index from the mirrored index table.

    Reads ``<out>/README_EN.md`` (the master table refreshed by the fetch) and
    writes ``index_out``. Failures are logged as warnings, never fatal, so a
    successful fetch is not undone by an index-build hiccup.
    """
    if dry_run:
        _log("  (dry-run: search index not rebuilt)")
        return
    source = out / "README_EN.md"
    try:
        count = build_index.generate(source, index_out)
        _log(f"  Search index:  {count} entries -> {index_out}")
    except (FileNotFoundError, ValueError) as exc:
        _log(f"WARN: could not rebuild search index: {exc}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.clean_existing:
        _log(f"Cleaning existing README_EN.md files under {args.out} ...")
        counts = clean_existing_tree(args.out)
        _log("")
        _log("=== Clean Summary ===")
        _log(f"  Changed:    {counts['changed']}")
        _log(f"  Unchanged:  {counts['unchanged']}")
        _log(f"  Failed:     {counts['failed']}")
        if not args.no_index:
            rebuild_index(args.out, args.index_out)
        return 0 if counts["failed"] == 0 else 1

    check_git()

    if args.workdir is not None:
        workdir = args.workdir
        workdir.mkdir(parents=True, exist_ok=True)
        created_temp = False
    else:
        workdir = Path(tempfile.mkdtemp(prefix="leetcode-sync-"))
        created_temp = True

    try:
        solution_dir = sync_repo(workdir)

        _log("Selecting target files ...")
        pairs = select_files(solution_dir, limit=args.limit)
        problem_count = len({rel.parts[-2] for _s, rel in pairs if len(rel.parts) >= 2})
        _log(f"Selected {len(pairs)} files across {problem_count} problem folders.")

        counts = copy_out(pairs, args.out, overwrite=args.overwrite, dry_run=args.dry_run)
        write_manifest(pairs, args.out, dry_run=args.dry_run)

        _log("")
        _log("=== Summary ===")
        _log(f"  Problems:      {problem_count}")
        _log(f"  README_EN.md:  {counts['readme']}")
        _log(f"  Python (.py):  {counts['py']}")
        _log(f"  SQL (.sql):    {counts['sql']}")
        _log(f"  Skipped:       {counts['skipped']}")
        _log(f"  Failed:        {counts['failed']}")
        if args.dry_run:
            _log("  (dry-run: no files written)")
        else:
            _log(f"  Output:        {args.out.resolve()}")
        if not args.no_index:
            rebuild_index(args.out, args.index_out, dry_run=args.dry_run)
    except RuntimeError as exc:
        _log(f"ERROR: {exc}")
        return 1
    finally:
        if created_temp and not args.keep_workdir:
            shutil.rmtree(workdir, ignore_errors=True)
            _log(f"Removed working dir: {workdir}")
        elif args.keep_workdir:
            _log(f"Kept working dir: {workdir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
