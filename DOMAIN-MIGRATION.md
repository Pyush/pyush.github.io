# Move to ultimateplaystudio.com

Checklist for rebranding "Pyush Apps" as Ultimate Play Studio and moving the site from `pyush.github.io` to `ultimateplaystudio.com`. `pyush.github.io` keeps working: once the custom domain is set, GitHub redirects every old URL (301) to the same path on the new domain.

Work through the phases in order. Tick each box as you go.

**How to undo:** in repo Settings → Pages, clear the custom domain. `pyush.github.io` starts serving again within minutes.

---

## What uses the old domain today

| Where | What | Effect of the switch |
|---|---|---|
| This repo | 194 absolute links: footers on every page (privacy links), `apps.json` icon URLs, `scripts/apps.py`, `README.md` | Still work through the redirect. Update them for cleanliness |
| 13 project Pages sites (`*-privacy`, `*-site`, `snakes-ladders-sites`, plus 2 old demos) | Served at `pyush.github.io/<repo>/` | Move to `ultimateplaystudio.com/<repo>/` automatically, and old URLs redirect |
| `kodi-junction-site` | Has its own domain, `kodijunction.com` | **Not affected** |
| Play Console (12 apps) | Privacy policy URL, website, developer website | Still work through the redirect. Update them later |
| `app-ads.txt` | AdMob crawls the developer website | One redirect to another domain is allowed. Update the developer website to be safe |
| MathSurge challenge links | `.well-known/assetlinks.json`, the manifest host `pyush.github.io`, `challenge_link.dart` | **Opening links in the app stops working** (Android won't verify through a redirect) until a MathSurge update adds the new host. The links still open in the browser |
| "More apps" feed | BrainBoost, MathSurge, Undercover and MergeQuest fetch `https://pyush.github.io/apps.json` | `HttpClient` follows redirects, so it keeps working. Update in each app's next release |
| Legal links in apps | ScribeVault, BrainBoost, MathSurge, Undercover, Snakes & Ladders, Blokonia (Tetris-Block-Blast) | Keep working. Update in each app's next release |
| Google Cloud OAuth consent screen (Play Games sign-in, BrainBoost) | Home page / privacy URLs, authorised domains | Check and update (Phase 7) |

---

## Phase 0: Decisions (before touching anything)

- [x] Brand name as shown on the site: **Ultimate Play Studio**
- [x] Logo / brand mark: **"UP" monogram**: a U whose right stem rises into a P, with a gold sparkle, on a coral → pink → purple tile (`assets/logo.svg`, `logo-512.png`, `apple-touch-icon.png`, `og-image.png`). `logo-512.png` can also be used for the Play Console developer page and social profiles
- [x] Main address: `ultimateplaystudio.com`, with `www.` redirecting to it
- [x] Contact email: **keep the current address for now** (move to the new domain later)
- [x] Play Console developer name: rename to **Ultimate Play Studio** (the terms now name it as the developer)

## Phase 1: Prepare without going live (no visitor impact)

- [x] Branch `rebrand` in this repo:
  - [x] Brand name, logo and `<title>` in `index.html` and every app page header/footer (via `scripts/sync-nav.py`)
  - [x] Replace `https://pyush.github.io/` with `https://ultimateplaystudio.com/` in all pages, `apps.json`, `scripts/apps.py` and `README.md`
  - [x] Add a favicon, `<link rel="canonical">` and Open Graph tags (`og:url`, `og:image`) on every page
  - [x] Add `robots.txt`, `sitemap.xml` and a branded `404.html`
  - [x] Keep `app-ads.txt` and `.well-known/assetlinks.json` unchanged
  - [x] The "Open in app" button on `mathsurge/c/` still uses `intent://pyush.github.io/...` on purpose: installed MathSurge versions only handle that host, so challenges still open in the app after the switch. Change it once the MathSurge update (Phase 8) is widely installed
  - [x] Merged after the custom domain went live
- [x] QR codes: they point to Play Store links, so they don't need regenerating (only regenerate if the design changes)

## Phase 2: DNS (at the registrar)

- [x] Delete any parking / default `A`, `AAAA` or `CNAME` records on `@` and `www`
- [x] `A` on `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- [x] `AAAA` on `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
- [x] `CNAME` on `www` → `pyush.github.io`
- [x] **Do not** use a wildcard `*` record (that allows takeover)
- [x] GitHub → profile Settings → Pages → **Add a verified domain** → add the `TXT` record it gives you → Verify
- [x] Turn on **auto-renew** and **registrar lock** for the domain. If the domain ever expires, the old `pyush.github.io` URLs break too
- [x] Wait for DNS, then check: `dig +short ultimateplaystudio.com` shows the four GitHub IPs, and `dig +short www.ultimateplaystudio.com` shows `pyush.github.io.`

## Phase 3: Switch (about 5 minutes, best at a quiet time)

- [x] Repo `pyush/pyush.github.io` → Settings → Pages → Custom domain: `ultimateplaystudio.com` → Save (GitHub commits a `CNAME` file; pull it locally)
- [x] Wait for the DNS check ✅ and the certificate (up to about an hour)
- [x] Tick **Enforce HTTPS**

## Phase 4: Check that it works

- [x] `https://ultimateplaystudio.com/` and `https://www.ultimateplaystudio.com/` load over HTTPS
- [x] `https://pyush.github.io/` → 301 to the new domain
- [x] Each app page `/surjam/` … `/brainboost/` loads on both domains (the old one redirects)
- [x] Every Play Console privacy URL, on its **old** address, redirects and loads (the 11 `pyush.github.io/...-privacy` / `-site` URLs)
- [x] `https://kodijunction.com/` unchanged
- [x] `https://ultimateplaystudio.com/app-ads.txt` and `/.well-known/assetlinks.json` return 200 with the right content
- [x] `https://ultimateplaystudio.com/apps.json` returns 200
- [x] "More apps" still loads in an installed BrainBoost / MathSurge (clear the cache or wait for the daily refresh)

Quick check for any URL: `curl -sIL <url> | grep -iE '^(HTTP|location)'`

## Phase 5: Go live with the rebrand

- [x] Merge the `rebrand` branch (rebase it on the `CNAME` commit first)
- [x] Repeat the Phase 4 checks on the rebranded pages
- [x] Sibling repos: links moved to ultimateplaystudio.com in all 10 privacy/site repos; "More apps" disclosures say "ultimateplaystudio.com (formerly pyush.github.io)"; developer named Ultimate Play Studio in the MathSurge, Undercover and BrainBoost terms. `kodi-junction-site` and `blokonia-site` / `scribevault-privacy` had no old links

## Phase 6: Play Console and AdMob (for each of the 12 apps)

| App | Developer website | Privacy policy URL | Store listing website |
|---|---|---|---|
| SurJam | [ ] | [ ] | [ ] |
| Hokayantra | [ ] | [ ] | [ ] |
| MathSurge | [ ] | [ ] | [ ] |
| ScribeVault | [ ] | [ ] | [ ] |
| Undercover | [ ] | [ ] | [ ] |
| Rasidly | [ ] | [ ] | [ ] |
| Scanrow | [ ] | [ ] | [ ] |
| Kodi Junction | [ ] | n/a (kodijunction.com) | [ ] |
| Blokonia | [ ] | [ ] | [ ] |
| Snakes & Ladders | [ ] | [ ] | [ ] |
| Merge Quest | [ ] | [ ] | [ ] |
| BrainBoost | [ ] | [ ] | [ ] |

- [ ] Developer website: `https://ultimateplaystudio.com` (account level, Play Console → Developer page / account details)
- [ ] Privacy policy URLs: the new address (e.g. `https://ultimateplaystudio.com/surjam-privacy/`)
- [x] Contact email: unchanged for now (`androidpyus@gmail.com`)
- [ ] AdMob → Apps → app-ads.txt: run "Check for updates" and confirm it shows **Verified** for every app (it can take up to 24 hours)

## Phase 7: Other Google services

- [ ] Google Cloud console → OAuth consent screen (projects used for Play Games / Firebase): application home page, privacy policy URL and authorised domains
- [ ] Firebase → Authentication → Authorised domains (if any app uses web sign-in)
- [x] Google Search Console: **Domain** property for `ultimateplaystudio.com` verified by DNS `TXT`; `sitemap.xml` submitted (Success, 13 pages, 25 Nov 2026). No Change of address: `pyush.github.io` can no longer be verified because it redirects, and its 301s are enough
- [ ] Search Console: URL inspection → **Request indexing** for the home page and the main app pages (about 10 a day)
- [ ] Bing Webmaster Tools: sign in, **Import from Google Search Console** (also covers DuckDuckGo and Yahoo)

## Phase 8: App updates (put them in each app's next release, no need for a special one)

- [ ] **MathSurge** (most important):
  - [x] `AndroidManifest.xml`: verified `intent-filter` for `ultimateplaystudio.com`; `pyush.github.io` kept in a separate non-autoVerify filter (branch `ultimateplaystudio-domain`)
  - [x] `lib/models/challenge_link.dart`: build new links on the new domain; **accept both** hosts when parsing, so links people already shared still work
  - [x] `test/challenge_link_test.dart`: tests for both hosts
  - [x] MathSurge 1.2.5 (build 11) built and committed (`dc4a76c`)
  - [x] Uploaded to production with `play_store_assets/tools/play_release_upload.py --apply` (25 Nov 2026), in review
  - [ ] After release, check: `adb shell pm get-app-links com.mathsurge.app` shows the new domain as `verified`
- [ ] "More apps" feed URL to `https://ultimateplaystudio.com/apps.json`: BrainBoost, MathSurge, Undercover, MergeQuest (and their tests)
- [ ] Legal / privacy links: ScribeVault, BrainBoost, MathSurge, Undercover, Snakes & Ladders, Blokonia (`Tetris-Block-Blast/lib/core/constants/app_constants.dart`)
- [ ] Store-listing and README docs in each app repo

## Phase 9: Outside channels

- [ ] Social profiles, email signature, any printed QR codes or flyers that show the old site URL
- [ ] Kodi Junction site footer: link to the studio site

## Ongoing (don't break it later)

- Never delete the `CNAME` file or the `A` records while `pyush.github.io` links are still out there
- Keep the domain on auto-renew
- New apps: use `https://ultimateplaystudio.com/...` URLs from the start
