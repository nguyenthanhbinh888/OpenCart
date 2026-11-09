import subprocess

php_exe = r"C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.2_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe"
code = """
$mysqli = new mysqli('localhost', 'root', '123456', 'opencart', 3306);
if ($mysqli->connect_error) {
    die('Connect error: ' . $mysqli->connect_error);
}
$mysqli->set_charset('utf8mb4');

echo "Updating store configuration...\n";
// Update store name and title
$mysqli->query("UPDATE oc_setting SET value = 'TECHZONE - Siêu Thị Điện Tử & Công Nghệ' WHERE oc_setting.key = 'config_name'");
$mysqli->query("UPDATE oc_setting SET value = 'TECHZONE - Điện Thoại, Laptop, Phụ Kiện Chính Hãng' WHERE oc_setting.key = 'config_meta_title'");

// Update Categories
$categories = [
    [101, 'Điện Thoại & Tablet', 'Top điện thoại iPhone, Samsung, Xiaomi chính hãng giá tốt nhất'],
    [102, 'Laptop & Máy Tính', 'Laptop văn phòng, đồ họa, MacBook, Laptop Gaming cao cấp'],
    [103, 'Máy Tính Bảng (iPad)', 'iPad Pro, iPad Air, Samsung Galaxy Tab chính hãng'],
    [104, 'Âm Thanh & Tai Nghe', 'Tai nghe chống ồn, loa Bluetooth Sony, Marshall, Apple'],
    [105, 'Đồng Hồ Thông Minh', 'Apple Watch, Galaxy Watch, Garmin đo sức khỏe chuyên sâu'],
    [106, 'Phụ Kiện & Gaming', 'Chuột, bàn phím cơ, sạc nhanh GaN, cáp sạc Anker'],
    [107, 'Flash Sale Giá Sốc', 'Chương trình xả kho đồ công nghệ giảm giá đến 50%']
];

foreach ($categories as $cat) {
    $cid = $cat[0];
    $name = $mysqli->real_escape_string($cat[1]);
    $desc = $mysqli->real_escape_string($cat[2]);
    $mysqli->query("REPLACE INTO oc_category (category_id, parent_id, sort_order, status) VALUES ($cid, 0, $cid, 1)");
    $mysqli->query("REPLACE INTO oc_category_description (category_id, language_id, name, description, meta_title, meta_description, meta_keyword) VALUES ($cid, 1, '$name', '$desc', '$name', '$desc', '$name')");
    $mysqli->query("REPLACE INTO oc_category_to_store (category_id, store_id) VALUES ($cid, 0)");
}

// Products
$products = [
    [45, 'iPhone 16 Pro Max 256GB - Titan Tự Nhiên', 'IP16PM-256', 32990000, 'catalog/tech/iphone16_pro.jpg', 8, [101, 107], 'Apple A18 Pro 3nm, Màn hình 6.9 inch 120Hz Super Retina XDR, Camera 48MP Zoom 5X, Khung viền Titanium chuẩn hàng không vũ trụ.'],
    [202, 'Samsung Galaxy S25 Ultra 5G (12GB/512GB)', 'S25U-512', 29990000, 'catalog/tech/samsung_ultra.jpg', 8, [101, 107], 'Snapdragon 8 Gen 4 for Galaxy, Màn hình Dynamic AMOLED 2X 6.8 inch 2600 nits, Bút S-Pen tích hợp, Camera 200MP Zoom AI 100x.'],
    [203, 'MacBook Pro 14 M3 Pro (18GB / 512GB SSD)', 'MBP14-M3P', 48990000, 'catalog/tech/macbook_m3.jpg', 8, [102], 'Chip Apple M3 Pro 11 CPU / 14 GPU, Màn hình Liquid Retina XDR 120Hz 1600 nits, Pin 18 giờ liên tục, Màu Đen Không Gian (Space Black).'],
    [204, 'Laptop Gaming ASUS ROG Strix G16 RTX 4060', 'G614-I74060', 33490000, 'catalog/tech/laptop_gaming.jpg', 8, [102, 107], 'Intel Core i7-13650HX 14 nhân, GPU RTX 4060 8GB GDDR6 140W TGP, Màn hình 16 inch QHD+ 240Hz 100% DCI-P3, Tản nhiệt 3 quạt ROG Intelligent.'],
    [205, 'iPad Pro 11 M4 OLED Wi-Fi 256GB Mỏng Nhất', 'IPAD-M4-256', 27490000, 'catalog/tech/ipad_pro.jpg', 8, [101, 103], 'Chip Apple M4 thế hệ mới, Thiết kế siêu mỏng 5.3mm, Màn hình Ultra Retina XDR công nghệ Tandem OLED kép đỉnh cao, Hỗ trợ Apple Pencil Pro.'],
    [206, 'Tai Nghe Chống Ồn Sony WH-1000XM5 Hi-Res', 'WH1000XM5', 7490000, 'catalog/tech/sony_headphones.jpg', 8, [104, 107], 'Bộ xử lý chống ồn đỉnh cao Integrated Processor V1 và QN1, 8 micro lọc âm, Thời lượng pin 30 giờ sạc nhanh 3 phút nghe 3 giờ, Âm thanh Hi-Res LDAC.'],
    [207, 'Apple Watch Ultra 2 GPS + Cellular 49mm', 'AW-ULTRA2', 19990000, 'catalog/tech/smartwatch.jpg', 8, [105], 'Vỏ Titanium cấp quân sự 49mm, Màn hình 3000 nits sáng nhất mọi thời đại, Kháng nước 100m chuẩn thợ lặn, Thời lượng pin tới 72 giờ ở chế độ tiết kiệm.'],
    [301, 'Chuột Không Dây Công Thái Học Logitech MX Master 3S', 'MX-M3S', 2190000, 'catalog/tech/mouse_keyboard.jpg', 8, [106], 'Cảm biến 8000 DPI Darkfield lướt trên mọi mặt phẳng kể cả kính, Cuộn siêu tốc MagSpeed 1000 dòng/giây, Cú click tĩnh âm 90%, Kết nối đa thiết bị Easy-Switch.']
];

foreach ($products as $p) {
    $pid = $p[0];
    $name = $mysqli->real_escape_string($p[1]);
    $model = $mysqli->real_escape_string($p[2]);
    $price = $p[3];
    $img = $p[4];
    $manuf = $p[5];
    $cat_ids = $p[6];
    $desc = $mysqli->real_escape_string($p[7]);

    $mysqli->query("REPLACE INTO oc_product (product_id, master_id, model, location, quantity, stock_status_id, image, manufacturer_id, shipping, price, points, tax_class_id, date_available, weight, weight_class_id, length, width, height, length_class_id, subtract, minimum, sort_order, status, date_added, date_modified) 
        VALUES ($pid, 0, '$model', '', 100, 7, '$img', $manuf, 1, $price, 0, 0, '2020-01-01', 0.5, 1, 0, 0, 0, 1, 1, 1, $pid, 1, NOW(), NOW())");

    $mysqli->query("REPLACE INTO oc_product_description (product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword) 
        VALUES ($pid, 1, '$name', '$desc', '$name', '$name', '$desc', '$name')");

    $mysqli->query("REPLACE INTO oc_product_to_store (product_id, store_id) VALUES ($pid, 0)");

    // Link to categories
    foreach ($cat_ids as $c_id) {
        $mysqli->query("REPLACE INTO oc_product_to_category (product_id, category_id) VALUES ($pid, $c_id)");
    }
}

// Add extra thumbnails for product 45 (iPhone 16 Pro)
$mysqli->query("DELETE FROM oc_product_image WHERE product_id = 45");
$mysqli->query("INSERT INTO oc_product_image (product_id, image, sort_order) VALUES (45, 'catalog/tech/iphone16_pro.jpg', 1)");
$mysqli->query("INSERT INTO oc_product_image (product_id, image, sort_order) VALUES (45, 'catalog/tech/samsung_ultra.jpg', 2)");
$mysqli->query("INSERT INTO oc_product_image (product_id, image, sort_order) VALUES (45, 'catalog/tech/ipad_pro.jpg', 3)");

echo "Database updated successfully with Electronics Products!\n";
"""

res = subprocess.run([php_exe, "-r", code], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("ERR:", res.stderr)
