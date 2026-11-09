import urllib.request
import os

images = {
    "iphone16_pro.jpg": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop&q=80", # iPhone titanium
    "samsung_ultra.jpg": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=600&auto=format&fit=crop&q=80", # Samsung galaxy
    "macbook_m3.jpg": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=80", # MacBook Pro
    "laptop_gaming.jpg": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80", # Gaming laptop
    "ipad_pro.jpg": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&auto=format&fit=crop&q=80", # iPad
    "sony_headphones.jpg": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&auto=format&fit=crop&q=80", # Sony / High-end Headphones
    "smartwatch.jpg": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop&q=80", # Apple Watch
    "mouse_keyboard.jpg": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&auto=format&fit=crop&q=80", # Gaming Mouse Logitech
    "banner_hero_phone.jpg": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200&auto=format&fit=crop&q=80", # Cyberpunk / Tech hardware hero
    "banner_sub_laptop.jpg": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&auto=format&fit=crop&q=80", # Laptop tech banner
    "banner_sub_audio.jpg": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80"  # Audio gear banner
}

target_dir = r"C:\Users\Admin\Desktop\opencart\upload\image\catalog\tech"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
for filename, url in images.items():
    dest = os.path.join(target_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(dest, 'wb') as out_file:
            out_file.write(resp.read())
        print(f"[OK] Downloaded {filename} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"[FAIL] {filename}: {e}")

