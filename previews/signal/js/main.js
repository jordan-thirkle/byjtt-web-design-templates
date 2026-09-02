// Signal — progressive enhancements only; the page works without JS.
(function () {
  "use strict";

  document.documentElement.classList.add("js");

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  var form = document.getElementById("wait-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = (document.getElementById("wl-email") || {}).value || "";
      var subject = encodeURIComponent("Signal early access");
      var body = encodeURIComponent("Hi Signal team,\n\nPlease add me to early access.\nWork email: " + email + "\n\nThanks!");
      window.location.href = "mailto:early@signal.dev?subject=" + subject + "&body=" + body;
    });
  }

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) || reduceMotion || items.length === 0) {
    items.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach(function (el) { io.observe(el); });
})();
