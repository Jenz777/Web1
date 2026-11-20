# TTL Shop – Đồ án Web1 (website tĩnh HTML/CSS/JS)

Mở `index.html` (trang chủ chưa đăng nhập) để bắt đầu. Khu quản trị: `admin/login.html` (có link chuyển qua lại với `pages/auth/login.html`).
Không có cơ sở dữ liệu và không xử lý logic: dữ liệu là mẫu, các trang chỉ là giao diện.
JavaScript chỉ có 2 file nhỏ, không xử lý dữ liệu: `admin/assets/js/preview.js` (xem trước ảnh khi chọn file ở trang thêm/sửa sản phẩm) và `assets/js/format-gia.js` (tự thêm dấu chấm hàng nghìn khi gõ vào ô khoảng giá ở trang tìm kiếm và ô giá bán ở trang thêm/sửa sản phẩm admin).

## Cấu trúc thư mục

```
ttlshop/
├── index.html                  TRANG BẮT ĐẦU: trang chủ khi CHƯA đăng nhập (mở file này để chấm)
├── README.md
│
├── assets/                     Tài nguyên DÙNG CHUNG (css, font, ảnh, file tải về, format-gia.js)
│
├── pages/                      Các trang của KHÁCH chưa đăng nhập
│   ├── auth/                   login, dang-ky, dang-ky-thanh-cong
│   ├── danh-muc/               category-* (theo phân loại), top-ban-chay
│   ├── san-pham/               product-detail-*
│   ├── tim-kiem/               tim-kiem (cơ bản + nâng cao), tim-kiem-* (tìm nhanh theo loại)
│   ├── mua-hang/               kiem-tra-don-hang, don-hang-thanh-cong (kết quả tra cứu)
│   └── danh-gia.html
│
├── da-dang-nhap/               Giao diện NGƯỜI MUA SAU KHI ĐĂNG NHẬP
│   ├── index.html              Trang chủ đã đăng nhập
│   └── pages/                  auth/dang-nhap-thanh-cong, danh-muc, san-pham, tim-kiem,
│                               mua-hang (cart, don-hang-thanh-cong, kiem-tra-don-hang),
│                               tai-khoan (tai-khoan: gồm các mục #thong-tin, #dia-chi, #mat-khau, #don-hang, #lich-su; chi-tiet-don-hang-*), danh-gia.html
│
└── admin/                      Khu vực QUẢN TRỊ (CSS/JS riêng trong admin/assets/)
    ├── login, login-thanh-cong, logout, index (tổng quan, có chọn khoảng thời gian)
    ├── san-pham/               products (nút Xem mở trang chi tiết của khách; Xoá/Ẩn có popup xác nhận),
    │                           product-add/-added, product-saved, product-deleted, product-hidden,
    │                           product-edit-1/2/3/5/13 (mỗi danh mục 1 trang sửa, bố cục như trang chi tiết của khách;
    │                           mọi sản phẩm cùng danh mục trỏ về trang này)
    ├── don-hang/               orders, order-chua-xac-nhan / da-xac-nhan / giao-thanh-cong / da-huy,
    │                           order-saved-* (trang kết quả sau khi cập nhật trạng thái; chỉ là giao diện, không đổi dữ liệu thật)
    ├── khach-hang/             users, user-detail-1..7 (chỉ xem, không sửa), user-add, user-saved
    ├── quan-tri-vien/          admins, admin-add, admin-edit-1..3, admin-saved
    └── thong-ke/               stats
```

Luồng: `index.html` (khách) → `pages/auth/login.html` → `da-dang-nhap/pages/auth/dang-nhap-thanh-cong.html` → giỏ hàng. Đăng xuất quay về `pages/auth/login.html`.

## Quy ước
- Trang khách chưa đăng nhập nằm trong `pages/<nhóm>/`; trang sau đăng nhập nằm trong `da-dang-nhap/pages/<nhóm>/`; trang admin nằm trong `admin/<nhóm>/`.
- CSS/ảnh/font dùng chung để trong `assets/`; chỉ CSS/JS của admin để trong `admin/assets/` (admin-product.css dùng lại product-detail.css của cửa hàng).
