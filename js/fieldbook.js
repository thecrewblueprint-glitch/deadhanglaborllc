// Deadhang Labor LLC — Field Book interactions
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

function closeNav() {
  if (!navToggle || !navLinks) return;
  navLinks.classList.remove('open');
  navToggle.classList.remove('is-open');
  navToggle.setAttribute('aria-expanded', 'false');
}

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.classList.toggle('is-open', open);
    navToggle.setAttribute('aria-expanded', String(open));
  });
  navLinks.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeNav));
  document.addEventListener('click', (event) => {
    if (!navLinks.contains(event.target) && !navToggle.contains(event.target)) closeNav();
  });
}

// Portfolio filters
const filterButtons = [...document.querySelectorAll('[data-filter]')];
const fieldItems = [...document.querySelectorAll('[data-category]')];
filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((item) => item.classList.toggle('active', item === button));
    fieldItems.forEach((item) => {
      const categories = (item.dataset.category || '').split(' ');
      item.hidden = filter !== 'all' && !categories.includes(filter);
    });
  });
});

// Shared lightbox
const lightbox = document.getElementById('portfolioLightbox');
const lightboxImage = document.getElementById('portfolioLightboxImage');
const lightboxCaption = document.getElementById('portfolioLightboxCaption');
const lightboxClose = document.getElementById('portfolioLightboxClose');
let lastFocus = null;

function openLightbox(trigger) {
  if (!lightbox || !lightboxImage) return;
  const image = trigger.closest('figure, .field-item')?.querySelector('img') || trigger.querySelector('img');
  if (!image) return;
  lastFocus = trigger;
  lightboxImage.src = trigger.dataset.full || image.src;
  lightboxImage.alt = image.alt || 'Portfolio image';
  if (lightboxCaption) lightboxCaption.textContent = trigger.dataset.caption || image.alt || '';
  lightbox.hidden = false;
  document.body.classList.add('no-scroll');
  lightboxClose?.focus();
}

function closeLightbox() {
  if (!lightbox || lightbox.hidden) return;
  lightbox.hidden = true;
  lightboxImage.src = '';
  lightboxImage.alt = '';
  if (lightboxCaption) lightboxCaption.textContent = '';
  document.body.classList.remove('no-scroll');
  lastFocus?.focus();
}

document.querySelectorAll('.lightbox-trigger').forEach((trigger) => {
  trigger.addEventListener('click', () => openLightbox(trigger));
});
lightboxClose?.addEventListener('click', closeLightbox);
lightbox?.addEventListener('click', (event) => { if (event.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape') { closeLightbox(); closeNav(); } });

// Essential-storage notice retained from production site policy.
(function cookieNotice() {
  try {
    if (localStorage.getItem('cookieAck')) return;
    const notice = document.createElement('div');
    notice.className = 'cookie-notice';
    notice.setAttribute('role', 'region');
    notice.setAttribute('aria-label', 'Cookie notice');
    notice.innerHTML = '<p>This site uses essential browser storage for basic functionality only. No tracking or advertising cookies are used. <a href="cookies.html">Learn more</a></p><button type="button" class="cookie-notice-dismiss">Got it</button>';
    document.body.appendChild(notice);
    notice.querySelector('button').addEventListener('click', () => {
      localStorage.setItem('cookieAck', '1');
      notice.remove();
    });
  } catch (_) {
    // If storage is unavailable, the site still functions normally.
  }
}());
