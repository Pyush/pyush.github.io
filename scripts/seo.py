"""Search and sharing tags for the home page and every app page, from scripts/seo_data.py.

Usage, from the repo root (safe to run again after any edit):

    python3 scripts/seo.py            # pages + sitemap
    python3 scripts/seo.py --images   # also redraw the share images in assets/og/ (needs Pillow)

On each page it writes the <title>, meta description, canonical URL, Open Graph and Twitter tags
and JSON-LD structured data between <!-- seo --> markers in <head>. On app pages it also writes a
breadcrumb and a "Questions and answers" section between their own markers, and lazy-loads
screenshots below the first. It regenerates sitemap.xml with today's date.
"""

import datetime
import html
import json
import re
import sys
from pathlib import Path

from apps import APPS as APP_LIST
from seo_data import APPS, BRAND, EMAIL, HOME, SITE

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.date.today().isoformat()
ORG = {'@type': 'Organization', '@id': SITE + '#organization', 'name': BRAND, 'url': SITE,
       'logo': SITE + 'assets/logo-512.png', 'email': EMAIL}


def esc(s):
    return html.escape(s, quote=True)


def ld(data):
    text = json.dumps(data, ensure_ascii=False, indent=2).replace('</', '<\\/')
    return f'  <script type="application/ld+json">\n{text}\n  </script>\n'


def head_block(url, title, desc, image, large, graph, prefix):
    return ('  <!-- seo -->\n'
            f'  <link rel="canonical" href="{url}">\n'
            f'  <meta name="theme-color" content="#f7f6fb" media="(prefers-color-scheme: light)">\n'
            f'  <meta name="theme-color" content="#0f0e17" media="(prefers-color-scheme: dark)">\n'
            f'  <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">\n'
            f'  <meta property="og:type" content="website">\n'
            f'  <meta property="og:site_name" content="{BRAND}">\n'
            f'  <meta property="og:locale" content="en_US">\n'
            f'  <meta property="og:title" content="{esc(title)}">\n'
            f'  <meta property="og:description" content="{esc(desc)}">\n'
            f'  <meta property="og:url" content="{url}">\n'
            f'  <meta property="og:image" content="{image}">\n'
            f'  <meta property="og:image:width" content="1200">\n'
            f'  <meta property="og:image:height" content="630">\n'
            f'  <meta name="twitter:card" content="{"summary_large_image" if large else "summary"}">\n'
            + ld({'@context': 'https://schema.org', '@graph': graph}) +
            '  <!-- /seo -->\n')


def set_head(text, block, title, desc):
    text = re.sub(r'<title>.*?</title>', f'<title>{esc(title)}</title>', text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', text, count=1)
    if '<!-- seo -->' in text:
        return re.sub(r'  <!-- seo -->\n.*?  <!-- /seo -->\n', lambda _: block, text, count=1, flags=re.S)
    # First run: drop the earlier one-off tags, then insert the block before the stylesheet.
    text = re.sub(r'  <(link rel="(canonical|apple-touch-icon)"|meta (property="og:|name="twitter:|name="theme-color"))[^>]*>\n', '', text)
    return text.replace('  <link rel="stylesheet"', block + '  <link rel="stylesheet"', 1)


def put_marked(text, name, content, anchor, before=True):
    """Replace <!-- seo:name --> ... <!-- /seo:name -->, or insert it next to `anchor` the first time."""
    block = f'<!-- seo:{name} -->\n{content}\n    <!-- /seo:{name} -->'
    pat = re.compile(rf'<!-- seo:{name} -->.*?<!-- /seo:{name} -->', re.S)
    if pat.search(text):
        return pat.sub(lambda _: block, text, count=1)
    if anchor not in text:
        raise SystemExit(f'anchor for {name} not found: {anchor!r}')
    return text.replace(anchor, (block + '\n    ' + anchor) if before else (anchor + '\n    ' + block), 1)


def lazy_images(text, skip_first):
    """Lazy-load screenshot and QR images. Keeps the first screenshot eager on app pages."""
    seen = 0

    def fix(m):
        nonlocal seen
        tag = m.group(0)
        if 'loading=' in tag:
            return tag
        if 'webp' in tag:
            seen += 1
            if skip_first and seen == 1:
                return tag
        return tag[:-1] + ' loading="lazy" decoding="async">'

    return re.sub(r'<img [^>]*(?:\.webp|qr-[a-z]+\.svg)"[^>]*>', fix, text)


def app_page(slug, d):
    path = ROOT / slug / 'index.html'
    text = path.read_text(encoding='utf-8')
    url = f'{SITE}{slug}/'
    name = html.unescape(re.search(r'<h1>(.*?)</h1>', text).group(1))
    play = re.search(r'class="btn btn-play" href="([^"]+)"', text).group(1)
    shots = [SITE + 'assets/' + s for s in re.findall(r'src="\.\./assets/([a-z]+-\d\.webp)"', text)]
    app = {'@type': 'MobileApplication', '@id': url + '#app', 'name': name, 'url': url,
           'description': d['description'], 'operatingSystem': 'Android',
           'applicationCategory': d['category'], 'genre': d['genre'],
           'image': f'{SITE}assets/{slug}-icon.png', 'screenshot': shots,
           'installUrl': play, 'sameAs': [play],
           'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'},
           'publisher': {'@id': SITE + '#organization'}, 'author': {'@id': SITE + '#organization'}}
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': url}]}
    faq = {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in d['faq']]}
    block = head_block(url, d['title'], d['description'], f'{SITE}assets/og/{slug}.png', True,
                       [ORG, app, crumbs, faq], '../')
    text = set_head(text, block, d['title'], d['description'])

    crumb_html = ('    <nav class="breadcrumb" aria-label="Breadcrumb">\n'
                  '      <ol><li><a href="../">Home</a></li>'
                  f'<li><span aria-current="page">{esc(name)}</span></li></ol>\n'
                  '    </nav>')
    text = put_marked(text, 'breadcrumb', crumb_html, '<section class="app-hero">')

    items = '\n'.join(f'        <details>\n          <summary>{esc(q)}</summary>\n          <p>{esc(a)}</p>\n        </details>'
                      for q, a in d['faq'])
    faq_html = (f'    <section class="section" aria-labelledby="faq-title">\n'
                f'      <h2 id="faq-title">{esc(name.split(":")[0])}: questions and answers</h2>\n'
                f'      <div class="faq">\n{items}\n      </div>\n'
                f'    </section>')
    # Before the Privacy section, which every app page ends with.
    anchor = re.search(r'<section class="section">\s*<h2>Privacy</h2>', text).group(0)
    text = put_marked(text, 'faq', faq_html, anchor)
    text = lazy_images(text, skip_first=True)
    path.write_text(text, encoding='utf-8')
    return name


def home_page(names):
    path = ROOT / 'index.html'
    text = path.read_text(encoding='utf-8')
    site = {'@type': 'WebSite', '@id': SITE + '#website', 'name': BRAND, 'url': SITE,
            'publisher': {'@id': SITE + '#organization'}}
    items = {'@type': 'ItemList', 'name': f'Apps and games by {BRAND}', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE}{slug}/', 'name': names[slug]}
        for i, (slug, *_) in enumerate(APP_LIST)]}
    block = head_block(SITE, HOME['title'], HOME['description'], SITE + 'assets/og-image.png', True,
                       [ORG, site, items], '')
    text = set_head(text, block, HOME['title'], HOME['description'])
    text = lazy_images(text, skip_first=False)
    path.write_text(text, encoding='utf-8')


def sitemap():
    urls = [SITE] + [f'{SITE}{slug}/' for slug, *_ in APP_LIST]
    body = '\n'.join(f'  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>' for u in urls)
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
                                      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      f'{body}\n</urlset>\n', encoding='utf-8')


def share_images(names):
    from PIL import Image, ImageDraw, ImageFont
    css = (ROOT / 'assets/style.css').read_text()
    light = css[:css.index('@media')]
    font_path = '/usr/share/fonts/truetype/ubuntu/UbuntuSans[wdth,wght].ttf'

    def font(size, weight):
        f = ImageFont.truetype(font_path, size); f.set_variation_by_name(weight); return f

    def color(var):
        h = re.search(rf'--{var}:\s*#([0-9a-f]{{6}})', light).group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    def rounded(im, r):
        m = Image.new('L', im.size, 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=r, fill=255)
        im = im.convert('RGBA'); im.putalpha(m); return im

    out = ROOT / 'assets/og'; out.mkdir(exist_ok=True)
    logo = Image.open(ROOT / 'assets/logo-512.png').convert('RGBA').resize((44, 44), Image.LANCZOS)
    for slug, *_ in APP_LIST:
        c1, c2 = color(slug), color(f'{slug}-2')
        small = Image.new('RGB', (120, 63)); px = small.load()
        for y in range(63):
            for x in range(120):
                t = (x / 119) * 0.75 + (y / 62) * 0.25
                px[x, y] = tuple(round(c1[i] * (1 - t) * 0.82 + c2[i] * t * 0.82) for i in range(3))
        img = small.resize((1200, 630), Image.BICUBIC).convert('RGBA')
        d = ImageDraw.Draw(img)
        icon = rounded(Image.open(ROOT / f'assets/{slug}-icon.png').resize((150, 150), Image.LANCZOS), 36)
        img.alpha_composite(icon, (72, 84))
        # Name, wrapped to the text column
        title_font, y = font(66, 'ExtraBold'), 270
        words, lines, line = names[slug].split(), [], ''
        for w in words:
            trial = (line + ' ' + w).strip()
            if d.textlength(trial, font=title_font) > 600 and line:
                lines.append(line); line = w
            else:
                line = trial
        lines.append(line)
        for ln in lines[:2]:
            d.text((72, y), ln, font=title_font, fill='white'); y += 78
        sub = font(32, 'Medium'); words, line, sublines = APPS[slug]['share'].split(), '', []
        for w in words:
            trial = (line + ' ' + w).strip()
            if d.textlength(trial, font=sub) > 600 and line:
                sublines.append(line); line = w
            else:
                line = trial
        sublines.append(line)
        for ln in sublines:
            d.text((72, y + 10), ln, font=sub, fill=(255, 255, 255, 225)); y += 42
        img.alpha_composite(logo, (72, 540))
        d.text((128, 548), 'ultimateplaystudio.com', font=font(26, 'Medium'), fill=(255, 255, 255, 230))
        # Two screenshots on the right, running off the bottom edge
        for i, (x, top) in enumerate([(760, 90), (980, 150)]):
            shot = Image.open(ROOT / f'assets/{slug}-{i + 1}.webp').convert('RGB').resize((200, 400), Image.LANCZOS)
            frame = Image.new('RGB', (212, 412), (15, 14, 23)); frame.paste(shot, (6, 6))
            frame = rounded(frame, 28)
            shadow = Image.new('RGBA', img.size)
            ImageDraw.Draw(shadow).rounded_rectangle([x + 8, top + 16, x + 220, top + 428], radius=28, fill=(0, 0, 0, 90))
            from PIL import ImageFilter
            img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(14)))
            img.alpha_composite(frame, (x, top))
        img.convert('RGB').save(out / f'{slug}.png', optimize=True)
        print('assets/og/' + slug + '.png')


if __name__ == '__main__':
    names = {}
    for slug, *_ in APP_LIST:
        names[slug] = app_page(slug, APPS[slug])
        print(f'{slug}/index.html')
    home_page(names)
    print('index.html')
    sitemap()
    print('sitemap.xml')
    if '--images' in sys.argv:
        share_images(names)
