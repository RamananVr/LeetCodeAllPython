# LeetCodeAllPython

A curated collection of LeetCode solutions, trimmed to **Python** (and **SQL** for
database problems) only, plus a static, client-side **search website** served from
GitHub Pages.

## Repository layout

| Path | Purpose |
|------|---------|
| `solutions/` | Mirrored problem folders (`README_EN.md`, `Solution.py`, `Solution.sql`, …). |
| `solutions/README_EN.md` | Master index table (number, title, tags, difficulty). |
| `fetch_solutions.py` | Fetches + cleans solutions. |
| `build_index.py` | Generates `search-index.json` from the index table. |
| `index.html`, `assets/` | The static search website. |
| `.nojekyll` | Makes GitHub Pages serve `.md` files verbatim. |

## Search website

A dependency-free (vanilla HTML/CSS/JS) site that searches the mirrored solutions by
**problem name, number, or tag**, filters by difficulty, and renders the selected
problem's `README_EN.md` (Python/SQL, syntax-highlighted) in-page. LaTeX math in the
write-ups (`$...$` / `$$...$$`) is rendered with a locally-vendored **KaTeX**
(`assets/vendor/katex/`), so the site has no runtime CDN dependency.

### Regenerate the search index

Run whenever `solutions/README_EN.md` changes:

```bash
python build_index.py            # writes search-index.json
```

> **Note:** `fetch_solutions.py` already rebuilds the index automatically after a
> fetch or clean (see below), so you normally only run this directly for a manual
> one-off regeneration.

A GitHub Actions workflow (`.github/workflows/build-index.yml`) also rebuilds and
commits `search-index.json` automatically whenever `solutions/README_EN.md` changes
on `main` — so the index stays in sync even if the tree is edited without running the
fetcher. For the workflow's bot commit to push, enable write access once:
**Settings → Actions → General → Workflow permissions → "Read and write permissions"**.

### Run locally

```bash
python -m http.server 8000
# then open http://localhost:8000/index.html
```

The app fetches `search-index.json` and the individual `solutions/**/README_EN.md`
files at runtime, so it must be served over HTTP (not opened via `file://`).

### Deploy on GitHub Pages

The site is served from the **repository root** so the app can fetch the `solutions/`
tree at runtime.

1. Push to `main`.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch **`main`** and folder **`/ (root)`**, then **Save**.

The `.nojekyll` file (already at the root) disables Jekyll so the frontmatter `.md`
files are served raw for the client-side markdown renderer.

## Fetching / refreshing solutions

`fetch_solutions.py` fetches the solution source, copies Python/SQL solutions and
`README_EN.md` files, and cleans each README to reference only Python (plus SQL for
database problems), keeping tags, the question, and SQL blocks.

```bash
python fetch_solutions.py                 # fetch + clean into solutions/
python fetch_solutions.py --clean-existing  # re-clean the already-fetched tree
```

The master index table (`solutions/README_EN.md`) is always refreshed on a fetch —
even in the default skip-existing mode — so newly added problems appear in it. After
the fetch (or clean) completes, `search-index.json` is **rebuilt automatically** from
that table, so new problems are immediately searchable on the website. Control this with:

```bash
python fetch_solutions.py --no-index                 # skip the automatic index rebuild
python fetch_solutions.py --index-out search-index.json  # customize the index output path
```
