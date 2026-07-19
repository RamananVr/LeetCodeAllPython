# LeetCode Solution Fetcher

Mirror a local copy of every problem's English write-up and Python/SQL solutions
from [`doocs/leetcode`](https://github.com/doocs/leetcode), preserving the repo's
folder layout.

## What it fetches

For each problem folder under the upstream `solution/` tree it copies:

- `README_EN.md` — English problem statement + editorial. On copy, each write-up is
  **rewritten to reference only Python (plus SQL for database problems)**: all other
  programming-language code tabs and the Chinese-doc (`中文文档`) link are stripped. The
  YAML frontmatter (including `tags:`) and the full problem description are preserved.
- `Solution*.py` — every Python solution (`Solution.py`, `Solution2.py`, ...)
- `Solution*.sql` — every SQL solution (database problems only)

Output mirrors the source layout, e.g.:

```
solutions/0000-0099/0005.Longest Palindromic Substring/README_EN.md
solutions/0000-0099/0005.Longest Palindromic Substring/Solution.py
```

## How it works

Instead of thousands of individual HTTP downloads (and API rate limits), it drives
`git` to create a **shallow, blobless, sparse** working directory limited to the
`solution/` subtree, walks it on the local filesystem, copies the wanted files, and
then deletes the temporary working directory.

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/doocs/leetcode.git <workdir>
git -C <workdir> sparse-checkout set --no-cone solution
```

- `--depth 1` — no history (fast, small).
- `--filter=blob:none` — file contents fetched lazily, not the whole repo.
- `--sparse` + `sparse-checkout set solution` — only the `solution/` subtree.

## Requirements

- Python 3.8+ (standard library only — no third-party packages)
- `git` on `PATH`

## Usage

```bash
# Test with a small slice first (no history, quick):
python fetch_solutions.py --limit 20

# Full run:
python fetch_solutions.py

# Preview without writing anything:
python fetch_solutions.py --limit 20 --dry-run

# Clean already-fetched READMEs in place (Python/SQL only):
python fetch_solutions.py --clean-existing
```

### Options

| Flag | Description |
|------|-------------|
| `--out PATH` | Output directory for the mirrored tree (default: `./solutions`). |
| `--limit N` | Only process the first N problem folders (for testing). |
| `--dry-run` | Report what would be copied without writing files. |
| `--overwrite` | Overwrite existing files (default: skip existing). |
| `--clean-existing` | Skip the git sync; rewrite existing `--out/**/README_EN.md` in place to reference only Python/SQL (removes other languages and the Chinese-doc link). Idempotent. |
| `--keep-workdir` | Keep the temporary git working directory (debugging). |
| `--workdir PATH` | Use this path for the git working dir instead of a temp dir. |

## Output

- `solutions/` — mirrored tree of `README_EN.md` / `Solution*.py` / `Solution*.sql`.
- `solutions/manifest.csv` — one row per copied file: `problem, category, file`.
- A run summary printed to stdout (problems, README/py/sql counts, skipped, failed).

The temporary git working directory is deleted automatically on completion (unless
`--keep-workdir` is given), so the `solutions/` output stays clean.

## Fallback if `git` is unavailable

The script requires `git`. If `git` cannot be installed, the equivalent data can be
retrieved via the GitHub Git Trees API (`GET /repos/doocs/leetcode/git/trees/main?recursive=1`)
plus `raw.githubusercontent.com` downloads — but that path needs custom concurrency
and retry handling and can hit API rate limits for a repo this large, so the git-based
approach above is preferred.

## Windows note

On deeply nested paths you may hit the legacy 260-character path limit. Run under a
short `--out` root, and/or enable long paths
(`git config --global core.longpaths true` and the Windows `LongPathsEnabled` policy).
# LeetCodeAllPython
