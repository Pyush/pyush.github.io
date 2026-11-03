# pyush.github.io

Root of the GitHub Pages site at https://pyush.github.io/

## Apps

| App | What it is | Page | Google Play | Privacy policy |
|---|---|---|---|---|
| SurJam | Music studio: 15 instruments, lessons, tuner and recorder | [/surjam/](https://pyush.github.io/surjam/) | [com.surjam.app](https://play.google.com/store/apps/details?id=com.surjam.app) | [surjam-privacy](https://pyush.github.io/surjam-privacy/) |
| Hokayantra | Compass and everyday toolkit: level, ruler, expenses, focus and workouts | [/hokayantra/](https://pyush.github.io/hokayantra/) | [com.hokayantra.app](https://play.google.com/store/apps/details?id=com.hokayantra.app) | [hokayantra-privacy](https://pyush.github.io/hokayantra-privacy/) |
| MathSurge | Mental math speed trainer with brain games and Vedic tricks | [/mathsurge/](https://pyush.github.io/mathsurge/) | [com.mathsurge.app](https://play.google.com/store/apps/details?id=com.mathsurge.app) | [mathsurge-privacy](https://pyush.github.io/mathsurge-privacy/) |
| ScribeVault | Private voice notes with on-device transcription, speaker detection and summaries | [/scribevault/](https://pyush.github.io/scribevault/) | [com.scribevault.app](https://play.google.com/store/apps/details?id=com.scribevault.app) | [scribevault-privacy](https://pyush.github.io/scribevault-privacy/) |
| Undercover | Pass-and-play word party game: find the impostor | [/undercover/](https://pyush.github.io/undercover/) | [com.undercoverimpostor.app](https://play.google.com/store/apps/details?id=com.undercoverimpostor.app) | [undercover-word-imposter-privacy](https://pyush.github.io/undercover-word-imposter-privacy/) |
| Rasidly | Offline receipt scanner and tax organiser: GST, bills, warranties and documents | [/rasidly/](https://pyush.github.io/rasidly/) | [com.rasidly.app](https://play.google.com/store/apps/details?id=com.rasidly.app) | [rasidly-privacy](https://pyush.github.io/rasidly-privacy/) |
| Scanrow | Printed tables and PDFs to editable spreadsheets (coming soon to Play) | [/scanrow/](https://pyush.github.io/scanrow/) | [com.scanrow.app](https://play.google.com/store/apps/details?id=com.scanrow.app) | [scanrow-site/privacy](https://pyush.github.io/scanrow-site/privacy/) |

## Files

- `index.html`: home page with a card for each app
- `surjam/`, `hokayantra/`, `mathsurge/`, `scribevault/`, `undercover/`, `rasidly/`, `scanrow/`: app pages (`/surjam/` is the website on SurJam's Play listing)
- `mathsurge/c/`: MathSurge challenge links, with `.well-known/assetlinks.json` so they open in the app
- `scripts/apps.py`: the list of apps that `scripts/sync-nav.py` and `scripts/make-qr.py` read
- `assets/`: shared stylesheet, icons, screenshots and the "scan to install" QR codes (`qr-<app>.svg`, regenerate with `python3 scripts/make-qr.py`; needs `pip install segno`)
- `app-ads.txt`: checked by AdMob for every app in the account

To add an app: add a line to `scripts/apps.py` and run `python3 scripts/sync-nav.py`, which rewrites the header's Apps menu and the footer on every page. Then add its card in `index.html` (with `data-tags` naming its filter categories), its own page, and its colours (`--<app>` and `--<app>-2` in `assets/style.css`).

## Adding an app before it's on Google Play

Until an app's Play page is public, use a `btn-soon` span ("Coming soon to Google Play") instead of the `btn-play` link and leave out the `qr` block, so visitors don't hit Play's "not found" page. Once it's live, mark it live in `scripts/apps.py`, run `scripts/make-qr.py`, and switch to the `btn-play` link with the QR block.
