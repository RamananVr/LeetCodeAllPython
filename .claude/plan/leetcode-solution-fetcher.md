# Implementation Plan: LeetCode Solution Fetcher

Fetch, from `doocs/leetcode`, a local mirror of every problem's English write-up and
Python solutions (plus SQL for database problems), preserving the repo's folder layout.

### Task Type
- [x] Backend (data-fetching CLI script → Codex domain)
- [ ] Frontend
- [ ] Fullstack

---

## Requirement (confirmed)

- **Scope:** the **entire** `doocs/leetcode` repo (~3000+ problem folders).
- **Per problem folder**, download:
  - `README_EN.md` (English problem statement + editorial)
  - Every `Solution*.py` file (`Solution.py`, `Solution2.py`, ...)
  - Every `Solution*.sql` file (database problems only)
- **Output:** recreate the source layout locally, e.g.
  `solutions/0000-0099/0005.Longest Palindromic Substring/README_EN.md`.

---

## Technical Solution

**Chosen approach: sync a temporary git working directory, copy out the wanted files, then
delete the temp dir.** This avoids any API rate limits entirely and reuses git's own robust,
resumable transfer instead of thousands of individual HTTP downloads.

1. **Shallow, blobless, sparse clone** into a temp working dir (e.g. `%TEMP%\leetcode-sync`
   / `tempfile.mkdtemp()`):
   ```
   git clone --depth 1 --filter=blob:none --sparse \
       https://github.com/doocs/leetcode.git <workdir>
   git -C <workdir> sparse-checkout set --no-cone solution
   ```
   - `--depth 1` → no history (fast, small).
   - `--filter=blob:none` → file contents fetched lazily/on demand, not the whole repo.
   - `--sparse` + `sparse-checkout set solution` → only the `solution/` subtree is materialized.
2. **Walk** `<workdir>/solution/**` locally (plain filesystem, no network) and select files
   whose basename is `README_EN.md`, matches `Solution*.py`, or matches `Solution*.sql`.
3. **Copy** each selected file to `solutions/<relative path minus the leading "solution/">`,
   preserving the folder layout (`shutil.copy2`, `pathlib` for Windows-safe paths).
4. Write a `manifest.csv` (problem, category, files copied) and a run summary.
5. **Clean up:** delete the temp working dir (respect a `--keep-workdir` flag for debugging).

**Language/tooling:** Python 3 stdlib (`subprocess` to drive `git`, `pathlib`, `shutil`,
`fnmatch`, `csv`, `tempfile`) — no third-party deps. Requires `git` on PATH (already available
in this environment). Optional `GITHUB_TOKEN` only needed for private/rate-limited networks.

**Why this over the API approach:** no 60 req/hr limit, no per-file HTTP orchestration, git
handles retries/packing, and a blobless+sparse clone still transfers only the `solution/`
files it needs. The temp dir is disposable, so the final `solutions/` output stays clean.

**Alternatives (documented, not chosen):**
- *Git Trees API (`?recursive=1`) + `raw.githubusercontent.com` downloads.* Works and needs no
  local git, but requires custom concurrency/retry and can hit API limits on the tree call for
  a repo this large (`truncated` responses). Kept as a fallback if `git` is unavailable.
- *Full `git clone`.* Simplest, but pulls all history and every language's solutions — far more
  data than needed.

---

## Implementation Steps

1. **Scaffold** — Create `fetch_solutions.py` and `README.md`. *Deliverable:* runnable `argparse` CLI (`--out`, `--limit`, `--dry-run`, `--overwrite`, `--keep-workdir`, `--workdir`).
2. **Sync working dir** — Implement `sync_repo(workdir)`: shallow blobless sparse clone of `doocs/leetcode` limited to `solution/` (via `subprocess` git calls, with error handling if `git` missing → suggest API fallback). *Deliverable:* populated `<workdir>/solution/` tree.
3. **Filter targets** — Implement `select_files(workdir)` walking `solution/**` and keeping `README_EN.md`, `Solution*.py`, `Solution*.sql`. *Deliverable:* list of (src path, local dest) pairs.
4. **Copy layer** — Implement `copy_out(files, out)` mirroring the layout under `--out` (skip existing unless `--overwrite`, create parent dirs). *Deliverable:* `solutions/` output tree.
5. **Manifest + summary** — Emit `manifest.csv` and print counts (problems, py, sql, skipped, failed). *Deliverable:* auditable run output.
6. **Cleanup** — Delete the temp working dir in a `finally` block unless `--keep-workdir`. *Deliverable:* no leftover temp data.
7. **Verify** — Run with `--limit` (e.g. 20 problems) and confirm `0005` folder has `README_EN.md` + `Solution.py`; confirm a known DB problem yields `.sql`; confirm workdir is removed. *Deliverable:* validated output; then optional full run.

---

## Key Files

| File | Operation | Description |
|------|-----------|-------------|
| `fetch_solutions.py` | Create | Main CLI: git sync, walk/filter, copy-out, manifest, temp-dir cleanup. |
| `README.md` | Create | Usage, git prerequisite, output layout, `--keep-workdir`/fallback notes. |
| `solutions/` (dir) | Create (generated) | Mirrored output tree; gitignored. |
| `.gitignore` | Create/Modify | Ignore `solutions/`, `manifest.csv`, and any temp workdir. |

---

## Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| `git` not on PATH | Detect at startup; clear error + documented Git Trees API fallback path. |
| Sparse clone still large / slow | `--depth 1` + `--filter=blob:none` + sparse `solution/` only pulls needed blobs. |
| Temp dir left behind on crash | Create via `tempfile.mkdtemp()`; delete in a `finally` block; `--keep-workdir` opt-out. |
| Disk space for working dir | Blobless sparse clone keeps footprint small; workdir deleted after copy-out. |
| Filenames with spaces (`0005.Longest Palindromic Substring`) | Filesystem walk + `pathlib`/`shutil` handle spaces natively (no URL encoding needed). |
| Multi-file solutions (`Solution2.py`, `Solution.sql`) | Glob `Solution*.py` / `Solution*.sql`, not exact names. |
| Windows path length limits on deep nested dirs | Write under a short `--out` root; rely on `pathlib`; note long-path option in README. |

---

### SESSION_ID (for /ccg:execute use)
- CODEX_SESSION: n/a (ccg-workflow runtime not installed; planned with built-in tools)
- GEMINI_SESSION: n/a
