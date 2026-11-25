"""Social profile art for Ultimate Play Studio, drawn from the UP mark in assets/logo.svg.

Usage, from the repo root (needs Pillow and the Ubuntu Sans font):

    python3 brand/make_social_assets.py

Writes to brand/youtube/:
- banner-2560x1440.jpg   channel banner; logo, name and app icons sit inside the
                         1546x423 centre area that every device shows
- profile-800.png        profile picture (opaque; YouTube crops it to a circle)
- watermark-150.png      video watermark (transparent background)

and to brand/social/ (crops of the same banner around its centre block):
- facebook-cover-1640x624.jpg
- x-header-1500x500.jpg
- linkedin-cover-1128x191.jpg
The profile picture (brand/youtube/profile-800.png) suits every platform.
"""

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'brand' / 'youtube'
FONT = '/usr/share/fonts/truetype/ubuntu/UbuntuSans[wdth,wght].ttf'
STOPS = [(0, (0xff, 0x6b, 0x35)), (.5, (0xe8, 0x33, 0x6d)), (1, (0x6c, 0x2b, 0xd9))]
GOLD, WHITE = (0xff, 0xd4, 0x3b), (255, 255, 255)
APPS = ['surjam', 'hokayantra', 'mathsurge', 'scribevault', 'undercover', 'rasidly',
        'scanrow', 'kodijunction', 'blokonia', 'snakesladders', 'mergequest', 'brainboost']


def font(size, weight):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_name(weight)
    return f


def gradient(size):
    small = Image.new('RGB', (256, 256)); px = small.load()
    for y in range(256):
        for x in range(256):
            t = (x + y) / 510
            for (t0, c0), (t1, c1) in zip(STOPS, STOPS[1:]):
                if t <= t1:
                    k = (t - t0) / (t1 - t0)
                    px[x, y] = tuple(round(c0[i] + (c1[i] - c0[i]) * k) for i in range(3))
                    break
    return small.resize((size, size), Image.BICUBIC)


def star(cx, cy, R, r):
    return [(cx + (R if i % 2 == 0 else r) * math.cos(math.radians(-90 + i * 45)),
             cy + (R if i % 2 == 0 else r) * math.sin(math.radians(-90 + i * 45))) for i in range(8)]


def draw_mark(img, ox, oy, s):
    """The UP mark (64-unit grid, as in logo.svg) at (ox, oy), s pixels per unit."""
    d = ImageDraw.Draw(img)
    P = lambda x, y: (ox + x * s, oy + y * s)
    w = 8.5 * s

    def dot(x, y):
        cx, cy = P(x, y); d.ellipse([cx - w / 2, cy - w / 2, cx + w / 2, cy + w / 2], fill=WHITE)

    def line(a, b):
        d.line([P(*a), P(*b)], fill=WHITE, width=round(w)); dot(*a); dot(*b)

    def arc(cx, cy, r, a0, a1):
        x, y = P(cx, cy); R = r * s + w / 2
        d.arc([x - R, y - R, x + R, y + R], a0, a1, fill=WHITE, width=round(w))

    line((14.5, 28), (14.5, 39)); arc(24.5, 39, 10, 0, 180); line((34.5, 12), (34.5, 39))
    line((34.5, 12), (39.5, 12)); line((34.5, 30), (39.5, 30)); arc(39.5, 21, 9, 270, 90)
    d.polygon([P(*q) for q in star(13.5, 15, 6, 1.8)], fill=GOLD)


def rounded_logo(size):
    big = size * 4
    tile = gradient(big).convert('RGBA')
    draw_mark(tile, 0, 0, big / 64)
    mask = Image.new('L', (big, big), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, big - 1, big - 1], radius=big // 4, fill=255)
    tile.putalpha(mask)
    return tile.resize((size, size), Image.LANCZOS)


def profile(size=800, scale=0.80):
    big = size * 3
    img = gradient(big)
    draw_mark(img, big * (1 - scale) / 2, big * (1 - scale) / 2 + big * 0.01, big / 64 * scale)
    return img.resize((size, size), Image.LANCZOS)


def banner():
    W, H = 2560, 1440
    bg = Image.new('RGB', (W // 8, H // 8), (11, 12, 22))
    glow = Image.new('RGB', bg.size); g = ImageDraw.Draw(glow)
    for cx, cy, r, col in [(0.10, 0.15, 0.28, (255, 107, 53)), (0.90, 0.85, 0.34, (108, 43, 217)),
                           (0.50, 0.42, 0.24, (232, 51, 109)), (0.12, 0.92, 0.22, (60, 40, 160))]:
        x, y, R = cx * bg.width, cy * bg.height, r * bg.width
        g.ellipse([x - R, y - R, x + R, y + R], fill=col)
    glow = glow.filter(ImageFilter.GaussianBlur(bg.width * 0.10))
    img = Image.blend(bg, glow, 0.32).resize((W, H), Image.BICUBIC).convert('RGBA')

    # Sparkles outside the centre area (they only show on wide screens and TVs)
    random.seed(11)
    safe = (507, 508, 2053, 931)
    for _ in range(46):
        x, y = random.uniform(0.03, 0.97) * W, random.uniform(0.04, 0.96) * H
        if safe[0] - 60 < x < safe[2] + 60 and safe[1] - 60 < y < safe[3] + 60:
            continue
        R = random.uniform(10, 34)
        col = GOLD if random.random() < 0.35 else WHITE
        layer = Image.new('RGBA', (W, H))
        ImageDraw.Draw(layer).polygon(star(x, y, R, R * 0.28), fill=(*col, random.randint(70, 170)))
        img.alpha_composite(layer)

    # Centre block: logo on the left, name, line and app icons on the right
    logo_size, gap = 250, 48
    title, sub = font(116, 'ExtraBold'), font(46, 'Medium')
    d = ImageDraw.Draw(img)
    name, line = 'Ultimate Play Studio', 'Apps and games for everyday play'
    text_w = max(d.textlength(name, font=title), d.textlength(line, font=sub))
    icon, icon_gap = 56, 12
    icons_w = len(APPS) * icon + (len(APPS) - 1) * icon_gap
    block_w = logo_size + gap + max(text_w, icons_w)
    x0 = (W - block_w) / 2
    y_mid = H / 2
    assert x0 >= safe[0] and x0 + block_w <= safe[2], 'centre block is wider than the safe area'

    shadow = Image.new('RGBA', (W, H))
    ImageDraw.Draw(shadow).rounded_rectangle([x0, y_mid - logo_size / 2 + 26, x0 + logo_size, y_mid + logo_size / 2 + 26],
                                             radius=62, fill=(0, 0, 0, 150))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(36)))
    img.alpha_composite(rounded_logo(logo_size), (int(x0), int(y_mid - logo_size / 2)))

    tx = x0 + logo_size + gap
    d.text((tx, y_mid - 150), name, font=title, fill=WHITE)
    d.text((tx + 4, y_mid - 4), line, font=sub, fill=(205, 208, 224))
    iy = y_mid + 70
    for i, slug in enumerate(APPS):
        ic = Image.open(ROOT / f'assets/{slug}-icon.png').convert('RGBA').resize((icon * 3, icon * 3), Image.LANCZOS)
        m = Image.new('L', ic.size, 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, ic.width - 1, ic.height - 1], radius=ic.width * 0.23, fill=255)
        a = Image.new('L', ic.size, 0); a.paste(ic.getchannel('A'), (0, 0), m); ic.putalpha(a)
        img.alpha_composite(ic.resize((icon, icon), Image.LANCZOS), (int(tx + 6 + i * (icon + icon_gap)), int(iy)))
    assert iy + icon <= safe[3] and y_mid - 150 >= safe[1], 'centre block is taller than the safe area'
    return img.convert('RGB')


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    b = banner()
    b.save(OUT / 'banner-2560x1440.jpg', quality=92, optimize=True, progressive=True)
    profile().save(OUT / 'profile-800.png', optimize=True)
    rounded_logo(150).save(OUT / 'watermark-150.png', optimize=True)
    social = ROOT / 'brand' / 'social'
    social.mkdir(exist_ok=True)
    cx, cy = 1280, 720
    for name, (w, h), crop_w in [('facebook-cover-1640x624.jpg', (1640, 624), 1800),
                                 ('x-header-1500x500.jpg', (1500, 500), 1800),
                                 ('linkedin-cover-1128x191.jpg', (1128, 191), 2400)]:
        crop_h = round(crop_w * h / w)
        box = (cx - crop_w // 2, cy - crop_h // 2, cx + crop_w // 2, cy + crop_h // 2)
        b.crop(box).resize((w, h), Image.LANCZOS).save(social / name, quality=92, optimize=True)
        print(f'brand/social/{name}')
    for f in sorted(OUT.iterdir()):
        print(f.relative_to(ROOT), f'{f.stat().st_size // 1024} KB')
