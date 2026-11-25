# Ultimate Play Studio website

Root of the GitHub Pages site at https://ultimateplaystudio.com/ (repo `pyush.github.io`; the old https://pyush.github.io/ address redirects here). See `DOMAIN-MIGRATION.md` for the move.

## Apps

| App | What it is | Page | Google Play | Privacy policy |
|---|---|---|---|---|
| SurJam | Music studio: 15 instruments, lessons, tuner and recorder | [/surjam/](https://ultimateplaystudio.com/surjam/) | [com.surjam.app](https://play.google.com/store/apps/details?id=com.surjam.app) | [surjam-privacy](https://ultimateplaystudio.com/surjam-privacy/) |
| Hokayantra | Compass and everyday toolkit: level, ruler, expenses, focus and workouts | [/hokayantra/](https://ultimateplaystudio.com/hokayantra/) | [com.hokayantra.app](https://play.google.com/store/apps/details?id=com.hokayantra.app) | [hokayantra-privacy](https://ultimateplaystudio.com/hokayantra-privacy/) |
| MathSurge | Mental math speed trainer with brain games and Vedic tricks | [/mathsurge/](https://ultimateplaystudio.com/mathsurge/) | [com.mathsurge.app](https://play.google.com/store/apps/details?id=com.mathsurge.app) | [mathsurge-privacy](https://ultimateplaystudio.com/mathsurge-privacy/) |
| ScribeVault | Private voice notes with on-device transcription, speaker detection and summaries | [/scribevault/](https://ultimateplaystudio.com/scribevault/) | [com.scribevault.app](https://play.google.com/store/apps/details?id=com.scribevault.app) | [scribevault-privacy](https://ultimateplaystudio.com/scribevault-privacy/) |
| Undercover | Pass-and-play word party game: find the impostor | [/undercover/](https://ultimateplaystudio.com/undercover/) | [com.undercoverimpostor.app](https://play.google.com/store/apps/details?id=com.undercoverimpostor.app) | [undercover-word-imposter-privacy](https://ultimateplaystudio.com/undercover-word-imposter-privacy/) |
| Rasidly | Offline receipt scanner and tax organiser: GST, bills, warranties and documents | [/rasidly/](https://ultimateplaystudio.com/rasidly/) | [com.rasidly.app](https://play.google.com/store/apps/details?id=com.rasidly.app) | [rasidly-privacy](https://ultimateplaystudio.com/rasidly-privacy/) |
| Scanrow | Printed tables and PDFs to editable spreadsheets | [/scanrow/](https://ultimateplaystudio.com/scanrow/) | [com.scanrow.app](https://play.google.com/store/apps/details?id=com.scanrow.app) | [scanrow-site/privacy](https://ultimateplaystudio.com/scanrow-site/privacy/) |
| Kodi Junction | Gujarati cowrie board game, like Chowka Bhara: play the computer, pass and play, or online | [/kodijunction/](https://ultimateplaystudio.com/kodijunction/) | [com.kodijunction.app](https://play.google.com/store/apps/details?id=com.kodijunction.app) | [kodijunction.com](https://kodijunction.com/privacy.html) |
| Blokonia | Classic falling block puzzle: Classic, Daily Challenge, Sprint and Zen modes | [/blokonia/](https://ultimateplaystudio.com/blokonia/) | [com.blokonia.app](https://play.google.com/store/apps/details?id=com.blokonia.app) | [blokonia-site](https://ultimateplaystudio.com/blokonia-site/privacy.html) |
| Snakes & Ladders: Editions | The classic dice board game in five editions: play the computer or pass and play | [/snakesladders/](https://ultimateplaystudio.com/snakesladders/) | [com.snakesladders.editions](https://play.google.com/store/apps/details?id=com.snakesladders.editions) | [snakes-ladders-privacy](https://ultimateplaystudio.com/snakes-ladders-privacy/) |
| Merge Quest: Discovery Puzzle | Relaxing merge puzzle: 64 magical items, patron orders, weekly events | [/mergequest/](https://ultimateplaystudio.com/mergequest/) | [com.mergequest.app](https://play.google.com/store/apps/details?id=com.mergequest.app) | [mergequest-site](https://ultimateplaystudio.com/mergequest-site/privacy.html) |
| BrainBoost: Brain Training | 20 quick brain games for memory, focus, math and logic, with a Daily Workout and Brain Age test | [/brainboost/](https://ultimateplaystudio.com/brainboost/) | [com.brainboost.game](https://play.google.com/store/apps/details?id=com.brainboost.game) | [brainboost-privacy](https://ultimateplaystudio.com/brainboost-privacy/) |

## Files

- `index.html`: home page with a card for each app
- `surjam/`, `hokayantra/`, `mathsurge/`, `scribevault/`, `undercover/`, `rasidly/`, `scanrow/`, `kodijunction/`, `blokonia/`, `snakesladders/`, `mergequest/`, `brainboost/`: app pages (`/surjam/` is the website on SurJam's Play listing)
- `mathsurge/c/`: MathSurge challenge links, with `.well-known/assetlinks.json` so they open in the app
- `scripts/apps.py`: the list of apps that `scripts/sync-nav.py` and `scripts/make-qr.py` read
- `assets/`: shared stylesheet, icons, screenshots and the "scan to install" QR codes (`qr-<app>.svg`, regenerate with `python3 scripts/make-qr.py`; needs `pip install segno`)
- `app-ads.txt`: checked by AdMob for every app in the account
- `scripts/seo_data.py` + `scripts/seo.py`: titles, descriptions, FAQs and structured data for search. Edit the data file, then run `python3 scripts/seo.py` (add `--images` to redraw the 1200×630 share images in `assets/og/`)
- `scripts/social.py`: social profile links and icons, used by the footer (`sync-nav.py`) and the structured data (`seo.py`)
- `robots.txt`, `sitemap.xml` (written by `seo.py`), `404.html`
- `brand/`: logo and Play Console developer-page images

To add an app: add its entry to `scripts/seo_data.py` too, and run `python3 scripts/seo.py --images` after the steps below. To add an app: add a line to `scripts/apps.py` and run `python3 scripts/sync-nav.py`, which rewrites the header's Apps menu and the footer on every page. Then add its card in `index.html` (with `data-tags` naming its filter categories), its own page, and its colours (`--<app>` and `--<app>-2` in `assets/style.css`).

## Adding an app before it's on Google Play

Until an app's Play page is public, use a `btn-soon` span ("Coming soon to Google Play") instead of the `btn-play` link and leave out the `qr` block, so visitors don't hit Play's "not found" page. Once it's live, mark it live in `scripts/apps.py`, run `scripts/make-qr.py`, and switch to the `btn-play` link with the QR block.
