// Deadhang Labor LLC — main.js
const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");

function closeNavigation() {
  if (!navToggle || !navLinks) return;
  navLinks.classList.remove("open");
  navToggle.classList.remove("is-open");
  navToggle.setAttribute("aria-expanded", "false");
}

if (navToggle && navLinks) {
  navToggle.setAttribute("aria-expanded", navToggle.getAttribute("aria-expanded") || "false");

  navToggle.addEventListener("click", () => {
    const open = navLinks.classList.toggle("open");
    navToggle.classList.toggle("is-open", open);
    navToggle.setAttribute("aria-expanded", String(open));
  });

  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeNavigation);
  });

  document.addEventListener("click", (event) => {
    if (!navLinks.contains(event.target) && !navToggle.contains(event.target)) {
      closeNavigation();
    }
  });
}

const lightbox = document.getElementById("portfolioLightbox");
const lightboxImage = document.getElementById("portfolioLightboxImage");
const lightboxCaption = document.getElementById("portfolioLightboxCaption");
const lightboxClose = document.getElementById("portfolioLightboxClose");
let lastFocusedElement = null;

function openLightbox(trigger) {
  const image = trigger?.querySelector("img");

  if (!lightbox || !lightboxImage || !image) return;

  lastFocusedElement = trigger;
  lightboxImage.src = trigger.dataset.full || image.src;
  lightboxImage.alt = image.alt || "Portfolio image";

  if (lightboxCaption) {
    lightboxCaption.textContent = trigger.dataset.caption || image.alt || "Portfolio image";
  }

  lightbox.hidden = false;
  document.body.classList.add("no-scroll");
  lightboxClose?.focus();
}

function closeLightbox() {
  if (!lightbox || lightbox.hidden) return;

  lightbox.hidden = true;
  lightboxImage.src = "";
  lightboxImage.alt = "";

  if (lightboxCaption) {
    lightboxCaption.textContent = "";
  }

  document.body.classList.remove("no-scroll");
  lastFocusedElement?.focus();
}

document.querySelectorAll(".portfolio-lightbox-trigger").forEach((trigger) => {
  trigger.addEventListener("click", () => openLightbox(trigger));
  trigger.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      openLightbox(trigger);
    }
  });
});

lightboxClose?.addEventListener("click", closeLightbox);

lightbox?.addEventListener("click", (event) => {
  if (event.target === lightbox) {
    closeLightbox();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeLightbox();
  }
});

// Cookie notice
(function () {
  if (localStorage.getItem("cookieAck")) return;

  const notice = document.createElement("div");
  notice.className = "cookie-notice";
  notice.setAttribute("role", "region");
  notice.setAttribute("aria-label", "Cookie notice");

  const message = document.createElement("p");
  message.append(
    document.createTextNode(
      "This site uses essential cookies and browser storage for basic functionality only. No tracking or advertising cookies are used. "
    )
  );

  const learnMore = document.createElement("a");
  learnMore.href = "cookies.html";
  learnMore.textContent = "Learn more";
  message.append(learnMore);

  const dismiss = document.createElement("button");
  dismiss.type = "button";
  dismiss.className = "cookie-notice-dismiss";
  dismiss.textContent = "Got it";

  notice.append(message, dismiss);
  document.body.appendChild(notice);

  dismiss.addEventListener("click", () => {
    notice.remove();
    localStorage.setItem("cookieAck", "1");
  });
})();
