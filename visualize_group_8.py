import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc các file dữ liệu cần thiết
try:
    df_orders = pd.read_csv(DATA_DIR + 'orders.csv')
    df_items = pd.read_csv(DATA_DIR + 'order_items.csv')
    df_promo = pd.read_csv(DATA_DIR + 'promotions.csv')
    df_prod = pd.read_csv(DATA_DIR + 'products.csv')
    df_ship = pd.read_csv(DATA_DIR + 'shipments.csv')
except FileNotFoundError:
    print("Vui lòng đảm bảo các file CSV nằm trong thư mục 'dataset/'")

# Xử lý kiểu dữ liệu ngày tháng
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
df_promo['start_date'] = pd.to_datetime(df_promo['start_date'])
df_promo['end_date'] = pd.to_datetime(df_promo['end_date'])

# Tạo bảng dữ liệu tổng hợp (Merge)
df_merged = df_items.merge(df_orders, on='order_id', how='left')
df_merged = df_merged.merge(df_promo, on='promo_id', how='left')
df_merged = df_merged.merge(df_prod, on='product_id', how='left')

# Tạo thêm các cột tính toán cơ bản
df_merged['item_revenue'] = df_merged['quantity'] * df_merged['unit_price']
df_merged['has_promo'] = df_merged['promo_id'].notnull()
df_merged['month_year'] = df_merged['order_date'].dt.to_period('M')


# ==============================================================================
# 41. Doanh thu tăng thêm theo Chiến dịch (Sales Lift by Campaign)
# Chỉ số: Khối lượng đơn hàng tăng thêm (Proxy: Số lượng đơn hàng của chiến dịch)
# Khía cạnh: Tên chiến dịch mùa vụ (promo_name)
# ==============================================================================
req_41 = df_merged[df_merged['has_promo']].groupby('promo_name')['order_id'].nunique().sort_values(ascending=False).head(15)

plt.figure(figsize=(12, 6))
req_41.plot(kind='bar', color='skyblue')
plt.title('41. Khối lượng Đơn hàng theo Chiến dịch Khuyến mãi (Top 15)')
plt.xlabel('Tên Chiến dịch (Promo Name)')
plt.ylabel('Số lượng Đơn hàng (Sales Lift proxy)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ==============================================================================
# 42. Ngân sách Khuyến mãi theo Kịch bản (Discount Burn by Promo Type)
# Chỉ số: Tổng ngân sách đã "đốt" (Total Discount Amount)
# Khía cạnh: Kịch bản khuyến mãi (Promo type)
# Filter: YTD (Lấy dữ liệu của năm cuối cùng trong tập dữ liệu)
# ==============================================================================
max_year = df_merged['order_date'].dt.year.max()
df_ytd = df_merged[df_merged['order_date'].dt.year == max_year]
req_42 = df_ytd[df_ytd['has_promo']].groupby('promo_type')['discount_amount'].sum()

plt.figure(figsize=(8, 6))
req_42.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title(f'42. Ngân sách "Đốt" theo Loại Khuyến mãi (YTD {max_year})')
plt.ylabel('')
plt.tight_layout()
plt.show()


# ==============================================================================
# 43. Tỷ lệ sử dụng mã cộng dồn (Stackable Rate by Channel)
# Chỉ số: Tỷ lệ dùng chung mã
# Khía cạnh: Kênh tung khuyến mãi
# ==============================================================================
df_promo_orders = df_merged[df_merged['has_promo']]
req_43 = df_promo_orders.groupby('promo_channel')['stackable_flag'].mean() * 100

plt.figure(figsize=(10, 6))
req_43.sort_values().plot(kind='barh', color='lightgreen')
plt.title('43. Tỷ lệ Đơn hàng Khuyến mãi có sử dụng Mã Cộng dồn theo Kênh')
plt.xlabel('Tỷ lệ % (Stackable Rate)')
plt.ylabel('Kênh phân phối Khuyến mãi (Promo Channel)')
plt.tight_layout()
plt.show()


# ==============================================================================
# 44. Ngân sách "Đốt" theo Danh mục SP (Discount by Product Category)
# Chỉ số: Tổng ngân sách đã "đốt" (Sum Discount Amount)
# Khía cạnh: Danh mục SP
# ==============================================================================
req_44 = df_merged[df_merged['has_promo']].groupby('category')['discount_amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
req_44.plot(kind='bar', color='coral')
plt.title('44. Ngân sách Giảm giá theo Danh mục Sản phẩm')
plt.xlabel('Danh mục Sản phẩm (Category)')
plt.ylabel('Tổng giá trị giảm giá (Discount Amount)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 45. Tương quan Ngân sách Khuyến mãi và Sales Lift (Discount vs. Lift)
# Trục X: Sum(Discount), Trục Y: Sum(Sales Lift - Volume Orders)
# ==============================================================================
max_date = df_orders['order_date'].max()
ended_promos = df_promo[df_promo['end_date'] < max_date]['promo_name'].tolist()

df_ended = df_merged[df_merged['promo_name'].isin(ended_promos)]
req_45 = df_ended.groupby('promo_name').agg(
    total_discount=('discount_amount', 'sum'),
    sales_lift=('order_id', 'nunique')
).reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(req_45['total_discount'], req_45['sales_lift'], alpha=0.7, color='purple')
for i, txt in enumerate(req_45['promo_name']):
    if req_45['total_discount'][i] > req_45['total_discount'].quantile(0.8) or req_45['sales_lift'][i] > req_45['sales_lift'].quantile(0.8):
        plt.annotate(txt, (req_45['total_discount'][i], req_45['sales_lift'][i]), fontsize=8)
plt.title('45. Tương quan giữa Ngân sách Khuyến mãi và Khối lượng Đơn hàng (Sales Lift)')
plt.xlabel('Tổng Ngân sách Giảm giá (Discount Amount)')
plt.ylabel('Khối lượng Đơn hàng Tăng thêm (Orders)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==============================================================================
# 46. Xu hướng sử dụng Promo theo thời gian thực (Promo Usage Timeline)
# Chỉ số: Khối lượng đơn hàng áp mã theo ngày
# ==============================================================================
req_46 = df_merged[df_merged['has_promo']].groupby('order_date')['order_id'].nunique()

plt.figure(figsize=(14, 6))
req_46.plot(kind='line', color='darkorange', linewidth=1.5)
plt.title('46. Xu hướng Sử dụng Khuyến mãi theo Thời gian')
plt.xlabel('Ngày Đặt hàng')
plt.ylabel('Số lượng Đơn hàng áp mã')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==============================================================================
# 47. Tỷ lệ đóng góp doanh thu của Promo (Promo Contribution to Revenue)
# ==============================================================================
monthly_total_rev = df_merged.groupby('month_year')['item_revenue'].sum()
monthly_promo_rev = df_merged[df_merged['has_promo']].groupby('month_year')['item_revenue'].sum()

req_47 = (monthly_promo_rev / monthly_total_rev * 100).fillna(0)

plt.figure(figsize=(14, 6))
req_47.plot(kind='bar', color='teal')
plt.title('47. Tỷ lệ Đóng góp Doanh thu của Đơn hàng Khuyến mãi theo Tháng')
plt.xlabel('Tháng')
plt.ylabel('Tỷ lệ Đóng góp (%)')
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.show()


# ==============================================================================
# 48. Hiệu suất các Kênh tung khuyến mãi (Promo Channel Performance)
# ==============================================================================
req_48 = df_merged[df_merged['has_promo']].groupby('promo_channel')['order_id'].nunique().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
req_48.plot(kind='bar', color='dodgerblue')
plt.title('48. Khối lượng Đơn hàng Khuyến mãi theo Kênh phân phối')
plt.xlabel('Kênh Khuyến mãi (Promo Channel)')
plt.ylabel('Khối lượng Đơn hàng (Sales Lift)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 49. ROI của Khuyến mãi theo Mùa vụ (Promo ROI)
# Chỉ số: Revenue / Total Discount Amount cho Top 10 chiến dịch
# ==============================================================================
req_49 = df_merged[df_merged['has_promo']].groupby('promo_name').agg(
    total_revenue=('item_revenue', 'sum'),
    total_discount=('discount_amount', 'sum')
)
req_49['ROI'] = req_49['total_revenue'] / req_49['total_discount']
req_49 = req_49.sort_values('total_revenue', ascending=False).head(10)

plt.figure(figsize=(12, 6))
req_49['ROI'].sort_values().plot(kind='barh', color='mediumseagreen')
plt.title('49. ROI Khuyến mãi (Revenue / Discount) - Top 10 Chiến dịch Lớn nhất')
plt.xlabel('Tỷ lệ Lợi tức (ROI Ratio)')
plt.ylabel('Tên Chiến dịch')
plt.tight_layout()
plt.show()


# ==============================================================================
# 50. Phân bổ chiến dịch theo Danh mục (Campaigns by Category Coverage)
# ==============================================================================
df_promo['applicable_category_filled'] = df_promo['applicable_category'].fillna('Áp dụng Toàn bộ (All)')
req_50 = df_promo.groupby('applicable_category_filled')['promo_id'].nunique().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
req_50.plot(kind='bar', color='salmon')
plt.title('50. Số lượng Chiến dịch Khuyến mãi theo Danh mục Áp dụng')
plt.xlabel('Danh mục Áp dụng')
plt.ylabel('Số lượng Kịch bản/Chiến dịch')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 75. Độ nhạy cảm với khuyến mãi (Promo Adoption Rate - Q5)
# Chỉ số: Tỷ lệ áp dụng khuyến mãi = Có Promo / Tổng Order Items theo Tháng
# ==============================================================================
req_75 = df_merged.groupby('month_year')['has_promo'].mean() * 100

plt.figure(figsize=(14, 6))
req_75.plot(kind='line', color='crimson', marker='o', markersize=3)
plt.title('75. Độ nhạy cảm với Khuyến mãi (Promo Adoption Rate) theo Tháng')
plt.xlabel('Tháng')
plt.ylabel('Tỷ lệ áp dụng Khuyến mãi (%)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==============================================================================
# 76. Doanh thu Hàng nguyên giá vs Hàng giảm giá (Full-price vs Markdown Sales)
# ==============================================================================
req_76 = df_merged.groupby(['month_year', 'has_promo'])['item_revenue'].sum().unstack()
req_76.columns = ['Full-price (Nguyên giá)', 'Markdown (Giảm giá)']

plt.figure(figsize=(14, 6))
req_76.plot(kind='bar', stacked=True, color=['#4daf4a', '#e41a1c'], ax=plt.gca())
plt.title('76. Cơ cấu Doanh thu Nguyên giá và Giảm giá theo Tháng')
plt.xlabel('Tháng')
plt.ylabel('Doanh thu (Revenue)')
plt.xticks(rotation=90, fontsize=8)
plt.legend(title='Loại Doanh thu')
plt.tight_layout()
plt.show()


# ==============================================================================
# 77. Mức độ "ăn mòn" biên lợi nhuận do Promo (Margin Erosion by Promo)
# Base Margin = (price - cogs) / price
# Effective Margin = (unit_price - cogs) / unit_price
# ==============================================================================
promo_items = df_merged[df_merged['has_promo']].copy()
promo_items['base_margin'] = (promo_items['price'] - promo_items['cogs']) / promo_items['price']
promo_items['effective_margin'] = (promo_items['unit_price'] - promo_items['cogs']) / promo_items['unit_price']

req_77 = promo_items.groupby('promo_name')[['base_margin', 'effective_margin']].mean().sort_values('base_margin', ascending=False).head(15)

req_77.plot(kind='bar', figsize=(14, 6), color=['#377eb8', '#ff7f00'])
plt.title('77. Tác động của Khuyến mãi đến Biên Lợi nhuận Gộp (Top 15 Chiến dịch)')
plt.xlabel('Tên Chiến dịch')
plt.ylabel('Biên Lợi nhuận Trung bình (%)')
plt.legend(['Base Margin (Trước KM)', 'Effective Margin (Sau KM)'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ==============================================================================
# 78. Tỷ lệ dùng Promo theo Phân khúc giá (Promo Usage by Price Tier)
# ==============================================================================
df_merged['price_tier'] = pd.qcut(df_merged['price'], q=3, labels=['Thấp (Low)', 'Trung bình (Medium)', 'Cao cấp (High)'])
req_78 = df_merged.groupby('price_tier')['has_promo'].mean() * 100

plt.figure(figsize=(8, 6))
req_78.plot(kind='bar', color='goldenrod')
plt.title('78. Tỷ lệ Sử dụng Khuyến mãi theo Phân khúc Giá trị Sản phẩm')
plt.xlabel('Phân khúc Giá')
plt.ylabel('Tỷ lệ áp dụng Khuyến mãi (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 79. Tác động của Miễn phí vận chuyển đến AOV (Freeship Impact on AOV)
# ==============================================================================
order_totals = df_merged.groupby('order_id')['item_revenue'].sum().reset_index()
order_totals = order_totals.merge(df_ship[['order_id', 'shipping_fee']], on='order_id', how='left')
order_totals['freeship_flag'] = order_totals['shipping_fee'].fillna(-1).apply(lambda x: 'Có Freeship' if x == 0 else 'Không Freeship' if x > 0 else 'Chưa giao')

req_79 = order_totals[order_totals['freeship_flag'] != 'Chưa giao'].groupby('freeship_flag')['item_revenue'].mean()

plt.figure(figsize=(8, 6))
req_79.plot(kind='bar', color=['lightcoral', 'lightseagreen'])
plt.title('79. Tác động của Miễn phí Vận chuyển đến Giá trị Trung bình Đơn (AOV)')
plt.xlabel('Chính sách Vận chuyển')
plt.ylabel('Giá trị Trung bình Đơn hàng (AOV)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 80. Phân bổ mức giảm giá hiệu quả (Optimal Markdown Depth Scatter)
# Clearance proxy: Các sản phẩm có giảm giá (Discount > 0)
# Markdown % = discount_amount / (unit_price * quantity + discount_amount)
# ==============================================================================
clearance_items = df_merged[df_merged['discount_amount'] > 0].copy()
clearance_items['markdown_pct'] = clearance_items['discount_amount'] / (clearance_items['item_revenue'] + clearance_items['discount_amount'])

# Sales velocity: Tính số lượng bán chia cho khoảng thời gian xuất hiện của sản phẩm
velocity_df = clearance_items.groupby('product_id').agg(
    total_qty=('quantity', 'sum'),
    min_date=('order_date', 'min'),
    max_date=('order_date', 'max'),
    avg_markdown=('markdown_pct', 'mean')
).reset_index()

velocity_df['days_active'] = (velocity_df['max_date'] - velocity_df['min_date']).dt.days.clip(lower=1)
velocity_df['sales_velocity'] = velocity_df['total_qty'] / velocity_df['days_active']

plt.figure(figsize=(10, 6))
plt.scatter(velocity_df['avg_markdown'] * 100, velocity_df['sales_velocity'], alpha=0.6, color='brown')
plt.title('80. Tương quan giữa Mức Giảm giá (%) và Tốc độ Bán (Sales Velocity)')
plt.xlabel('Mức Giảm giá Trung bình (%)')
plt.ylabel('Tốc độ bán (Đơn vị / Ngày)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==============================================================================
# 81. Doanh thu tăng thêm từ Combo/Bundle (Bundle Sales Lift)
# Phân loại Bundle: Có sử dụng promo_id_2 (stackable)
# ==============================================================================
df_promo_only = df_merged[df_merged['has_promo']].copy()
df_promo_only['promo_type_agg'] = np.where(df_promo_only['promo_id_2'].notnull(), 'Bundle/Combo Discount', 'Single Item Discount')
req_81 = df_promo_only.groupby('promo_type_agg')['item_revenue'].sum()

plt.figure(figsize=(8, 6))
req_81.plot(kind='bar', color=['#984ea3', '#ff7f00'])
plt.title('81. Doanh thu đóng góp từ Khuyến mãi Đơn lẻ vs Bundle/Combo')
plt.xlabel('Loại Khuyến mãi Áp dụng')
plt.ylabel('Tổng Doanh thu (Revenue)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==============================================================================
# 82. Tỷ lệ thoát/Hủy đơn khi Không có Mã giảm giá (Cart Abandonment Proxy)
# Chỉ số: Tỷ lệ trạng thái Cancelled nhóm theo Việc có áp mã hay không
# ==============================================================================
order_promo_status = df_merged.groupby('order_id').agg(
    has_promo=('has_promo', 'max'),
    order_status=('order_status', 'first')
).reset_index()

abandonment_rates = order_promo_status.groupby('has_promo').apply(
    lambda x: (x['order_status'] == 'cancelled').sum() / len(x) * 100
)
abandonment_rates.index = ['Không Áp Mã (No Promo)', 'Có Áp Mã (With Promo)']

plt.figure(figsize=(8, 6))
abandonment_rates.plot(kind='bar', color=['gray', 'orange'])
plt.title('82. Tỷ lệ Hủy đơn (Proxy cho Abandonment) theo Trạng thái Áp mã')
plt.xlabel('Trạng thái Khuyến mãi tại Checkout')
plt.ylabel('Tỷ lệ Hủy Đơn (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()