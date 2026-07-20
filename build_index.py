#!/usr/bin/env python3
"""Generate search-index.json from solutions/README_EN.md.

Parses the markdown index table (columns: #, Solution, Tags, Difficulty, Remark)
into a compact JSON array used by the static search website.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROW_RE = re.compile(r"^\|(.+)\|\s*$")
LINK_RE = re.compile(r"\[(?P<title>.+?)\]\((?P<path>.+?)\)")
TAG_RE = re.compile(r"`([^`]+)`")


def split_row(line: str) -> list[str] | None:
    """Split a markdown table row into trimmed cell values, or None if not a row."""
    m = ROW_RE.match(line.strip())
    if not m:
        return None
    return [c.strip() for c in m.group(1).split("|")]


def parse_index(md: str) -> list[dict]:
    entries: list[dict] = []
    for line in md.splitlines():
        cells = split_row(line)
        if not cells or len(cells) < 4:
            continue
        num_cell, sol_cell, tags_cell, diff_cell = cells[0], cells[1], cells[2], cells[3]
        # Skip header / separator rows.
        if not num_cell.isdigit():
            continue
        link = LINK_RE.search(sol_cell)
        if not link:
            continue
        title = link.group("title").strip()
        path = unquote(link.group("path").strip())
        tags = [t.strip() for t in TAG_RE.findall(tags_cell)]
        difficulty = diff_cell.strip()
        entries.append(
            {
                "id": num_cell,
                "num": int(num_cell),
                "title": title,
                "path": path,
                "tags": tags,
                "difficulty": difficulty,
            }
        )
    return entries


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--source",
        default="solutions/README_EN.md",
        help="Path to the solutions index README (default: solutions/README_EN.md)",
    )
    ap.add_argument(
        "--out",
        default="search-index.json",
        help="Output JSON path (default: search-index.json)",
    )
    args = ap.parse_args()

    src = Path(args.source)
    if not src.is_file():
        print(f"error: source not found: {src}", file=sys.stderr)
        return 1

    md = src.read_text(encoding="utf-8")
    entries = parse_index(md)
    if not entries:
        print("error: no rows parsed from index table", file=sys.stderr)
        return 1

    Path(args.out).write_text(
        json.dumps(entries, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Wrote {len(entries)} entries to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
