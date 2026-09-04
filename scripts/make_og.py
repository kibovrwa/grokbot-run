# -*- coding: utf-8 -*-
"""Official-style OG: black field, cream squircle, black slit eyes."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "og.png"
W, H = 1200, 630


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        p = Path(path)
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), (10, 10, 10))
    draw = ImageDraw.Draw(img)

    face = 168
    x0 = (W - face) // 2
    y0 = 132
    draw.rounded_rectangle((x0, y0, x0 + face, y0 + face), radius=52, fill=(246, 244, 239))

    eye_w, eye_h = 16, 46
    gap = 42
    cy = y0 + 70
    lx = x0 + face // 2 - gap // 2 - eye_w
    rx = x0 + face // 2 + gap // 2
    draw.rounded_rectangle((lx, cy, lx + eye_w, cy + eye_h), radius=8, fill=(17, 17, 17))
    draw.rounded_rectangle((rx, cy, rx + eye_w, cy + eye_h), radius=8, fill=(17, 17, 17))

    title = font(54, bold=True)
    sub = font(22)
    t = "Grok Bot"
    tw = draw.textlength(t, font=title)
    draw.text(((W - tw) / 2, y0 + face + 36), t, font=title, fill=(246, 244, 239))
    s = "how to start  ·  grokbot.run"
    sw = draw.textlength(s, font=sub)
    draw.text(((W - sw) / 2, y0 + face + 104), s, font=sub, fill=(120, 120, 118))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
