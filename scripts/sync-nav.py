"""Rewrite the header's Apps menu and the footer on every page from scripts/apps.py.

Usage, from the repo root:

    python3 scripts/sync-nav.py
"""

import re
from pathlib import Path

from apps import APPS

ROOT = Path(__file__).resolve().parent.parent
GRID_ICON = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M4 4h4v4H4zm6 0h4v4h-4zm6 0h4v4h-4zM4 10h4v4H4zm6 0h4v4h-4zm6 0h4v4h-4zM4 16h4v4H4zm6 0h4v4h-4zm6 0h4v4h-4z"/></svg>'
CHEVRON = '<svg class="apps-chevron" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M7 10l5 5 5-5z"/></svg>'


def app_href(slug, page, prefix):
    return './' if page == f'{slug}/index.html' else f'{prefix}{slug}/'


def header(page, prefix):
    links = []
    for slug, name, *_ in APPS:
        current = ' aria-current="page"' if page == f'{slug}/index.html' else ''
        links.append(f'          <a href="{app_href(slug, page, prefix)}"{current}>'
                     f'<img src="{prefix}assets/{slug}-icon.png" alt="" width="32" height="32" loading="lazy">'
                     f'<span>{name}</span></a>')
    return ('<details class="apps-menu">\n'
            f'        <summary>{GRID_ICON}<span>Apps</span>{CHEVRON}</summary>\n'
            '        <nav class="apps-panel" aria-label="Apps">\n'
            + '\n'.join(links) +
            '\n        </nav>\n'
            '      </details>\n'
            f'      <script src="{prefix}assets/site.js" defer></script>')


def footer(page, prefix):
    home = prefix or './'
    apps = '\n'.join(f'            <li><a href="{app_href(slug, page, prefix)}">{name}</a></li>' for slug, name, *_ in APPS)
    privacy = '\n'.join(f'            <li><a href="{url}">{name}</a></li>' for _, name, _, url, _ in APPS)
    return f'''<div class="footer-grid">
        <div class="footer-about">
          <a class="brand" href="{home}"><span class="brand-mark" aria-hidden="true">P</span>Pyush Apps</a>
          <p>Small, private Android apps that work offline. No accounts, no sign-up.</p>
          <p><a href="mailto:androidpyus@gmail.com">androidpyus@gmail.com</a></p>
        </div>
        <nav aria-label="Apps">
          <h2>Apps</h2>
          <ul>
{apps}
          </ul>
        </nav>
        <nav aria-label="Privacy policies">
          <h2>Privacy policies</h2>
          <ul>
{privacy}
          </ul>
        </nav>
      </div>
      <div class="footer-bottom">'''


HEADER = re.compile(r'<nav class="site-nav".*?</nav>'
                    r'|<details class="apps-menu">.*?</details>\s*<script src="[^"]*site\.js" defer></script>', re.S)
FOOTER = re.compile(r'<div class="footer-grid">.*?<div class="footer-bottom">', re.S)

# mathsurge/c/ is a challenge landing page with its own header, so it isn't listed.
for page in ['index.html', *(f'{slug}/index.html' for slug, *_ in APPS)]:
    path = ROOT / page
    prefix = '../' * page.count('/')
    text = path.read_text(encoding='utf-8')
    text, found = HEADER.subn(lambda _: header(page, prefix), text)
    if found != 1:
        raise SystemExit(f'{page}: expected one header menu, found {found}')
    text = FOOTER.sub(lambda _: footer(page, prefix), text)
    path.write_text(text, encoding='utf-8')
    print(page)
