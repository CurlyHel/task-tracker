from PIL import Image, ImageDraw

SIZE = 180
img = Image.new('RGBA', (SIZE, SIZE))
draw = ImageDraw.Draw(img)

# Diagonal gradient: indigo (#4f46e5) -> purple (#a855f7) -> pink (#db2777)
c1 = (79, 70, 229)
c2 = (168, 85, 247)
c3 = (219, 39, 119)
for y in range(SIZE):
    for x in range(SIZE):
        t = (x + y) / (2 * (SIZE - 1))
        if t < 0.5:
            f = t / 0.5
            r = int(c1[0] + (c2[0] - c1[0]) * f)
            g = int(c1[1] + (c2[1] - c1[1]) * f)
            b = int(c1[2] + (c2[2] - c1[2]) * f)
        else:
            f = (t - 0.5) / 0.5
            r = int(c2[0] + (c3[0] - c2[0]) * f)
            g = int(c2[1] + (c3[1] - c2[1]) * f)
            b = int(c2[2] + (c3[2] - c2[2]) * f)
        img.putpixel((x, y), (r, g, b, 255))

draw = ImageDraw.Draw(img)

# Bold white tick with rounded ends
tick = [(42, 96), (76, 130), (138, 58)]
draw.line(tick, fill=(255, 255, 255, 255), width=20, joint='curve')
for px, py in (tick[0], tick[2]):
    draw.ellipse([px - 10, py - 10, px + 10, py + 10], fill=(255, 255, 255, 255))

# Sparkle: 4-pointed star, top right
def sparkle(cx, cy, r_long, r_short):
    pts = [
        (cx, cy - r_long), (cx + r_short, cy - r_short),
        (cx + r_long, cy), (cx + r_short, cy + r_short),
        (cx, cy + r_long), (cx - r_short, cy + r_short),
        (cx - r_long, cy), (cx - r_short, cy - r_short),
    ]
    draw.polygon(pts, fill=(255, 255, 255, 235))

sparkle(140, 128, 16, 4)
sparkle(112, 150, 9, 2)

img.save('icon.png')
print('icon.png written', img.size)
