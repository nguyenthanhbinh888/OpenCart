from PIL import Image, ImageDraw, ImageFont
import os

target_dir = r"C:\Users\Admin\Desktop\opencart\upload\image\catalog\tech"
img = Image.new('RGBA', (360, 60), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 30)
    font_sub = ImageFont.truetype("arialbd.ttf", 11)
except:
    font_bold = font_sub = ImageFont.load_default()

# Icon badge (Square red box with lightning/power)
draw.rounded_rectangle([(0, 5), (50, 55)], radius=10, fill=(215, 0, 24))
draw.polygon([(28, 12), (18, 32), (26, 32), (22, 48), (34, 28), (26, 28)], fill=(255, 255, 255)) # Lightning

# Brand Name
draw.text((60, 6), "TECH", fill=(30, 41, 59), font=font_bold)
draw.text((150, 6), "ZONE", fill=(215, 0, 24), font=font_bold)
draw.text((245, 14), ".VN", fill=(100, 116, 139), font=font_sub)

# Tagline
draw.text((62, 38), "SIÊU THỊ ĐIỆN TỬ & CÔNG NGHỆ CHÍNH HÃNG", fill=(100, 116, 139), font=font_sub)

img.save(os.path.join(target_dir, "tech_logo.png"))
print("[OK] Created tech_logo.png")

