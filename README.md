# Datathon 2026 - Jollibee Visualization Project

Dự án này chứa bộ script Python tự động phân tích và trực quan hóa dữ liệu Datathon 2026 dựa trên cấu trúc vận hành của doanh nghiệp thương mại điện tử/bán lẻ.

## Cấu trúc Script Trực quan hóa

Các biểu đồ được chia thành 9 nhóm chuyên sâu, tương ứng với các file `visualize_group_*.py`:

1.  **visualize_group_1.py (Sales & Revenue Overview)**: Phân tích các chỉ số cốt lõi về doanh thu, số lượng đơn hàng, AOV và hiệu suất bán hàng tổng thể.
2.  **visualize_group_2.py (Finance, Payments & Profitability)**: Tập trung vào hiệu quả tài chính, phương thức thanh toán, tình trạng hủy đơn và tỷ suất lợi nhuận.
3.  **visualize_group_3.py (Customer Behavior & CRM)**: Phân tích tệp khách hàng, tần suất mua hàng, giỏ hàng (Market Basket) và giá trị vòng đời (CLV).
4.  **visualize_group_4.py (Reviews & Customer Satisfaction)**: Theo dõi các chỉ số về xếp hạng, cảm nhận của người mua và tỷ lệ phản hồi.
5.  **visualize_group_5.py (Return Management)**: Phân tích chi tiết về hàng hoàn trả, lý do trả, rủi ro kích cỡ và chi phí chìm.
6.  **visualize_group_6.py (Logistics & Delivery)**: Phân tích thời gian xử lý đơn, giao nhận hàng hóa và chi phí vận chuyển theo vùng miền.
7.  **visualize_group_7.py (Traffic, Web Funnel & Omnichannel)**: Phân tích lưu lượng website, phễu chuyển đổi UI/UX và hành trình đa kênh (O2O).
8.  **visualize_group_8.py (Promotions & Pricing Strategy)**: Đánh giá hiệu quả các chiến dịch khuyến mãi, mã giảm giá và tác động đến biên lợi nhuận.
9.  **visualize_group_9.py (Merchandising & Inventory)**: Quản trị SKU, tốc độ hao mòn tồn kho (Sell-through rate) và tình trạng cạn/quá tải kho.

## Hướng dẫn sử dụng

### 1. Yêu cầu hệ thống
- Python 3.8+
- Các thư viện cần thiết:
  ```bash
  pip install pandas numpy matplotlib
  ```

### 2. Cấu trúc thư mục dữ liệu

**Lưu ý:** Các file dữ liệu `.csv` không được bao gồm trong repository này để giảm dung lượng. Bạn cần tải dataset và đặt chúng vào thư mục `dataset/` ở thư mục gốc của project:

```
.
├── dataset/
│   ├── customers.csv
│   ├── orders.csv
│   └── ...
├── visualize_group_1.py
├── ...
└── README.md
```

### 3. Chạy script
Bạn có thể chạy từng nhóm phân tích bằng cách thực hiện lệnh sau trong terminal:
```bash
python visualize_group_1.py
```
Mỗi script sẽ xử lý dữ liệu, tính toán các chỉ số và hiển thị các biểu đồ tương ứng.

---
*Ghi chú: Dữ liệu sử dụng trong dự án này được trích xuất và xử lý từ bộ dataset Datathon 2026.*
