# TTL Shop – Đồ án Web1 (website tĩnh HTML/CSS)

Mở `index.html` để vào trang chủ cửa hàng. Khu quản trị: `admin/login.html` (có link chuyển qua lại với `pages/auth/login.html`).
Không có cơ sở dữ liệu và không xử lý logic: dữ liệu là mẫu, các trang chỉ là giao diện.
JavaScript duy nhất: `admin/assets/js/preview.js` (xem trước ảnh khi chọn file ở trang thêm/sửa sản phẩm).

## Cấu trúc thư mục

```
ttlshop/
├── index.html                  Trang chủ (người dùng)
├── README.md
│
├── assets/                     Tài nguyên DÙNG CHUNG cho cả cửa hàng và admin
│   ├── css/
│   │   ├── style.css           Giao diện nền của cửa hàng
│   │   ├── ui-overrides.css    Ghi đè/hoàn thiện giao diện (nạp sau style.css)
│   │   ├── an-san-pham.css     Hộp thoại "thêm vào giỏ"
│   │   ├── product-detail.css  Trang chi tiết sản phẩm
│   │   └── order.css           Giỏ hàng, đơn hàng
│   ├── fonts/fonts.css         Font Be Vietnam Pro (nhúng sẵn, không cần mạng)
│   ├── images/                 Ảnh sản phẩm, banner; logo.png (logo đầy đủ), logo-icon.png (chỉ biểu tượng, dùng cho admin)
│   └── downloads/              File tải về (bản sao đơn hàng .txt)
│
├── pages/                      Các trang của NGƯỜI MUA
│   ├── auth/                   login, dang-ky, dang-ky-thanh-cong, dang-nhap-thanh-cong
│   ├── danh-muc/               category-* (theo phân loại), top-ban-chay
│   ├── san-pham/               product-detail-*
│   ├── tim-kiem/               tim-kiem (cơ bản + nâng cao), tim-kiem-* (tìm nhanh theo loại)
│   ├── mua-hang/               cart, don-hang-thanh-cong, kiem-tra-don-hang
│   ├── tai-khoan/              tai-khoan, lich-su-mua-hang
│   └── danh-gia.html           Đánh giá của khách về cửa hàng
│
├── admin/                      Khu vực QUẢN TRỊ (URL riêng, tách khỏi người dùng)
│   ├── login.html, logout.html, login-thanh-cong.html, index.html (tổng quan)
│   ├── assets/css/admin.css    Giao diện riêng của admin
│   ├── assets/js/preview.js
│   ├── san-pham/               products, product-add/-added, product-edit-*, product-saved
│   ├── don-hang/               orders, order-* (chi tiết + cập nhật trạng thái)
│   ├── khach-hang/             users, user-add, user-edit-*, user-saved
│   ├── quan-tri-vien/          admins, admin-add, admin-edit-*, admin-saved
│   └── thong-ke/               stats (top 5 khách mua nhiều nhất)
│
└── tools/tai-anh-ve-may.py     Script cũ tải ảnh về máy (ảnh đã có sẵn, không cần chạy)
```

## Quy ước
- Trang người mua nằm trong `pages/<nhóm>/`; trang admin nằm trong `admin/<nhóm>/`.
- CSS/ảnh/font dùng chung để trong `assets/`; chỉ CSS/JS của admin để trong `admin/assets/`.
- Tên file giữ nguyên như bản cũ, chỉ đổi vị trí; toàn bộ đường dẫn đã được cập nhật (đã kiểm tra, không có link gãy).
