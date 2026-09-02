// Embercraft — progressive enhancements only; page fully works without JS.
(function () {
  "use strict";

  // Flag JS availability: content-hiding animations only run when this class exists.
  document.documentElement.classList.add("js");

  // Footer year
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // Roast-list form (honest static flow: opens a pre-filled email)
  var form = document.getElementById("roast-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = (document.getElementById("sub-email") || {}).value || "";
      var cadence = (document.getElementById("sub-cadence") || {}).value || "Every 2 weeks";
      var subject = encodeURIComponent("Start my coffee plan (" + cadence + ")");
      var body = encodeURIComponent("Hi Embercraft,\n\nI'd like to start a plan on this cadence: " + cadence + ".\nMy email: " + email + "\n\nThanks!");
      window.location.href = "mailto:hello@embercraft.coffee?subject=" + subject + "&body=" + body;
    });
  }

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Reveal on scroll (disabled by CSS under prefers-reduced-motion)
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
