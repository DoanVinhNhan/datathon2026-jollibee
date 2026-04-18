Dưới đây là sơ đồ luồng hoạt động kinh doanh (Business Process Flow) và luồng dữ liệu (Data Flow) tương ứng, được suy luận từ cấu trúc cơ sở dữ liệu của doanh nghiệp. Quá trình này mô phỏng toàn bộ hành trình khách hàng (Customer Journey) từ điểm chạm đầu tiên cho đến khi hoàn tất vòng đời của một đơn hàng.

### 1. Giai đoạn Truy cập & Tương tác (Acquisition & Browsing)
* **Hoạt động:** Khách hàng nhấp vào website thông qua các kênh marketing (traffic_source). Họ duyệt qua trang web, xem thông tin sản phẩm và có thể thoát ra hoặc tiếp tục thao tác.
* **Luồng dữ liệu:**
    * Bảng `web_traffic.csv` ghi nhận lưu lượng hàng ngày: `sessions`, `page_views`, `unique_visitors`, thời gian trung bình (`avg_session_duration_sec`) và tỷ lệ thoát (`bounce_rate`).
    * Hệ thống truy xuất `products.csv` để hiển thị `product_name`, `category`, `price`.

### 2. Giai đoạn Định danh Khách hàng (User Registration)
* **Hoạt động:** Nếu đây là khách hàng mới, họ sẽ đăng ký tài khoản. Nếu là khách cũ, họ tiến hành đăng nhập.
* **Luồng dữ liệu:**
    * Bảng `customers.csv` ghi lại thông tin người dùng mới: `customer_id`, `signup_date`, nhóm tuổi (`age_group`), giới tính (`gender`), và kênh tiếp thị mang khách hàng đến (`acquisition_channel`).
    * Dữ liệu vị trí của khách hàng (`zip`) được liên kết với `geography.csv` để xác định `city`, `district`, `region`.

### 3. Giai đoạn Quyết định mua & Thêm vào giỏ hàng (Consideration & Cart)
* **Hoạt động:** Khách hàng quyết định mua hàng, áp dụng các mã giảm giá nếu có. Hệ thống ngầm kiểm tra xem hàng có còn trong kho không.
* **Luồng dữ liệu:**
    * Hệ thống đối chiếu với `inventory.csv` (các chỉ số như `stock_on_hand`) để đảm bảo sản phẩm có sẵn.
    * Hệ thống kiểm tra `promotions.csv` để xác định điều kiện áp dụng mã giảm giá: thời gian (`start_date`, `end_date`), giá trị tối thiểu (`min_order_value`), và cờ cộng dồn (`stackable_flag`).

### 4. Giai đoạn Tạo đơn hàng & Thanh toán (Checkout & Payment)
* **Hoạt động:** Khách hàng chốt đơn, chọn phương thức thanh toán và hoàn tất giao dịch.
* **Luồng dữ liệu:**
    * Bảng `orders.csv` tạo bản ghi mới (Transaction Master): `order_id`, `order_date`, `device_type`, `order_source`, cập nhật `order_status` thành *Pending/Processing*.
    * Bảng `order_items.csv` ghi lại chi tiết từng sản phẩm (quan hệ 1:N với orders): `product_id`, `quantity`, `unit_price` sau giảm giá, và mã khuyến mãi đã dùng (`promo_id`, `promo_id_2`). Công thức giảm giá ở bảng `promotions` được kích hoạt để tính `discount_amount`.
    * Bảng `payments.csv` ghi nhận giao dịch thành công (quan hệ 1:1 với orders): `payment_value`, `payment_method`, `installments`. `order_status` chuyển sang *Paid*.

### 5. Giai đoạn Xử lý kho & Vận chuyển (Fulfillment & Shipping)
* **Hoạt động:** Đơn hàng được xuất kho và giao cho đơn vị vận chuyển để đưa đến tay khách hàng.
* **Luồng dữ liệu:**
    * Bảng `inventory.csv` và `inventory_enhanced.csv` (Operational) được cập nhật: `units_sold` tăng, `stock_on_hand` giảm.
    * Bảng `shipments.csv` tạo bản ghi mới: `ship_date`, `shipping_fee`. Trạng thái `order_status` chuyển thành *Shipped*.
    * Khi khách nhận được hàng, cập nhật `delivery_date` và `order_status` thành *Delivered*.

### 6. Giai đoạn Hậu mãi: Đánh giá hoặc Trả hàng (Post-Purchase Action)
Tại đây, luồng rẽ nhánh theo trải nghiệm của khách hàng:
* **Nhánh A (Khách hàng hài lòng - Đánh giá):**
    * Hoạt động: Khách hàng để lại nhận xét cho sản phẩm.
    * Luồng dữ liệu: Bảng `reviews.csv` ghi nhận `rating` (1-5 sao), `review_title`, `review_date`.
* **Nhánh B (Khách hàng không hài lòng - Trả hàng):**
    * Hoạt động: Khách hàng yêu cầu trả hàng và hoàn tiền.
    * Luồng dữ liệu: Bảng `returns.csv` ghi nhận `return_date`, `return_reason`, `return_quantity` và `refund_amount`. `order_status` chuyển thành *Returned*.

### 7. Giai đoạn Tổng hợp Phân tích (Data Analytics & Reporting)
* **Hoạt động:** Vào cuối ngày/tháng, doanh nghiệp chạy các báo cáo hiệu quả kinh doanh.
* **Luồng dữ liệu:**
    * Các giao dịch thành công được tổng hợp vào bảng `sales.csv` (Analytical) để tính toán `Revenue` (Doanh thu thuần) và `COGS` (Giá vốn hàng bán).
    * Bảng `web_traffic.csv` tính toán `conversion_rate` (tỷ lệ chuyển đổi ra đơn hàng).
    * Dữ liệu này được dùng cho các mô hình dự báo (ví dụ: chia tập `sales.csv` thành Train/Test để dự báo doanh thu tương lai).

---

### Tóm tắt Sơ đồ Luồng (Flowchart)

```text
[Khách truy cập Web] (web_traffic)
        │
        ▼
[Đăng ký/Đăng nhập] (customers + geography)
        │
        ▼
[Xem Sản phẩm & Áp mã Khuyến mãi] (products + inventory + promotions)
        │
        ▼
[Tạo Đơn Hàng] (orders + order_items)
        │
        ▼
[Thanh toán] (payments) ──> Trạng thái: Paid
        │
        ▼
[Xuất kho & Vận chuyển] (shipments + inventory) ──> Trạng thái: Shipped ──> Delivered
        │
        ├─────────────────────────────┐
        ▼                             ▼
[Viết Đánh Giá] (reviews)     [Yêu cầu Trả hàng] (returns) ──> Trạng thái: Returned
        │                             │
        └──────────────┬──────────────┘
                       ▼
[Tổng hợp Doanh thu & Báo cáo] (sales + web_traffic)
```