// ByJTT marketplace: copy-to-clipboard with a human fallback (no dead buttons).
(function () {
  "use strict";
  var live = document.createElement("p");
  live.className = "visually-hidden";
  live.setAttribute("aria-live", "polite");
  document.body.appendChild(live);

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  document.querySelectorAll(".copy-btn[data-copy-target]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var pre = document.getElementById(btn.getAttribute("data-copy-target"));
      if (!pre) return;
      var text = pre.textContent;
      var done = function (ok) {
        if (ok) {
          btn.textContent = "Copied ✓";
          live.textContent = "Prompt copied to clipboard";
          setTimeout(function () { btn.textContent = "Copy"; }, 2000);
        } else {
          btn.textContent = "Copy failed — select the text above";
          live.textContent = "Copy failed; select the prompt text manually";
        }
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(fallbackCopy(text)); });
      } else {
        done(fallbackCopy(text));
      }
    });
  });
})();

// Explore filters (progressive: no-JS shows everything)
(function () {
  "use strict";
  var cat = "all", tier = "all";
  var cards = document.querySelectorAll(".res-card[data-cat]");
  var empty = document.getElementById("res-empty");
  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (cat === "all" || c.getAttribute("data-cat") === cat) &&
               (tier === "all" || c.getAttribute("data-tier") === tier);
      c.hidden = !ok;
      if (ok) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
  }
  document.querySelectorAll(".filter-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      if (b.hasAttribute("data-filter-cat")) {
        cat = b.getAttribute("data-filter-cat");
        document.querySelectorAll("[data-filter-cat]").forEach(function (x) { x.classList.toggle("is-on", x === b); });
      }
      if (b.hasAttribute("data-filter-tier")) {
        tier = b.getAttribute("data-filter-tier");
        document.querySelectorAll("[data-filter-tier]").forEach(function (x) { x.classList.toggle("is-on", x === b); });
      }
      apply();
    });
  });
})();
