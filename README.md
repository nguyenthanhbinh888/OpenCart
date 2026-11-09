# Dự Án Website Thương Mại Điện Tử OpenCart 4 - Thời Trang

Website bán hàng thời trang trực tuyến được phát triển trên nền tảng **OpenCart 4.x** kết hợp **PHP 8.2** và cơ sở dữ liệu **MySQL 8.0**, tùy biến giao diện và tính năng theo chuẩn đề bài thực hành.

---

## 1. Tính Năng Nổi Bật

- **Giao diện Trang chủ**:
  - Tích hợp 7 danh mục: Thời trang em bé, Váy & Đầm, Tặng quà, Thời trang, Thời trang biển, Thời trang nữ, Thời trang nam.
  - Banner quảng cáo thời trang độ phân giải cao (HD).
  - Khối sản phẩm dạng Carousel Slider cuộn ngang mượt mà.
  - Thanh tìm kiếm và giỏ hàng thời gian thực.
- **Trang Chi tiết Sản phẩm**:
  - Đầy đủ thông số: Nhà sản xuất (Apple), Mã sản phẩm (Product 18), Tình trạng (Còn hàng), Giá bán (600.000đ).
  - Tùy chọn số lượng (+ / -), thêm vào giỏ hàng qua AJAX, đánh giá và chia sẻ mạng xã hội.
  - Khối sản phẩm liên quan gồm 3 mẫu đầm/váy kèm đánh giá 5 sao.
- **Trang Thông tin Khuyến mại**:
  - Banner Flash Sale 2026.
  - Đồng hồ đếm ngược thời gian thực (Countdown Timer).
  - Các mã giảm giá (Voucher) có nút bấm sao chép nhanh.
- **Backend Quản trị**:
  - Trang Admin chuẩn OpenCart quản lý toàn bộ sản phẩm, danh mục, đơn hàng, khách hàng và cấu hình hệ thống.
  - Hỗ trợ đầy đủ tiền tệ VND (Việt Nam Đồng).

---

## 2. Cấu Trúc Dự Án

```
opencart/
├── upload/                     # Toàn bộ mã nguồn OpenCart (PHP, Twig, Assets)
│   ├── admin/                  # Backend quản trị viên
│   ├── catalog/                # Frontend và logic phía người dùng
│   ├── system/                 # Core framework, kết nối database, template engine
│   ├── image/                  # Hình ảnh sản phẩm và banners
│   ├── config.php              # Cấu hình website
│   └── index.php               # Điểm đón tiếp chính
├── database_opencart_full.sql  # Toàn bộ dữ liệu MySQL đã xuất sẵn
├── run.bat                     # File chạy nhanh máy chủ trên Windows
└── README.md                   # Hướng dẫn dự án
```

---

## 3. Hướng Dẫn Cài Đặt & Chạy Dự Án

### Yêu cầu môi trường
- PHP >= 8.2 (kèm các extension: `mysqli`, `pdo_mysql`, `curl`, `gd`, `mbstring`, `zip`)
- MySQL Server >= 8.0 (hoặc MariaDB)

### Các bước thực hiện
1. **Khởi tạo Cơ sở dữ liệu**:
   - Tạo một database mới tên là `opencart` trong MySQL:
     ```sql
     CREATE DATABASE opencart CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```
   - Nhập file dữ liệu `database_opencart_full.sql` vào database `opencart`:
     ```bash
     mysql -u root -p opencart < database_opencart_full.sql
     ```

2. **Cấu hình kết nối**:
   - Kiểm tra thông tin tài khoản MySQL trong `upload/config.php` và `upload/admin/config.php` (mặc định user `root`, mật khẩu `123456`, cổng `3306`).

3. **Khởi chạy máy chủ**:
   - Cách 1: Click đúp vào file `run.bat` trên Windows.
   - Cách 2: Chạy lệnh terminal từ thư mục `upload/`:
     ```bash
     cd upload
     php -S localhost:8000
     ```

---

## 4. Đường Dẫn Truy Cập

- **Trang chủ Website**: [http://localhost:8000/](http://localhost:8000/)
- **Trang Quản trị (Admin)**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
  - **Tên đăng nhập**: `admin`
  - **Mật khẩu**: `admin`
