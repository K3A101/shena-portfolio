/* ==========================================================================
   Main script
   ========================================================================== */

// Let CSS know JS is available (used for the nav toggle and reveal effects)
document.documentElement.classList.replace("no-js", "js");

/* ---- Mobile navigation ---- */
const navToggle = document.querySelector(".nav__toggle");
const navList = document.querySelector(".nav__list");

function closeNav() {
  navToggle.setAttribute("aria-expanded", "false");
  navList.classList.remove("is-open");
}

if (navToggle && navList) {
  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isOpen));
    navList.classList.toggle("is-open", !isOpen);
  });

  // Close the menu after choosing a link
  navList.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeNav();
  });

  // Close with Escape and return focus to the toggle
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navList.classList.contains("is-open")) {
      closeNav();
      navToggle.focus();
    }
  });
}

/* ---- Footer year ---- */
document.querySelectorAll("[data-year]").forEach((el) => {
  el.textContent = new Date().getFullYear();
});

/* ---- Sliders (prev/next buttons; without JS the track still scrolls) ---- */
document.querySelectorAll("[data-slider]").forEach((slider) => {
  const track = slider.querySelector("[data-slider-track]");
  const prev = slider.querySelector("[data-slider-prev]");
  const next = slider.querySelector("[data-slider-next]");
  if (!track || !prev || !next) return;

  prev.parentElement.hidden = false;

  const step = () => {
    const item = track.firstElementChild;
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    return item ? item.getBoundingClientRect().width + gap : track.clientWidth;
  };

  const update = () => {
    const max = track.scrollWidth - track.clientWidth;
    prev.disabled = track.scrollLeft <= 1;
    next.disabled = track.scrollLeft >= max - 1;
    // Hide the buttons when everything already fits
    prev.parentElement.hidden = max <= 1;
  };

  const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
  prev.addEventListener("click", () => track.scrollBy({ left: -step(), behavior }));
  next.addEventListener("click", () => track.scrollBy({ left: step(), behavior }));
  track.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
});

/* ---- Reveal elements on scroll ---- */
const revealItems = document.querySelectorAll(".reveal");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}
