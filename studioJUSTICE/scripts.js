/* ═══════════════════════════════════════════════════════
   STUDIO JUSTICE — Scripts
   ═══════════════════════════════════════════════════════ */

/* ─── Custom Cursor ──────────────────────────────────── */
const cursor = document.getElementById('cursor');
const cursorFollower = document.getElementById('cursorFollower');
let mouseX = 0, mouseY = 0;
let followerX = 0, followerY = 0;

document.addEventListener('mousemove', (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  cursor.style.left = mouseX + 'px';
  cursor.style.top  = mouseY + 'px';
});

// Smooth follower with rAF
function animateFollower() {
  followerX += (mouseX - followerX) * 0.12;
  followerY += (mouseY - followerY) * 0.12;
  cursorFollower.style.left = followerX + 'px';
  cursorFollower.style.top  = followerY + 'px';
  requestAnimationFrame(animateFollower);
}
animateFollower();

// Hover state
document.querySelectorAll('a, button, .project-card, .filter-btn, .service-item').forEach(el => {
  el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
  el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
});

/* ─── Nav Scroll State ───────────────────────────────── */
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

/* ─── Mobile Nav Toggle ──────────────────────────────── */
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  navToggle.classList.toggle('open', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

// Close on link click
navLinks.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle.classList.remove('open');
    document.body.style.overflow = '';
  });
});

/* ─── Scroll Fade-In (Intersection Observer) ─────────── */
const fadeEls = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger siblings slightly
      const delay = entry.target.dataset.delay || 0;
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, delay);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

// Add stagger delays to grid cards
document.querySelectorAll('.project-card').forEach((card, i) => {
  card.dataset.delay = (i % 3) * 80;
});
document.querySelectorAll('.service-item').forEach((item, i) => {
  item.dataset.delay = i * 60;
});

fadeEls.forEach(el => observer.observe(el));

/* ─── Portfolio Filter ───────────────────────────────── */
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Update active button
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.dataset.filter;

    projectCards.forEach(card => {
      if (filter === 'all' || card.dataset.category === filter) {
        card.classList.remove('hidden');
        // Re-trigger fade if not yet visible
        if (!card.classList.contains('visible')) {
          observer.observe(card);
        }
      } else {
        card.classList.add('hidden');
      }
    });
  });
});

/* ─── Lightbox ───────────────────────────────────────── */
const lightbox       = document.getElementById('lightbox');
const lightboxClose  = document.getElementById('lightboxClose');
const lightboxIframe = document.getElementById('lightboxIframe');
const lightboxVideo  = document.getElementById('lightboxVideo');
const lightboxPhoto  = document.getElementById('lightboxPhoto');
const lightboxMeta   = document.getElementById('lightboxMeta');

function openLightbox(card) {
  const title    = card.dataset.title;
  const category = card.querySelector('.project-category').textContent;
  const year     = card.dataset.year;
  const type     = card.dataset.type || 'youtube';

  lightboxMeta.textContent = `${category} — ${title} — ${year}`;

  // Hide all, then show the right one
  lightboxIframe.style.display = 'none';
  lightboxVideo.style.display  = 'none';
  lightboxPhoto.style.display  = 'none';

  if (type === 'local-video') {
    lightboxVideo.src = encodeURI(card.dataset.video);
    lightboxVideo.load();
    lightboxVideo.style.display = 'block';
  } else if (type === 'photo') {
    lightboxPhoto.src = card.dataset.photo;
    lightboxPhoto.style.display = 'block';
  } else {
    lightboxIframe.src = card.dataset.video + '?autoplay=1';
    lightboxIframe.style.display = 'block';
  }

  lightbox.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  lightbox.classList.remove('open');
  lightboxIframe.src = '';
  lightboxVideo.pause();
  lightboxVideo.src = '';
  lightboxPhoto.src = '';
  document.body.style.overflow = '';
}

projectCards.forEach(card => {
  card.addEventListener('click', () => openLightbox(card));
});

lightboxClose.addEventListener('click', closeLightbox);

lightbox.addEventListener('click', (e) => {
  if (e.target === lightbox) closeLightbox();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});

/* ─── Contact Form (demo) ────────────────────────────── */
const contactForm = document.getElementById('contactForm');
contactForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const btn = contactForm.querySelector('.form-submit');
  btn.textContent = 'Message Sent';
  btn.style.opacity = '0.5';
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = 'Send Message';
    btn.style.opacity = '';
    btn.disabled = false;
    contactForm.reset();
  }, 3000);
});
