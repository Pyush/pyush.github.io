"""Regenerate the "scan to install" QR codes in assets/ (one per app).

Usage, from the repo root, with segno installed (pip install segno):

    python3 scripts/make-qr.py

Each code opens the app's Google Play page. The referrer marks these
installs as coming from this website in Play Console's acquisition reports.
"""

from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parent.parent
APPS = {
    'surjam': 'com.surjam.app',
    'hokayantra': 'com.hokayantra.app',
    'mathsurge': 'com.mathsurge.app',
}

for name, package in APPS.items():
    url = (f'https://play.google.com/store/apps/details?id={package}'
           '&referrer=utm_source%3Dpyush.github.io%26utm_medium%3Dqr')
    qr = segno.make(url, error='m')
    # Dark modules on a white quiet zone, so phones read it in dark mode too.
    qr.save(ROOT / 'assets' / f'qr-{name}.svg', scale=4, border=3,
            dark='#17161f', light='#ffffff', xmldecl=False, svgns=True,
            title=f'QR code: get {name} on Google Play')
    print(f'assets/qr-{name}.svg -> {url}')
