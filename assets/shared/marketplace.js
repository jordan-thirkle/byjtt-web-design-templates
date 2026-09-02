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
