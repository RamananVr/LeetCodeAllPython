/* LeetCode Solutions static search app. */
(function () {
  "use strict";

  var MAX_ROWS = 200;
  var state = {
    all: [],
    query: "",
    difficulty: "",
    tags: [],          // active tag filters (AND)
    selectedId: null,
  };

  var els = {};

  function $(id) { return document.getElementById(id); }

  /* ---- Math (KaTeX via marked extension) -------------------------------- */

  function registerMathExtension() {
    if (!window.marked || !window.katex || !window.marked.use) return;

    function render(tex, displayMode, raw) {
      try {
        return window.katex.renderToString(tex, {
          displayMode: displayMode,
          throwOnError: false,
        });
      } catch (e) {
        return raw;
      }
    }

    window.marked.use({
      extensions: [
        {
          name: "blockMath",
          level: "block",
          start: function (src) { var i = src.indexOf("$$"); return i < 0 ? undefined : i; },
          tokenizer: function (src) {
            var m = /^\$\$([\s\S]+?)\$\$/.exec(src);
            if (m) {
              return { type: "blockMath", raw: m[0], text: m[1].trim() };
            }
          },
          renderer: function (token) {
            return render(token.text, true, token.raw);
          },
        },
        {
          name: "inlineMath",
          level: "inline",
          start: function (src) { var i = src.indexOf("$"); return i < 0 ? undefined : i; },
          tokenizer: function (src) {
            // Single-$ inline math; not $$ (handled by blockMath). Allow escaped chars.
            var m = /^\$(?!\$)((?:\\.|[^$\\])+?)\$/.exec(src);
            if (m) {
              return { type: "inlineMath", raw: m[0], text: m[1].trim() };
            }
          },
          renderer: function (token) {
            return render(token.text, false, token.raw);
          },
        },
      ],
    });
  }

  function debounce(fn, ms) {
    var t;
    return function () {
      var args = arguments, ctx = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(ctx, args); }, ms);
    };
  }

  function normalize(s) { return (s || "").toLowerCase(); }

  /* ---- Filtering & ranking ---------------------------------------------- */

  function scoreEntry(entry, q) {
    // Returns a sort rank (lower = better), or null if it doesn't match q.
    if (!q) return 0;

    // Numeric query → match by problem number.
    if (/^\d+$/.test(q)) {
      var nStr = String(entry.num);
      var padded = entry.id; // zero-padded id like "0175"
      if (nStr === q || padded === q) return 0;
      if (nStr.indexOf(q) === 0 || padded.indexOf(q) === 0) return 1;
      if (nStr.indexOf(q) !== -1) return 3;
      return null;
    }

    var title = normalize(entry.title);
    if (title === q) return 0;
    if (title.indexOf(q) === 0) return 1;
    if (title.indexOf(q) !== -1) return 2;

    for (var i = 0; i < entry.tags.length; i++) {
      if (normalize(entry.tags[i]).indexOf(q) !== -1) return 4;
    }
    return null;
  }

  function currentResults() {
    var q = normalize(state.query.trim());
    var out = [];
    for (var i = 0; i < state.all.length; i++) {
      var e = state.all[i];

      if (state.difficulty && e.difficulty !== state.difficulty) continue;

      if (state.tags.length) {
        var ok = true;
        for (var t = 0; t < state.tags.length; t++) {
          if (e.tags.indexOf(state.tags[t]) === -1) { ok = false; break; }
        }
        if (!ok) continue;
      }

      var rank = scoreEntry(e, q);
      if (rank === null) continue;
      out.push({ e: e, rank: rank });
    }

    out.sort(function (a, b) {
      if (a.rank !== b.rank) return a.rank - b.rank;
      return a.e.num - b.e.num;
    });
    return out;
  }

  /* ---- Rendering -------------------------------------------------------- */

  function renderActiveTags() {
    els.activeTags.innerHTML = "";
    state.tags.forEach(function (tag) {
      var chip = document.createElement("span");
      chip.className = "chip";
      chip.innerHTML = "";
      chip.appendChild(document.createTextNode(tag + " "));
      var x = document.createElement("span");
      x.className = "x";
      x.textContent = "×";
      chip.appendChild(x);
      chip.title = "Remove filter";
      chip.addEventListener("click", function () {
        state.tags = state.tags.filter(function (t) { return t !== tag; });
        renderActiveTags();
        renderResults();
      });
      els.activeTags.appendChild(chip);
    });
  }

  function addTag(tag) {
    if (state.tags.indexOf(tag) === -1) {
      state.tags.push(tag);
      renderActiveTags();
      renderResults();
    }
  }

  function renderResults() {
    var results = currentResults();
    var total = results.length;
    var shown = Math.min(total, MAX_ROWS);

    els.count.textContent =
      total === 0 ? "No results"
      : (total > MAX_ROWS ? ("Showing " + shown + " of " + total + " — refine your search")
                          : (total + (total === 1 ? " result" : " results")));

    els.results.innerHTML = "";
    var frag = document.createDocumentFragment();

    for (var i = 0; i < shown; i++) {
      var e = results[i].e;
      var li = document.createElement("li");
      li.className = "result-item" + (e.id === state.selectedId ? " active" : "");
      li.dataset.id = e.id;

      var title = document.createElement("div");
      title.className = "result-title";
      var num = document.createElement("span");
      num.className = "result-num";
      num.textContent = e.id + " · ";
      title.appendChild(num);
      title.appendChild(document.createTextNode(e.title));
      li.appendChild(title);

      var meta = document.createElement("div");
      meta.className = "result-meta";
      var diff = document.createElement("span");
      diff.className = "diff " + e.difficulty;
      diff.textContent = e.difficulty;
      meta.appendChild(diff);

      e.tags.forEach(function (tag) {
        var ts = document.createElement("span");
        ts.className = "tag";
        ts.textContent = tag;
        ts.title = "Filter by " + tag;
        ts.addEventListener("click", function (ev) {
          ev.stopPropagation();
          addTag(this.textContent);
        });
        meta.appendChild(ts);
      });
      li.appendChild(meta);

      li.addEventListener("click", function () { select(this.dataset.id); });
      frag.appendChild(li);
    }
    els.results.appendChild(frag);
  }

  /* ---- Detail view ------------------------------------------------------ */

  function stripFrontmatter(text) {
    if (text.slice(0, 3) === "---") {
      var end = text.indexOf("\n---", 3);
      if (end !== -1) {
        var nl = text.indexOf("\n", end + 1);
        return nl === -1 ? "" : text.slice(nl + 1);
      }
    }
    return text;
  }

  function highlightAll(container) {
    var blocks = container.querySelectorAll("pre code");
    for (var i = 0; i < blocks.length; i++) {
      try { window.hljs.highlightElement(blocks[i]); } catch (e) { /* ignore */ }
    }
  }

  function select(id) {
    if (!id) return;
    state.selectedId = id;
    renderResults();

    var entry = null;
    for (var i = 0; i < state.all.length; i++) {
      if (state.all[i].id === id) { entry = state.all[i]; break; }
    }
    if (!entry) return;

    els.empty.hidden = true;
    els.content.hidden = false;
    els.content.innerHTML = "<p class='detail-loading'>Loading…</p>";

    var url = "solutions/" + entry.path.split("/").map(encodeURIComponent).join("/");
    fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.text();
      })
      .then(function (md) {
        var body = stripFrontmatter(md);
        els.content.innerHTML = window.marked.parse(body);
        highlightAll(els.content);
        els.detail.scrollTop = 0;
      })
      .catch(function (err) {
        els.content.innerHTML =
          "<p class='detail-error'>Failed to load solution: " + err.message + "</p>";
      });
  }

  /* ---- Init ------------------------------------------------------------- */

  function initTheme() {
    var toggle = $("theme-toggle");
    var light = $("hljs-light");
    var dark = $("hljs-dark");

    function apply(theme) {
      document.documentElement.setAttribute("data-theme", theme);
      var isDark = theme === "dark";
      dark.disabled = !isDark;
      light.disabled = isDark;
      toggle.textContent = isDark ? "☀️" : "🌙";
      try { localStorage.setItem("lc-theme", theme); } catch (e) {}
    }

    var saved = null;
    try { saved = localStorage.getItem("lc-theme"); } catch (e) {}
    if (!saved && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      saved = "dark";
    }
    apply(saved || "light");

    toggle.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme");
      apply(cur === "dark" ? "light" : "dark");
    });
  }

  function init() {
    els = {
      search: $("search"),
      difficulty: $("difficulty"),
      activeTags: $("active-tags"),
      count: $("result-count"),
      results: $("results"),
      empty: $("detail-empty"),
      content: $("detail-content"),
      detail: document.querySelector(".detail"),
    };

    if (window.marked) {
      window.marked.setOptions({ gfm: true, breaks: false });
    }
    registerMathExtension();

    initTheme();

    els.search.addEventListener("input", debounce(function () {
      state.query = els.search.value;
      renderResults();
    }, 120));

    els.difficulty.addEventListener("change", function () {
      state.difficulty = els.difficulty.value;
      renderResults();
    });

    fetch("search-index.json")
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        state.all = data;
        renderResults();
      })
      .catch(function (err) {
        els.count.textContent = "Failed to load index: " + err.message;
      });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
