# Render apple-touch-icon / PWA icons: cinnabar seal with 墨 on rice paper.
import random
from PIL import Image, ImageDraw, ImageFont
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
def icon(n):
    im = Image.new("RGB", (n, n), (241, 235, 221))
    d = ImageDraw.Draw(im)
    random.seed(7)
    for _ in range(n * 2):
        x, y = random.random() * n, random.random() * n
        d.point((x, y), fill=(222, 212, 190))
    m = n * 0.16
    d.rounded_rectangle((m, m, n - m, n - m), radius=n * 0.03, fill=(178, 32, 26))
    f = ImageFont.truetype(FONT, int(n * 0.52), index=1)
    d.text((n / 2, n / 2 + n * 0.01), "墨", font=f, fill=(246, 233, 226), anchor="mm")
    return im
for n, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    icon(n).save(name)
