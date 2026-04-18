Ngành bán lẻ thời trang có một hệ sinh thái dữ liệu rất đặc thù, phức tạp hơn nhiều so với các ngành bán lẻ truyền thống (như tạp hóa hay điện máy) vì tính chất vòng đời sản phẩm ngắn, tính xu hướng cao và sự đa dạng về biến thể (màu sắc, kích cỡ). 

Dưới đây là các mảng "Business Knowledge" (kiến thức nghiệp vụ) cốt lõi liên quan đến dữ liệu trong ngành này:

### 1. Quản trị Sản phẩm & Tồn kho (Merchandising & Inventory)
Đây là trái tim của dữ liệu thời trang, nơi quyết định doanh nghiệp có bị đọng vốn hay không.

* **Độ phức tạp của SKU (Stock Keeping Unit):** Trong thời trang, một mẫu áo (Style) có thể sinh ra hàng chục SKU dựa trên ma trận **Màu sắc (Color) x Kích cỡ (Size)**. Dữ liệu phải quản lý được đến cấp độ SKU nhỏ nhất thay vì chỉ ở cấp độ Style.
* **Sell-Through Rate (STR - Tỷ lệ bán hàng):** Tỷ lệ phần trăm hàng hóa đã bán so với lượng hàng nhập về ban đầu trong một khoảng thời gian. Chỉ số này giúp xác định bộ sưu tập nào đang "hot" và bộ sưu tập nào có nguy cơ tồn kho.
* **Weeks of Supply (WOS - Số tuần bán hàng tồn kho):** Dữ liệu dự báo lượng tồn kho hiện tại sẽ bán được trong bao nhiêu tuần tới dựa trên tốc độ bán hiện tại, giúp ra quyết định châm hàng (replenishment) hoặc cắt giảm.
* **Markdown Optimization (Tối ưu hóa giảm giá):** Dữ liệu về vòng đời sản phẩm để quyết định *khi nào* nên bắt đầu giảm giá hàng lỗi mốt và *giảm bao nhiêu phần trăm* để vừa đẩy được hàng tồn vừa tối ưu hóa biên lợi nhuận (Profit Margin).

### 2. Dữ liệu Hành vi Mua sắm & Doanh thu (Sales & POS Data)
Dữ liệu từ các điểm bán (offline và online) giúp phân tích hiệu quả kinh doanh thực tế.

* **AOV (Average Order Value - Giá trị trung bình đơn hàng):** Khách hàng thường chi bao nhiêu tiền trên một hóa đơn.
* **UPT (Units Per Transaction - Số sản phẩm trên mỗi giao dịch):** Trung bình một hóa đơn khách mua mấy món. Trong thời trang, chỉ số này rất quan trọng để đánh giá năng lực tư vấn phối đồ (mix & match) của nhân viên hoặc hệ thống gợi ý trên website.
* **Market Basket Analysis (Phân tích giỏ hàng):** Tìm ra quy luật mua chéo. Ví dụ: Dữ liệu cho thấy khách mua áo sơ mi trắng thường mua kèm cà vạt xanh hoặc thắt lưng da. Kiến thức này dùng để sắp xếp trưng bày (Visual Merchandising) hoặc gợi ý combo online.
* **Omnichannel Tracking (Dữ liệu Đa kênh):** Khả năng theo dõi hành trình khách hàng từ lúc xem hàng trên Facebook, bỏ vào giỏ trên Website, đến lúc ra cửa hàng vật lý để thử size và chốt mua (O2O - Online to Offline).

### 3. Quản trị Quan hệ Khách hàng (CRM & Customer Data)
Đặc thù của thời trang là tính cá nhân hóa cao, do đó dữ liệu khách hàng sâu sắc hơn các ngành khác.

* **RFM Analysis (Recency - Frequency - Monetary):** Phân khúc khách hàng dựa trên dữ liệu: Lần cuối họ mua là khi nào? Tần suất mua có thường xuyên không? Tổng tiền họ đã chi là bao nhiêu? Từ đó tạo ra các tệp VIP, tệp có nguy cơ rời bỏ (Churn) để có chiến dịch phù hợp.
* **Sizing & Fit Data (Dữ liệu Kích cỡ & Form dáng):** Đây là dữ liệu sống còn của thời trang online. Phân tích lý do hoàn hàng (Return Rate) thường xoay quanh việc sai kích cỡ. Các thương hiệu lớn dùng dữ liệu này để điều chỉnh lại bảng size (size chart) cho phù hợp với tệp khách hàng mục tiêu.
* **Customer Lifetime Value (CLV - Giá trị vòng đời khách hàng):** Dự đoán tổng lợi nhuận một khách hàng sẽ mang lại trong suốt thời gian họ gắn bó với thương hiệu, từ đó quyết định chi phí tối đa để thu hút một khách hàng mới (CAC - Customer Acquisition Cost).

### 4. Dự báo Xu hướng & Chuỗi cung ứng (Trend Forecasting & Supply Chain)
* **Trend Analysis (Phân tích xu hướng):** Sử dụng dữ liệu phi cấu trúc (Unstructured Data) từ Mạng xã hội, lượt tìm kiếm Google, hoặc các show thời trang để dự báo màu sắc, chất liệu hoặc form dáng nào sẽ lên ngôi trong mùa tới.
* **Lead Time Data (Thời gian cung ứng):** Thời trang nhanh (Fast Fashion) phụ thuộc vào việc tối ưu dữ liệu thời gian từ bản vẽ thiết kế, lấy rập, sản xuất đến khi treo lên kệ.
* **Seasonality (Tính mùa vụ):** Dữ liệu chuỗi thời gian (Time-series data) cực kỳ quan trọng vì thời trang phụ thuộc mạnh vào thời tiết, dịp lễ hội (Tết, Back-to-school, Mùa cưới).