// The site works without this file. It adds closing the Apps menu on an outside click or
// Escape, and on the home page, the category filters and fading cards in on scroll.
document.addEventListener('click', (event) => {
  document.querySelectorAll('.apps-menu[open]').forEach((menu) => {
    if (!menu.contains(event.target)) menu.open = false;
  });
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  document.querySelectorAll('.apps-menu[open]').forEach((menu) => {
    menu.open = false;
    menu.querySelector('summary').focus();
  });
});

const filters = document.querySelector('.filters');
const cards = document.querySelectorAll('.apps .card');
if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', (event) => {
    const chosen = event.target.closest('button');
    if (!chosen) return;
    filters.querySelectorAll('button').forEach((button) => {
      button.setAttribute('aria-pressed', String(button === chosen));
    });
    cards.forEach((card) => {
      card.classList.remove('reveal');
      card.hidden = chosen.dataset.tag !== 'all' && !card.dataset.tags.split(' ').includes(chosen.dataset.tag);
    });
  });
}

if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries) => {
    entries.filter((entry) => entry.isIntersecting).forEach((entry) => {
      entry.target.classList.remove('reveal');
      observer.unobserve(entry.target);
    });
  });
  cards.forEach((card) => {
    if (card.getBoundingClientRect().top < innerHeight) return;
    card.classList.add('reveal');
    observer.observe(card);
  });
}
