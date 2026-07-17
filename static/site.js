// Lightweight interactions for static GitHub Pages deploy (no React).
(function () {
  // Scroll-reveal animations (CSS classes from original build)
  var revealEls = document.querySelectorAll(".reveal, .stagger");
  if (revealEls.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in");
    });
  }

  // Smooth in-page navigation
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      var id = link.getAttribute("href");
      if (!id || id === "#") return;
      var target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      history.pushState(null, "", id);
    });
  });

  // Demo form — show confirmation (no backend on static hosting)
  document.querySelectorAll("form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Thank you! We will contact you shortly to schedule your demo.");
      form.reset();
    });
  });

  // Header background on scroll
  var header = document.querySelector("header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 24) {
        header.classList.add("bg-white/95", "backdrop-blur-xl", "shadow-sm", "border-b", "border-slate-200/70");
        header.classList.remove("bg-transparent");
      } else {
        header.classList.remove("bg-white/95", "backdrop-blur-xl", "shadow-sm", "border-b", "border-slate-200/70");
        header.classList.add("bg-transparent");
      }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
