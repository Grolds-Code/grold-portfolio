"""
Generates og-image.png (1200x630) — the picture shown when this site's link
is pasted into LinkedIn, Slack, iMessage, X, etc.

Run once (and again any time SITE fields in content.py change):
    python make_og_image.py

Requires Pillow (already in requirements.txt) and the JetBrains Mono font
files in assets/, which were downloaded from the official JetBrainsMono
GitHub repo (OFL-1.1 licensed, free for this use).
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

import content as c

HERE = Path(__file__).parent
ASSETS = HERE / "assets"

W, H = 1200, 630

BG = (233, 231, 224)       # matches --bg
INK = (27, 27, 25)         # matches --ink
INK_DIM = (102, 101, 95)   # matches --ink-dim
ACCENT = (81, 79, 142)     # matches --accent
MESH_LINE = (27, 27, 25, 18)  # faint, alpha out of 255

regular = ImageFont.truetype(str(ASSETS / "JetBrainsMono-Regular.ttf"), 26)
medium = ImageFont.truetype(str(ASSETS / "JetBrainsMono-Medium.ttf"), 26)
bold_name = ImageFont.truetype(str(ASSETS / "JetBrainsMono-Bold.ttf"), 46)
small = ImageFont.truetype(str(ASSETS / "JetBrainsMono-Regular.ttf"), 22)

img = Image.new("RGB", (W, H), BG)

# --- faint mesh, same coordinate pattern as the site background, scaled to 1200x630 ---
mesh_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
mesh_draw = ImageDraw.Draw(mesh_layer)

def pt(x, y):
    return (x / 100 * W, y / 100 * H)

edges = [
    (8, 12, 24, 6), (24, 6, 38, 20), (38, 20, 50, 12), (50, 12, 62, 24),
    (62, 24, 72, 10), (72, 10, 88, 18), (88, 18, 80, 32), (80, 32, 94, 42),
    (38, 20, 16, 30), (16, 30, 8, 12), (16, 30, 44, 36), (44, 36, 38, 20),
    (44, 36, 62, 24), (44, 36, 56, 46), (62, 24, 80, 32), (80, 32, 56, 46),
    (56, 46, 66, 56), (66, 56, 80, 32), (56, 46, 30, 50), (30, 50, 16, 30),
    (76, 62, 94, 42), (76, 62, 86, 74), (86, 74, 96, 86),
]
for x1, y1, x2, y2 in edges:
    mesh_draw.line([pt(x1, y1), pt(x2, y2)], fill=MESH_LINE, width=2)

img.paste(mesh_layer, (0, 0), mesh_layer)

draw = ImageDraw.Draw(img)

# --- text content ---
left = 90
draw.text((left, 210), c.SITE["name"], font=bold_name, fill=INK)
draw.text((left, 275), c.SITE["role"], font=regular, fill=INK_DIM)

# thesis, wrapped manually to a sensible width
import textwrap
wrapped = textwrap.wrap(c.SITE["thesis"], width=72)
y = 340
for line in wrapped[:3]:
    draw.text((left, y), line, font=small, fill=INK_DIM)
    y += 32

# small accent rule + footer label
draw.line([(left, 560), (left + 60, 560)], fill=ACCENT, width=3)
draw.text((left, 578), c.SITE["location"], font=small, fill=INK_DIM)

out_path = HERE / "og-image.png"
img.save(out_path)
print(f"Wrote {out_path} ({img.size[0]}x{img.size[1]})")
