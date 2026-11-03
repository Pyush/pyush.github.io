// The Apps menu works without this; it only adds closing on an outside click or Escape.
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
