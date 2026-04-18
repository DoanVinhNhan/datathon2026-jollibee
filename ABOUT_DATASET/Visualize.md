### Nhóm 1: Phân tích Doanh thu & Bán hàng tổng quan (Sales & Revenue Overview)
*Nhóm này tập trung vào các chỉ số cốt lõi về doanh thu, số lượng đơn hàng, AOV và hiệu suất bán hàng tổng thể.*

**1. Xu hướng doanh thu tổng quan (Revenue Trend)**
* **Chỉ số:** Doanh thu thu thuần (Revenue)
* **Khía cạnh:** Thời gian (Năm/Tháng)
* **Value:** Sum(Revenue)
* **Filter by:** Trạng thái đơn hàng (Order Status) = Completed/Delivered

**2. Cơ cấu doanh thu theo Danh mục (Revenue by Category)**
* **Chỉ số:** Doanh thu thu thuần (Revenue)
* **Khía cạnh:** Danh mục sản phẩm (Product Category)
* **Value:** % of Total Revenue hoặc Sum(Revenue)
* **Filter by:** Thời gian = Year to Date (YTD)

**3. Số lượng đơn hàng theo Trạng thái (Orders by Status)**
* **Chỉ số:** Số lượng đơn hàng (Orders count)
* **Khía cạnh:** Trạng thái đơn hàng (Order Status)
* **Value:** Count(Orders)
* **Filter by:** Thời gian = Tháng hiện tại

**4. Giá trị trung bình đơn hàng theo Phân khúc (AOV by Segment)**
* **Chỉ số:** Giá trị trung bình đơn (AOV)
* **Khía cạnh:** Phân khúc chất lượng (Segment hàng hóa)
* **Value:** Average(Revenue per Order)
* **Filter by:** Không có (None)

**5. Sản lượng bán ra hàng ngày (Daily Quantity Sold)**
* **Chỉ số:** Sản lượng bán ra (Quantity sold)
* **Khía cạnh:** Thời gian (Ngày đặt hàng)
* **Value:** Sum(Quantity)
* **Filter by:** Thời gian = Last 30 Days

**8. Top 10 Sản phẩm bán chạy nhất (Top 10 Products)**
* **Chỉ số:** Sản lượng bán ra (Quantity sold)
* **Khía cạnh:** Tên Sản phẩm / Danh mục sản phẩm
* **Value:** Sum(Quantity)
* **Filter by:** Top N = 10 (Dựa trên Quantity)

**9. Tương quan Số lượng đơn và AOV (Orders vs. AOV Scatter)**
* **Chỉ số:** Số lượng đơn hàng & AOV
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Count(Orders) trên trục X, Average(AOV) trên trục Y
* **Filter by:** Trạng thái đơn hàng = Completed

**10. So sánh Doanh thu cùng kỳ năm trước (YoY Revenue Comparison)**
* **Chỉ số:** Doanh thu thu thuần
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** Sum(Revenue) năm nay vs. năm trước
* **Filter by:** Không có

**70. Đóng góp Doanh thu theo Vùng lãnh thổ (Geographic Revenue - Q7)**
* **Chỉ số:** Tổng doanh thu
* **Khía cạnh:** Vùng địa lý (Region: West, Central, East)
* **Value:** Sum(Revenue)
* **Filter by:** Không có

---

### Nhóm 2: Tài chính, Thanh toán & Biên Lợi nhuận (Finance, Payments & Profitability)
*Nhóm này tập trung vào hiệu quả tài chính, phương thức thanh toán, tình trạng hủy đơn và tỷ suất lợi nhuận.*

**6. Tỷ trọng Phương thức thanh toán (Payment Method Breakdown)**
* **Chỉ số:** Cước phí thanh toán/Tổng tiền nạp (Payment value)
* **Khía cạnh:** Phương thức thanh toán (Payment Type)
* **Value:** Sum(Payment value)
* **Filter by:** Không có

**7. Doanh thu theo Phân khúc trả góp (Installment Revenue)**
* **Chỉ số:** Doanh thu thu thuần
* **Khía cạnh:** Phân khúc trả góp (Installment brackets)
* **Value:** Sum(Revenue)
* **Filter by:** Payment Type = Installment

**67. Biên lợi nhuận gộp theo Phân khúc SP (Gross Margin by Segment - Q2)**
* **Chỉ số:** Biên lợi nhuận gộp
* **Khía cạnh:** Phân khúc sản phẩm (Premium, Performance, Activewear, Standard)
* **Value:** Average( $(Price - COGS)/Price$ )
* **Filter by:** Không có

**68. Giá trị đơn hàng theo Kỳ hạn trả góp (AOV by Installment Terms - Q10)**
* **Chỉ số:** Giá trị thanh toán trung bình
* **Khía cạnh:** Kế hoạch trả góp (1 kỳ, 3 kỳ, 6 kỳ, 12 kỳ)
* **Value:** Average(Order Value)
* **Filter by:** Hình thức = Installment/BNPL

**69. Tỷ lệ hủy đơn theo Phương thức thanh toán (Cancellations by Payment - Q8)**
* **Chỉ số:** Số lượng đơn bị hủy
* **Khía cạnh:** Phương thức thanh toán (COD, Credit Card, Paypal...)
* **Value:** Count(Orders) hoặc % of Total Orders per Method
* **Filter by:** Order_Status = 'Cancelled'

**71. Lợi nhuận ròng sau Hoàn trả theo Danh mục (Net Profit post-Returns)**
* **Chỉ số:** Lợi nhuận thực tế
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Sum(Gross Profit) - Sum(Return Value) - Sum(Return Ops Cost)
* **Filter by:** Không có

**72. Doanh thu theo Kênh thanh toán (Revenue by Payment Channel)**
* **Chỉ số:** Doanh thu thu thuần
* **Khía cạnh:** Kênh thanh toán / Cổng thanh toán
* **Value:** Sum(Revenue)
* **Filter by:** Trạng thái thanh toán = Success

**73. Tương quan Khối lượng giảm giá và Tăng trưởng lợi nhuận (Discount vs Margin Impact)**
* **Chỉ số:** Tổng Giảm giá & Biên lợi nhuận
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** Sum(Discount Amount) (Trục X) vs Avg(Gross Margin) (Trục Y)
* **Filter by:** Không có

**74. Tỷ lệ khách hàng mua trước trả sau (BNPL Adoption Rate)**
* **Chỉ số:** % Số đơn hàng dùng BNPL
* **Khía cạnh:** Nhóm tuổi khách hàng
* **Value:** Count(BNPL Orders) / Total Orders
* **Filter by:** Phân khúc = Premium

---

### Nhóm 3: Hành vi & Vòng đời Khách hàng (Customer Behavior & CRM)
*Nhóm này đi sâu vào phân tích tệp khách hàng, tần suất, rổ hàng và giá trị vòng đời (CLV).*

**59. Phân bổ khoảng cách mua lặp lại (Inter-order Gap - Q1)**
* **Chỉ số:** Số lượng khách hàng
* **Khía cạnh:** Số ngày giữa 2 lần mua (Inter-order gap brackets: <30, 30-90, 90-180, >180)
* **Value:** Count(Distinct Customer_ID)
* **Filter by:** Khách hàng có > 1 đơn hàng

**60. Tần suất mua hàng theo Nhóm tuổi (Purchase Frequency by Age - Q6)**
* **Chỉ số:** Số đơn hàng trung bình (Avg Orders per Customer)
* **Khía cạnh:** Nhóm tuổi (Age group: 25-34, 35-44...)
* **Value:** Total Orders / Count(Customers)
* **Filter by:** Không có

**61. Số sản phẩm trên mỗi giao dịch (UPT - Units Per Transaction)**
* **Chỉ số:** Số lượng sản phẩm trung bình/đơn
* **Khía cạnh:** Kênh mua sắm (Online vs Offline / App vs Web)
* **Value:** Sum(Quantity) / Count(Orders)
* **Filter by:** Không có

**62. Phân khúc Khách hàng theo RFM (RFM Customer Segments)**
* **Chỉ số:** Số lượng khách hàng
* **Khía cạnh:** Nhóm RFM (VIP, Loyal, At-Risk, Churn)
* **Value:** Count(Customer_ID)
* **Filter by:** Không có

**63. Lưới Phân tích Giỏ hàng (Market Basket - Cross-sell Matrix)**
* **Chỉ số:** Mức độ kết hợp (Affinity score / Order Count)
* **Khía cạnh:** Danh mục X (Cột) và Danh mục Y (Hàng)
* **Value:** Count(Orders có cả X và Y)
* **Filter by:** Kích thước giỏ hàng > 1

**64. Giá trị vòng đời khách hàng theo Nguồn thu hút (CLV by Acquisition Source)**
* **Chỉ số:** Giá trị vòng đời (CLV)
* **Khía cạnh:** Nguồn khách hàng ban đầu (First-touch Source)
* **Value:** Average(Total Revenue per Customer trọn đời)
* **Filter by:** Tuổi đời tài khoản > 1 năm

**65. Tỷ lệ giữ chân khách hàng (Retention Cohort Heatmap)**
* **Chỉ số:** Tỷ lệ khách hàng quay lại (%)
* **Khía cạnh:** Tháng mua hàng đầu tiên (Cohort) x Tháng thứ N (Month 1, Month 2...)
* **Value:** % Active Customers
* **Filter by:** Không có

**66. Phân bổ Giá trị đơn hàng theo Giới tính (AOV by Gender)**
* **Chỉ số:** Giá trị trung bình đơn
* **Khía cạnh:** Giới tính khách hàng (Gender)
* **Value:** Average(Order Value)
* **Filter by:** Không có

---

### Nhóm 4: Đánh giá & Trải nghiệm Khách hàng (Reviews & Customer Satisfaction)
*Nhóm này theo dõi các chỉ số về xếp hạng, tỷ lệ phản hồi và cảm nhận của người mua.*

**21. Điểm đánh giá trung bình theo Danh mục (Avg Review by Category)**
* **Chỉ số:** Điểm đánh giá trung bình (Avg Review score)
* **Khía cạnh:** Danh mục sản phẩm bị đánh giá
* **Value:** Average(Review score)
* **Filter by:** Không có

**22. Tỷ lệ Đánh giá Tích cực / Tiêu cực (Sentiment Distribution)**
* **Chỉ số:** Tỷ lệ đánh giá Tiêu cực (1-2 sao) & Tích cực (4-5 sao)
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** % of Total Reviews
* **Filter by:** Không có

**24. Điểm đánh giá theo Nhóm tuổi (Review Score by Age Group)**
* **Chỉ số:** Điểm đánh giá trung bình
* **Khía cạnh:** Nhóm tuổi khách hàng (Age group)
* **Value:** Average(Review score)
* **Filter by:** Không có

**26. Lượng đánh giá theo Giới tính (Review Volume by Gender)**
* **Chỉ số:** Tổng số lượng đánh giá
* **Khía cạnh:** Giới tính khách hàng (Gender)
* **Value:** Count(Reviews)
* **Filter by:** Không có

**28. Xu hướng điểm đánh giá theo thời gian mua (Review Score Trend)**
* **Chỉ số:** Điểm đánh giá trung bình
* **Khía cạnh:** Thời gian mua hàng (Tháng)
* **Value:** Average(Review score)
* **Filter by:** Không có

**30. Tỷ lệ phản hồi đánh giá (Review Response Rate)**
* **Chỉ số:** Tổng số lượng đánh giá
* **Khía cạnh:** Nhóm tuổi khách hàng
* **Value:** Count(Reviews) / Count(Customers) (%)
* **Filter by:** Khách hàng đã nhận hàng (Delivered)

---

### Nhóm 5: Quản lý Hàng hoàn trả & Rủi ro (Return Management)
*Toàn bộ các biểu đồ liên quan đến việc trả hàng, lý do trả, chi phí trả và rủi ro kích cỡ được gom vào một hệ sinh thái riêng.*

**23. Lý do trả hàng phổ biến (Top Return Reasons)**
* **Chỉ số:** Tỷ lệ hoàn trả hàng (Return rate)
* **Khía cạnh:** Lý do trả hàng (Return reason)
* **Value:** Count(Returns)
* **Filter by:** Trạng thái = Returned

**25. Tỷ lệ trả hàng theo Nguồn khách (Return Rate by Acquisition Channel)**
* **Chỉ số:** Tỷ lệ hoàn trả hàng
* **Khía cạnh:** Nguồn thu hút khách (Acquisition channel)
* **Value:** Count(Returns) / Total Orders (%)
* **Filter by:** Không có

**27. Tương quan Điểm đánh giá và Tỷ lệ hoàn trả (Satisfaction vs. Returns)**
* **Chỉ số:** Điểm đánh giá TB & Tỷ lệ hoàn trả
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Avg(Review score) & % Return rate
* **Filter by:** Không có

**29. Danh mục sản phẩm bị hoàn trả nhiều nhất (Highest Return Categories)**
* **Chỉ số:** Tỷ lệ hoàn trả hàng
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Count(Returns)
* **Filter by:** Top N = 5 danh mục

**51. Phân tích rủi ro kích cỡ (Sizing Risk Analysis - Q9)**
* **Chỉ số:** Tỷ lệ hoàn trả (Return Rate)
* **Khía cạnh:** Kích thước sản phẩm (Size: S, M, L, XL)
* **Value:** Count(Returns) / Count(Order_Items) (%)
* **Filter by:** Không có

**52. Phân bổ lý do trả hàng theo Danh mục (Return Reasons by Category - Q3)**
* **Chỉ số:** Số lượng đơn hoàn trả
* **Khía cạnh:** Lý do trả hàng (Defective, Wrong_size, Changed_mind...) & Danh mục (VD: Streetwear)
* **Value:** Count(Returns)
* **Filter by:** Danh mục = Streetwear (Hoặc để động theo Slicer)

**53. Tỷ lệ hoàn trả theo Màu sắc (Color Return Rate)**
* **Chỉ số:** Tỷ lệ hoàn trả
* **Khía cạnh:** Nhóm màu sắc (Color family)
* **Value:** Count(Returns) / Count(Order_Items) (%)
* **Filter by:** Không có

**54. Tỷ lệ trả hàng do "Sai Form/Size" theo Thương hiệu nội bộ**
* **Chỉ số:** Số lượng đơn hoàn trả
* **Khía cạnh:** Tên dòng sản phẩm / Bộ sưu tập
* **Value:** % of Total Returns
* **Filter by:** Lý do trả = Wrong_size hoặc Fit_issue

**55. Chi phí chìm từ Hàng hoàn trả (Sunk Cost of Returns)**
* **Chỉ số:** Tổng giá trị hàng trả + Phí vận chuyển ngược (Reverse Logistics)
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** Sum(Refund Amount) + Sum(Return Shipping Fee)
* **Filter by:** Trạng thái = Returned

**56. Tương quan Giá trị đơn hàng và Khả năng hoàn trả (AOV vs Return Probability)**
* **Chỉ số:** Tỷ lệ hoàn trả
* **Khía cạnh:** Phân khúc giá trị đơn hàng (AOV Brackets)
* **Value:** Average(Return Rate)
* **Filter by:** Không có

**57. Tỷ lệ hàng lỗi theo Nhà cung cấp (Defective Rate by Supplier)**
* **Chỉ số:** Tỷ lệ hàng lỗi
* **Khía cạnh:** Tên nhà cung cấp / Xưởng sản xuất (Supplier)
* **Value:** Count(Returns có lý do Defective) / Total Supplied Quantity
* **Filter by:** Lý do trả = Defective

**58. Tốc độ xử lý hàng hoàn vào lại kho (Return-to-Shelf Time)**
* **Chỉ số:** Thời gian trung bình (Ngày)
* **Khía cạnh:** Khu vực kho (Warehouse Region)
* **Value:** Average(Days từ lúc nhận trả đến lúc Available)
* **Filter by:** Trạng thái tồn = Available

---

### Nhóm 6: Vận hành Giao vận & Fulfillment (Logistics & Delivery)
*Các biểu đồ chuyên sâu về thời gian xử lý đơn, giao nhận hàng hóa và chi phí vận chuyển.*

**11. Thời gian giao hàng trung bình vùng miền (Avg Delivery Time by Region)**
* **Chỉ số:** Thời gian giao hàng thực tế (Delivery time)
* **Khía cạnh:** Phân cấp lãnh thổ (Region/City)
* **Value:** Average(Delivery time)
* **Filter by:** Trạng thái = Delivered

**12. Xu hướng thời gian chuẩn bị hàng (Lead Time Trend)**
* **Chỉ số:** Thời gian chuẩn bị hàng (Lead time)
* **Khía cạnh:** Thời gian (Tuần/Tháng)
* **Value:** Average(Lead time)
* **Filter by:** Không có

**13. Bản đồ nhiệt cước phí vận chuyển (Shipping Fee Heatmap)**
* **Chỉ số:** Cước phí vận chuyển (Shipping fee)
* **Khía cạnh:** Phân cấp vùng miền (City/District)
* **Value:** Average(Shipping fee)
* **Filter by:** Không có

**14. Phân bổ Zip Code có lượng đơn cao nhất (Top Zip Codes)**
* **Chỉ số:** Số lượng đơn hàng
* **Khía cạnh:** Mã bưu điện khách hàng (Zip code)
* **Value:** Count(Orders)
* **Filter by:** Top 20 Zip codes có đơn nhiều nhất

**15. Thời gian giao hàng theo Thiết bị đặt (Delivery by Device)**
* **Chỉ số:** Thời gian giao hàng thực tế
* **KhKhía cạnh:** Thiết bị đặt hàng (Device type)
* **Value:** Average(Delivery time)
* **Filter by:** Không có

**16. Tổng cước phí vận chuyển theo tháng (Total Shipping Fee by Month)**
* **Chỉ số:** Cước phí vận chuyển
* **Khía cạnh:** Thời gian (Tháng/Quý)
* **Value:** Sum(Shipping fee)
* **Filter by:** Thời gian = YTD

**17. Tương quan Cước phí và Thời gian giao hàng (Cost vs. Speed)**
* **Chỉ số:** Cước phí & Thời gian giao hàng
* **Khía cạnh:** Phân cấp vùng miền (Region)
* **Value:** Avg(Shipping fee) trên trục Y, Avg(Delivery time) trên trục X
* **Filter by:** Không có

**18. Tỷ lệ đơn hàng giao trễ (Late Delivery Rate)**
* **Chỉ số:** Số lượng đơn hàng (phân loại trễ/đúng hạn)
* **Khía cạnh:** Phân cấp vùng miền
* **Value:** % Count(Orders) giao trễ
* **Filter by:** Delivery time > Expected Delivery Time

**19. Chi phí vận chuyển trung bình trên mỗi đơn (Shipping Cost per Order)**
* **Chỉ số:** Cước phí vận chuyển
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** Sum(Shipping fee) / Count(Orders)
* **Filter by:** Không có

**20. Lead time theo Thiết bị đặt hàng (Lead time by Device - Hành vi chốt đơn)**
* **Chỉ số:** Thời gian chuẩn bị hàng
* **Khía cạnh:** Thiết bị đặt hàng (Device type)
* **Value:** Average(Lead time)
* **Filter by:** Không có

---

### Nhóm 7: Lưu lượng Website, Phễu Web & Đa kênh (Traffic, Web Funnel & Omnichannel)
*Nhóm này gộp chung các chỉ số trên nền tảng kỹ thuật số, traffic đầu vào, phễu chuyển đổi UI/UX và trải nghiệm đa kênh (O2O).*

**31. Phễu chuyển đổi Website (Web Funnel Conversion)**
* **Chỉ số:** Lưu lượng truy cập (Sessions)
* **Khía cạnh:** Các bước phễu (Traffic -> Giỏ hàng -> Thanh toán)
* **Value:** Count(Sessions) cho mỗi bước
* **Filter by:** Chu kỳ rà soát = Tháng hiện tại

**32. Lưu lượng truy cập theo Nguồn (Traffic by Source)**
* **Chỉ số:** Lưu lượng truy cập (Sessions/Page views)
* **Khía cạnh:** Nguồn kéo Traffic Website (Traffic source)
* **Value:** Sum(Sessions) hoặc Sum(Page views)
* **Filter by:** Không có

**33. Tỷ lệ thoát trang theo Nguồn (Bounce Rate by Traffic Source)**
* **Chỉ số:** Tỷ lệ thoát trang (Bounce rate)
* **Khía cạnh:** Nguồn kéo Traffic Website
* **Value:** Average(Bounce rate)
* **Filter by:** Không có

**38. Thời lượng phiên Web theo Nguồn (Avg Session by Source)**
* **Chỉ số:** Thời lượng phiên Web (Avg Session duration)
* **Khía cạnh:** Nguồn kéo Traffic Website
* **Value:** Average(Session duration)
* **Filter by:** Không có

**39. Tương quan Thời lượng phiên và Bounce Rate (Engagement Scatter)**
* **Chỉ số:** Thời lượng phiên Web & Tỷ lệ thoát trang
* **Khía cạnh:** Nguồn Traffic
* **Value:** Avg(Session duration) & Avg(Bounce rate)
* **Filter by:** Không có

**40. Xu hướng Traffic theo thời gian rà soát (Traffic Trend over Snapshots)**
* **Chỉ số:** Lưu lượng truy cập (Sessions/Page views)
* **Khía cạnh:** Chu kỳ thời gian rà soát (Snapshot_date)
* **Value:** Sum(Sessions)
* **Filter by:** Thời gian = YTD

**93. Tỷ lệ thoát trang theo Nguồn truy cập (Bounce Rate by Traffic Source - Q4)**
* **Chỉ số:** Tỷ lệ thoát trang
* **Khía cạnh:** Nguồn truy cập (Organic_search, Paid_search, Social_media...)
* **Value:** Average(Bounce Rate)
* **Filter by:** Không có

**94. Chất lượng Traffic: Tỷ lệ chuyển đổi theo Nguồn (Conversion Rate by Source)**
* **Chỉ số:** Tỷ lệ mua hàng (Conversion Rate)
* **Khía cạnh:** Nguồn truy cập
* **Value:** Count(Orders) / Count(Sessions) (%)
* **Filter by:** Không có

**95. Hành trình Đa kênh (Omnichannel: O2O Tracking)**
* **Chỉ số:** Tỷ trọng đơn hàng Click & Collect (Mua Online, Lấy tại Store)
* **Khía cạnh:** Vùng địa lý / Cửa hàng
* **Value:** % of Total Orders
* **Filter by:** Delivery Type = Store Pickup

**96. Phân bổ Lượt tìm kiếm Nội bộ theo Từ khóa (Internal Search Terms)**
* **Chỉ số:** Khối lượng tìm kiếm trên Website
* **Khía cạnh:** Từ khóa tìm kiếm (Search Query)
* **Value:** Count(Searches)
* **Filter by:** Top 20 từ khóa (thường phản ánh xu hướng Trend)

**97. Tỷ lệ Khách hàng tạo tài khoản so với Mua tư cách khách (Guest vs Registered)**
* **Chỉ số:** Tổng số đơn hàng / Doanh thu
* **Khía cạnh:** Loại tài khoản lúc Checkout (Guest vs Registered)
* **Value:** % Distribution
* **Filter by:** Kênh = Website/App

**98. Tác động của Review/Hình ảnh đến Tỷ lệ chuyển đổi (Visual Content Impact)**
* **Chỉ số:** Tỷ lệ chuyển đổi vào giỏ hàng (Add-to-cart Rate)
* **Khía cạnh:** Cờ có Video/User-generated Content (Có/Không)
* **Value:** Average(Conversion Rate)
* **Filter by:** Màn hình chi tiết sản phẩm (PDP)

**99. Tốc độ chuyển đổi thiết bị chéo (Cross-device Purchase Journey)**
* **Chỉ số:** Số lượng hành trình
* **Khía cạnh:** Thiết bị chạm lần đầu -> Thiết bị chốt đơn (VD: Mobile -> Desktop)
* **Value:** Count(Journeys)
* **Filter by:** Đã đăng nhập tài khoản

**100. ROAS (Return on Ad Spend) theo Kênh quảng cáo thời trang**
* **Chỉ số:** Lợi tức chi tiêu quảng cáo
* **Khía cạnh:** Nguồn truy cập (Meta Ads, TikTok Ads, Google Shopping)
* **Value:** Sum(Revenue Attributed) / Sum(Ad Spend)
* **Filter by:** Paid Channels Only

---

### Nhóm 8: Chiến lược Khuyến mãi & Định giá (Promotions & Pricing Strategy)
*Nhóm này tập trung vào hiệu quả "đốt tiền" của Marketing, mã giảm giá, tính mùa vụ và chính sách giá.*

**41. Doanh thu tăng thêm theo Chiến dịch (Sales Lift by Campaign)**
* **Chỉ số:** Khối lượng đơn hàng tăng thêm (Sales Lift)
* **Khía cạnh:** Tên chiến dịch mùa vụ (Promo name)
* **Value:** Sum(Sales Lift)
* **Filter by:** Không có

**42. Ngân sách Khuyến mãi theo Kịch bản (Discount Burn by Promo Type)**
* **Chỉ số:** Tổng ngân sách đã "đốt" (Total Discount Amount)
* **Khía cạnh:** Kịch bản khuyến mãi (Promo type: % vs. Cố định)
* **Value:** Sum(Discount Amount)
* **Filter by:** Thời gian chiến dịch (Start - End date) = YTD

**43. Tỷ lệ sử dụng mã cộng dồn (Stackable Rate by Channel)**
* **Chỉ số:** Tỷ lệ dùng chung mã (Stackable flag impact)
* **Khía cạnh:** Kênh tung khuyến mãi (Promo channel)
* **Value:** Count(Orders with Stackable) / Total Promo Orders (%)
* **Filter by:** Có sử dụng Promo

**44. Ngân sách "Đốt" theo Danh mục SP (Discount by Product Category)**
* **Chỉ số:** Tổng ngân sách đã "đốt"
* **Khía cạnh:** Danh mục SP được áp dụng mã
* **Value:** Sum(Discount Amount)
* **Filter by:** Không có

**45. Tương quan Ngân sách Khuyến mãi và Sales Lift (Discount vs. Lift)**
* **Chỉ số:** Ngân sách giảm giá & Khối lượng đơn tăng thêm
* **Khía cạnh:** Tên chiến dịch mùa vụ
* **Value:** Sum(Discount) trục X, Sum(Sales Lift) trục Y
* **Filter by:** Các chiến dịch đã kết thúc

**46. Xu hướng sử dụng Promo theo thời gian thực (Promo Usage Timeline)**
* **Chỉ số:** Khối lượng đơn hàng áp mã
* **Khía cạnh:** Thời gian chiến dịch (Ngày trong khoảng Start - End date)
* **Value:** Count(Orders)
* **Filter by:** Trạng thái mã = Active

**47. Tỷ lệ đóng góp doanh thu của Promo (Promo Contribution to Revenue)**
* **Chỉ số:** Doanh thu có mã KM / Tổng doanh thu
* **Khía cạnh:** Tên chiến dịch mùa vụ
* **Value:** % of Total Revenue
* **Filter by:** Thời gian (Tháng)

**48. Hiệu suất các Kênh tung khuyến mãi (Promo Channel Performance)**
* **Chỉ số:** Khối lượng đơn hàng tăng thêm (Sales Lift)
* **Khía cạnh:** Kênh tung khuyến mãi (Promo channel)
* **Value:** Sum(Sales Lift)
* **Filter by:** Không có

**49. ROI của Khuyến mãi theo Mùa vụ (Promo ROI)**
* **Chỉ số:** Lợi tức (Sales Lift / Total Discount Amount)
* **Khía cạnh:** Tên chiến dịch mùa vụ
* **Value:** Ratio (Tỷ lệ)
* **Filter by:** Top 10 chiến dịch lớn nhất

**50. Phân bổ chiến dịch theo Danh mục (Campaigns by Category Coverage)**
* **Chỉ số:** Số lượng kịch bản khuyến mãi/Chiến dịch
* **Khía cạnh:** Danh mục SP được áp dụng mã
* **Value:** Distinct Count(Promo name)
* **Filter by:** Không có

**75. Độ nhạy cảm với khuyến mãi (Promo Adoption Rate - Q5)**
* **Chỉ số:** Tỷ lệ áp dụng khuyến mãi
* **Khía cạnh:** Thời gian (Tháng/Quý)
* **Value:** Count(Order_items có Promo) / Count(Total Order_items) (%)
* **Filter by:** Không có

**76. Doanh thu Hàng nguyên giá vs Hàng giảm giá (Full-price vs Markdown Sales)**
* **Chỉ số:** Doanh thu
* **Khía cạnh:** Thời gian (Tháng)
* **Value:** Sum(Revenue) (Stacked bar cho Full-price và Markdown)
* **Filter by:** Không có

**77. Mức độ "ăn mòn" biên lợi nhuận do Promo (Margin Erosion by Promo)**
* **Chỉ số:** Biên lợi nhuận gộp trước và sau Promo
* **Khía cạnh:** Tên chiến dịch
* **Value:** Avg(Base Margin) vs Avg(Effective Margin)
* **Filter by:** Có áp dụng Promo

**78. Tỷ lệ dùng Promo theo Phân khúc giá (Promo Usage by Price Tier)**
* **Chỉ số:** Tỷ lệ đơn có Promo
* **Khía cạnh:** Phân khúc giá trị sản phẩm (Thấp, Trung bình, Cao cấp)
* **Value:** % Orders using Promo
* **Filter by:** Không có

**79. Tác động của Miễn phí vận chuyển đến AOV (Freeship Impact on AOV)**
* **Chỉ số:** Giá trị trung bình đơn (AOV)
* **Khía cạnh:** Cờ Miễn phí vận chuyển (Freeship_Flag: Yes/No)
* **Value:** Average(Order Value)
* **Filter by:** Không có

**80. Phân bổ mức giảm giá hiệu quả (Optimal Markdown Depth Scatter)**
* **Chỉ số:** Tốc độ bán (Sales Velocity) & Mức giảm giá
* **Khía cạnh:** Sản phẩm
* **Value:** Avg(Markdown %) trục X, Avg(Units Sold per Day) trục Y
* **Filter by:** Trạng thái = Clearance (Xả hàng)

**81. Doanh thu tăng thêm từ Combo/Bundle (Bundle Sales Lift)**
* **Chỉ số:** Doanh thu
* **Khía cạnh:** Loại Promo (Single item discount vs Bundle discount)
* **Value:** Sum(Revenue)
* **Filter by:** Không có

**82. Tỷ lệ thoát giỏ hàng khi không có Mã giảm giá (Cart Abandonment without Promo)**
* **Chỉ số:** Tỷ lệ Abandonment
* **Khía cạnh:** Trạng thái áp mã tại Check-out (Có/Không)
* **Value:** Count(Abandoned Carts) / Total Checkouts Started
* **Filter by:** Không có

---

### Nhóm 9: Quản trị Sản phẩm, Tồn kho & Chuỗi cung ứng (Merchandising & Inventory)
*Nhóm này đi sâu vào quản trị SKU, độ lấp đầy, hao mòn tồn kho và tình trạng cạn/quá tải kho.*

**34. Độ lấp đầy kho theo Danh mục (Fill Rate by Inventory Category)**
* **Chỉ số:** Độ lấp đầy kho (Fill rate)
* **Khía cạnh:** Danh mục nhà kho (Inventory Category)
* **Value:** Average(Fill rate) (%)
* **Filter by:** Chu kỳ thời gian = Báo cáo mới nhất (Latest Snapshot)

**35. Tốc độ hao mòn tồn kho (Sell-Through Rate by Category)**
* **Chỉ số:** Tốc độ hao mòn tồn kho (Sell-through rate)
* **Khía cạnh:** Danh mục nhà kho (Inventory Category)
* **Value:** Average(Sell-through rate)
* **Filter by:** Chu kỳ rà soát (Tháng)

**36. Số ngày cạn kho theo Danh mục (Stockout Days)**
* **Chỉ số:** Số ngày cạn kho (Stockout days)
* **Khía cạnh:** Danh mục nhà kho / Sản phẩm
* **Value:** Sum(Stockout days)
* **Filter by:** Stockout_flag = True

**37. Cảnh báo quá tải tồn kho (Overstock Alerts)**
* **Chỉ số:** Lượng hàng tồn
* **Khía cạnh:** Danh mục nhà kho
* **Value:** Count(Sản phẩm)
* **Filter by:** Overstock_flag = True

**83. Tỷ lệ bán hàng (Sell-Through Rate - STR) theo Bộ sưu tập**
* **Chỉ số:** Tỷ lệ hàng đã bán
* **Khía cạnh:** Bộ sưu tập (Collection Season: Fall 25, Spring 26...)
* **Value:** Sum(Quantity Sold) / Sum(Initial Inventory) (%)
* **Filter by:** Thời gian = 4 tuần kể từ khi Launch

**84. Số tuần bán hàng tồn kho (Weeks of Supply - WOS) theo SKU**
* **Chỉ số:** Tuần tồn kho dự kiến
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Avg(Current Inventory Level / Avg Weekly Sales)
* **Filter by:** Trạng thái = Active

**85. Phân bổ Tồn kho theo Ma trận Size-Màu (Size-Color Inventory Heatmap)**
* **Chỉ số:** Số lượng tồn kho
* **Khía cạnh:** Kích thước (Cột) x Màu sắc (Hàng)
* **Value:** Sum(Stock Quantity)
* **Filter by:** Chọn 1 Style/Mẫu cụ thể (Filter)

**86. Mức độ phức tạp SKU theo Danh mục (SKU Proliferation)**
* **Chỉ số:** Số lượng SKU duy nhất
* **Khía cạnh:** Phân khúc / Danh mục
* **Value:** Distinct Count(SKU_ID)
* **Filter by:** Không có

**87. Tỷ lệ cạn kho theo Kích cỡ (Stockout Rate by Size)**
* **Chỉ số:** Số ngày cạn kho
* **Khía cạnh:** Kích thước (S, M, L, XL)
* **Value:** Count(Days with Stock = 0)
* **Filter by:** Các sản phẩm đang in-season (trong mùa)

**88. Chu kỳ cung ứng thời trang nhanh (Lead Time by Collection)**
* **Chỉ số:** Thời gian từ thiết kế đến lên kệ (Lead Time)
* **Khía cạnh:** Tên Bộ sưu tập
* **Value:** Average(Days)
* **Filter by:** Không có

**89. Tỷ lệ Hàng tồn kho quá hạn (Aged/Dead Inventory Rate)**
* **Chỉ số:** Tỷ trọng tồn kho > 90 ngày không phát sinh giao dịch
* **Khía cạnh:** Kho lưu trữ (Warehouse)
* **Value:** Sum(Aged Stock Value) / Sum(Total Stock Value)
* **Filter by:** Không có

**90. Xu hướng vòng đời bán hàng của 1 Style (Style Lifecycle Curve)**
* **Chỉ số:** Sản lượng bán ra hàng ngày
* **Khía cạnh:** Số ngày kể từ lúc Launch (Days since launch)
* **Value:** Sum(Quantity)
* **Filter by:** Tên Mẫu (Style Name)

**91. Hiệu suất các mặt hàng Basic vs Trendy (Core vs Fashion Trend Sales)**
* **Chỉ số:** Đóng góp doanh thu
* **Khía cạnh:** Phân loại vòng đời (Core/Basic vs Seasonal/Trendy)
* **Value:** % Total Revenue
* **Filter by:** Không có

**92. Tổn thất doanh thu do hết hàng (Lost Sales Value due to Stockout)**
* **Chỉ số:** Doanh thu ước tính bị mất
* **Khía cạnh:** Danh mục sản phẩm
* **Value:** Sum(Avg Daily Sales * Stockout Days * Price)
* **Filter by:** Stockout_flag = True