// Deadhang Labor LLC — portfolio carousel
// Shows a window of photos with the active one big: 2 small · 1 big · 2 small
// in the middle of the list, 1 big · 4 small at the start, 4 small · 1 big at
// the end (3 photos on phones). Clicking the big photo opens the lightbox
// handled in main.js; clicking a small photo makes it the big one.
(function () {
  const carousel = document.getElementById("portfolioCarousel");
  if (!carousel) return;

  const track = carousel.querySelector(".portfolio-carousel-track");
  const slides = Array.from(carousel.querySelectorAll(".portfolio-carousel-slide"));
  const prev = carousel.querySelector(".portfolio-carousel-prev");
  const next = carousel.querySelector(".portfolio-carousel-next");
  const meta = carousel.querySelector(".portfolio-carousel-meta");
  const category = carousel.querySelector(".portfolio-carousel-category");
  const count = carousel.querySelector(".portfolio-carousel-count");
  const caption = carousel.querySelector(".portfolio-carousel-caption");
  const progress = carousel.querySelector(".portfolio-carousel-progress");
  const progressFill = progress?.querySelector("span");
  if (!track || slides.length === 0) return;

  const phone = window.matchMedia("(max-width: 640px)");
  let active = 0;

  function windowSize() {
    return Math.min(slides.length, phone.matches ? 3 : 5);
  }

  function render() {
    const size = windowSize();
    const half = Math.floor(size / 2);
    const first = Math.max(0, Math.min(active - half, slides.length - size));

    slides.forEach((slide, i) => {
      const inWindow = i >= first && i < first + size;
      slide.classList.toggle("is-out", !inWindow);
      slide.classList.toggle("is-active", i === active);
      slide.setAttribute("aria-current", i === active ? "true" : "false");
      if (inWindow) {
        // Visible photos load now even though they are marked lazy.
        const img = slide.querySelector("img");
        if (img && img.loading === "lazy") img.loading = "eager";
      }
    });

    const current = slides[active];
    if (category) category.textContent = current.dataset.category || "";
    if (count) count.textContent = `${active + 1} / ${slides.length}`;
    if (caption) caption.textContent = current.querySelector(".portfolio-caption")?.textContent || "";
    if (progressFill) progressFill.style.width = `${((active + 1) / slides.length) * 100}%`;
    if (prev) prev.disabled = active === 0;
    if (next) next.disabled = active === slides.length - 1;
  }

  function go(index) {
    const target = Math.max(0, Math.min(slides.length - 1, index));
    if (target === active) return;
    active = target;
    render();
  }

  // Small photos become the big one instead of opening the lightbox. Capture
  // phase runs before main.js's click handler on the slide itself.
  let suppressClick = false;
  track.addEventListener("click", (event) => {
    const slide = event.target.closest(".portfolio-carousel-slide");
    if (!slide) return;
    if (suppressClick) {
      suppressClick = false;
      event.stopPropagation();
      event.preventDefault();
      return;
    }
    const index = slides.indexOf(slide);
    if (index !== active) {
      event.stopPropagation();
      event.preventDefault();
      go(index);
    }
  }, true);

  // Enter/Space on a small photo also selects it rather than opening it.
  track.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    const slide = event.target.closest(".portfolio-carousel-slide");
    const index = slides.indexOf(slide);
    if (slide && index !== active) {
      event.stopPropagation();
      event.preventDefault();
      go(index);
      slides[active].focus();
    }
  }, true);

  prev?.addEventListener("click", () => go(active - 1));
  next?.addEventListener("click", () => go(active + 1));

  carousel.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      go(active - 1);
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      go(active + 1);
    } else {
      return;
    }
    if (carousel.contains(document.activeElement) && document.activeElement.classList.contains("portfolio-carousel-slide")) {
      slides[active].focus();
    }
  });

  // Trackpad side-scroll or Shift + mouse wheel moves through the photos.
  // Plain vertical wheel scrolling is left alone so the page still scrolls.
  let wheelTotal = 0;
  let wheelLock = false;
  track.addEventListener("wheel", (event) => {
    const horizontal = Math.abs(event.deltaX) > Math.abs(event.deltaY);
    const delta = horizontal ? event.deltaX : (event.shiftKey ? event.deltaY : 0);
    if (!delta) return;
    event.preventDefault();
    if (wheelLock) return;
    wheelTotal += delta;
    if (Math.abs(wheelTotal) >= 40) {
      go(active + (wheelTotal > 0 ? 1 : -1));
      wheelTotal = 0;
      wheelLock = true;
      setTimeout(() => { wheelLock = false; }, 350);
    }
  }, { passive: false });

  // Swipe (touch) or drag (mouse) left/right.
  let startX = null;
  let startY = null;
  track.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) return;
    startX = event.clientX;
    startY = event.clientY;
  });
  track.addEventListener("pointerup", (event) => {
    if (startX === null) return;
    const dx = event.clientX - startX;
    const dy = event.clientY - startY;
    startX = null;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
      suppressClick = true;
      setTimeout(() => { suppressClick = false; }, 0);
      go(active + (dx < 0 ? 1 : -1));
    }
  });
  track.addEventListener("pointercancel", () => { startX = null; });

  phone.addEventListener?.("change", render);

  [prev, next, meta, caption, progress].forEach((el) => { if (el) el.hidden = false; });
  carousel.classList.add("is-ready");
  render();
}());
