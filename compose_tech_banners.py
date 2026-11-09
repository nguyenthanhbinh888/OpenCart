from PIL import Image, ImageDraw, ImageFont
import os

target_dir = r"C:\Users\Admin\Desktop\opencart\upload\image\catalog\tech"

# 1. Compose Hero Banner (1100x420)
hero_src = os.path.join(target_dir, "banner_hero_phone.jpg")
hero_img = Image.open(hero_src).resize((1100, 420), Image.Resampling.LANCZOS)

# Create dark gradient overlay on left for readable tech typography
overlay = Image.new('RGBA', (1100, 420), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for x in range(700):
    alpha = int(220 * (1 - x / 700))
    draw.line([(x, 0), (x, 420)], fill=(15, 23, 42, alpha))

hero_img.paste(overlay, (0, 0), overlay)
draw_hero = ImageDraw.Draw(hero_img)

# Try fonts
try:
    font_badge = ImageFont.truetype("arialbd.ttf", 15)
    font_h1 = ImageFont.truetype("arialbd.ttf", 40)
    font_sub = ImageFont.truetype("arial.ttf", 18)
    font_btn = ImageFont.truetype("arialbd.ttf", 16)
except:
    font_badge = font_h1 = font_sub = font_btn = ImageFont.load_default()

# Badge "SIÊU PHẨM MỚI 2026"
draw_hero.rectangle([(40, 45), (230, 75)], fill=(215, 0, 24)) # Red badge
draw_hero.text((50, 52), "★ SIÊU PHẨM MỚI 2026", fill=(255, 255, 255), font=font_badge)

# Title
draw_hero.text((40, 90), "IPHONE 16 PRO MAX", fill=(255, 255, 255), font=font_h1)
draw_hero.text((40, 140), "TITANIUM ĐỈNH CAO - CHIP A18 PRO", fill=(245, 158, 11), font=font_h1) # Amber highlight

# Subtitle
draw_hero.text((40, 205), "Màn hình 6.9\" Super Retina XDR 120Hz | Camera 48MP Zoom 5X", fill=(226, 232, 240), font=font_sub)
draw_hero.text((40, 235), "Thu cũ đổi mới trợ giá 2.000.000đ - Trả góp 0% lãi suất", fill=(148, 163, 184), font=font_sub)

# Price Tag
draw_hero.text((40, 280), "Giá chỉ từ: 32.990.000đ", fill=(239, 68, 68), font=font_h1)

# CTA Button
draw_hero.rectangle([(40, 345), (220, 395)], fill=(215, 0, 24))
draw_hero.text((65, 360), "MUA NGAY HÔM NAY", fill=(255, 255, 255), font=font_btn)

hero_img.save(os.path.join(target_dir, "banner_hero_main.jpg"), quality=90)
print("[OK] Created banner_hero_main.jpg")

# 2. Sub Banner 1: MacBook Pro (540x200)
sub1 = Image.open(os.path.join(target_dir, "banner_sub_laptop.jpg")).resize((540, 200), Image.Resampling.LANCZOS)
sub1_over = Image.new('RGBA', (540, 200), (0, 0, 0, 0))
d1 = ImageDraw.Draw(sub1_over)
d1.rectangle([(0, 0), (320, 200)], fill=(10, 15, 30, 200))
sub1.paste(sub1_over, (0, 0), sub1_over)
d_sub1 = ImageDraw.Draw(sub1)
try:
    f_sub_title = ImageFont.truetype("arialbd.ttf", 22)
    f_sub_txt = ImageFont.truetype("arial.ttf", 14)
except:
    f_sub_title = f_sub_txt = ImageFont.load_default()

d_sub1.text((20, 25), "MACBOOK PRO M3", fill=(255, 255, 255), font=f_sub_title)
d_sub1.text((20, 55), "UY LỰC SIÊU PHÀM", fill=(59, 130, 246), font=f_sub_title)
d_sub1.text((20, 95), "Hiệu năng đồ họa đỉnh cao", fill=(203, 213, 225), font=f_sub_txt)
d_sub1.text((20, 120), "Giảm thẳng 3.000.000đ", fill=(239, 68, 68), font=f_sub_title)
d_sub1.text((20, 155), "Xem chi tiết →", fill=(255, 255, 255), font=f_sub_txt)
sub1.save(os.path.join(target_dir, "banner_sub1.jpg"), quality=90)
print("[OK] Created banner_sub1.jpg")

# 3. Sub Banner 2: Audio & Accessories (540x200)
sub2 = Image.open(os.path.join(target_dir, "banner_sub_audio.jpg")).resize((540, 200), Image.Resampling.LANCZOS)
sub2_over = Image.new('RGBA', (540, 200), (0, 0, 0, 0))
d2 = ImageDraw.Draw(sub2_over)
d2.rectangle([(0, 0), (320, 200)], fill=(15, 20, 25, 200))
sub2.paste(sub2_over, (0, 0), sub2_over)
d_sub2 = ImageDraw.Draw(sub2)
d_sub2.text((20, 25), "ÂM THANH HI-RES", fill=(255, 255, 255), font=f_sub_title)
d_sub2.text((20, 55), "SONY & MARSHALL", fill=(245, 158, 11), font=f_sub_title)
d_sub2.text((20, 95), "Chống ồn chủ động ANC", fill=(203, 213, 225), font=f_sub_txt)
d_sub2.text((20, 120), "Ưu đãi đến 35%", fill=(239, 68, 68), font=f_sub_title)
d_sub2.text((20, 155), "Khám phá ngay →", fill=(255, 255, 255), font=f_sub_txt)
sub2.save(os.path.join(target_dir, "banner_sub2.jpg"), quality=90)
print("[OK] Created banner_sub2.jpg")

