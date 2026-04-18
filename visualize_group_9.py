import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc các file dữ liệu cần thiết
inventory = pd.read_csv(DATA_DIR + 'inventory.csv')
products = pd.read_csv(DATA_DIR + 'products.csv')
orders = pd.read_csv(DATA_DIR + 'orders.csv')
order_items = pd.read_csv(DATA_DIR + 'order_items.csv')

# Ép kiểu dữ liệu thời gian
inventory['snapshot_date'] = pd.to_datetime(inventory['snapshot_date'])
orders['order_date'] = pd.to_datetime(orders['order_date'])

# -----------------------------------------------------------------------------
# 34. Độ lấp đầy kho theo Danh mục (Fill Rate by Inventory Category)
# -----------------------------------------------------------------------------
latest_date = inventory['snapshot_date'].max()
inv_latest = inventory[inventory['snapshot_date'] == latest_date]
fill_rate_cat = inv_latest.groupby('category')['fill_rate'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(fill_rate_cat['category'], fill_rate_cat['fill_rate'] * 100, color='skyblue')
plt.title('34. Độ lấp đầy kho theo Danh mục (Latest Snapshot)')
plt.xlabel('Danh mục')
plt.ylabel('Độ lấp đầy kho trung bình (%)')
for i, v in enumerate(fill_rate_cat['fill_rate'] * 100):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 35. Tốc độ hao mòn tồn kho (Sell-Through Rate by Category)
# -----------------------------------------------------------------------------
inv_monthly = inventory.groupby(['snapshot_date', 'category'])['sell_through_rate'].mean().reset_index()
inv_monthly = inv_monthly.sort_values('snapshot_date')

plt.figure(figsize=(12, 6))
for cat in inv_monthly['category'].unique():
    subset = inv_monthly[inv_monthly['category'] == cat]
    plt.plot(subset['snapshot_date'], subset['sell_through_rate'], label=cat)

plt.title('35. Tốc độ hao mòn tồn kho (Sell-Through Rate) theo Tháng và Danh mục')
plt.xlabel('Thời gian (Tháng)')
plt.ylabel('Tốc độ hao mòn (Sell-Through Rate)')
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 36. Số ngày cạn kho theo Danh mục (Stockout Days)
# -----------------------------------------------------------------------------
stockout_data = inventory[inventory['stockout_flag'] == 1]
stockout_cat = stockout_data.groupby('category')['stockout_days'].sum().reset_index().sort_values('stockout_days', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(stockout_cat['category'], stockout_cat['stockout_days'], color='salmon')
plt.title('36. Tổng số ngày cạn kho theo Danh mục')
plt.xlabel('Danh mục')
plt.ylabel('Số ngày cạn kho')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 37. Cảnh báo quá tải tồn kho (Overstock Alerts)
# -----------------------------------------------------------------------------
overstock_data = inventory[inventory['overstock_flag'] == 1]
overstock_cat = overstock_data.groupby('category')['product_id'].count().reset_index().rename(columns={'product_id': 'product_count'}).sort_values('product_count', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(overstock_cat['category'], overstock_cat['product_count'], color='orange')
plt.title('37. Cảnh báo quá tải tồn kho theo Danh mục')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng sản phẩm quá tải')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 83. Tỷ lệ bán hàng (Sell-Through Rate - STR) theo Bộ sưu tập (Segment proxy)
# -----------------------------------------------------------------------------
first_snapshot = inventory.groupby('product_id')['snapshot_date'].min().reset_index()
inv_launch = pd.merge(inventory, first_snapshot, on=['product_id', 'snapshot_date'])
inv_launch['initial_inventory'] = inv_launch['stock_on_hand'] + inv_launch['units_sold']

str_segment = inv_launch.groupby('segment').apply(
    lambda x: (x['units_sold'].sum() / x['initial_inventory'].sum() * 100) if x['initial_inventory'].sum() > 0 else 0
).reset_index(name='str_pct').sort_values('str_pct', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(str_segment['segment'], str_segment['str_pct'], color='teal')
plt.title('83. Tỷ lệ bán hàng (STR) theo Phân khúc (4 tuần đầu ra mắt)')
plt.xlabel('Phân khúc (Segment)')
plt.ylabel('Sell-Through Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 84. Số tuần bán hàng tồn kho (Weeks of Supply - WOS) theo SKU/Danh mục
# -----------------------------------------------------------------------------
active_inv = inventory[inventory['stock_on_hand'] > 0].copy()
active_inv['wos'] = active_inv['days_of_supply'] / 7
wos_cat = active_inv.groupby('category')['wos'].mean().reset_index().sort_values('wos')

plt.figure(figsize=(10, 6))
plt.barh(wos_cat['category'], wos_cat['wos'], color='lightgreen')
plt.title('84. Số tuần bán hàng tồn kho (WOS) trung bình theo Danh mục')
plt.xlabel('Weeks of Supply (Tuần)')
plt.ylabel('Danh mục')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 85. Phân bổ Tồn kho theo Ma trận Size-Màu (Size-Color Inventory Heatmap)
# -----------------------------------------------------------------------------
inv_prod = pd.merge(inv_latest, products, on='product_id', suffixes=('', '_prod'))
top_style = products.groupby('product_name').size().idxmax()
style_data = inv_prod[inv_prod['product_name'] == top_style]

if style_data.empty:
    style_data = inv_prod[inv_prod['category'] == inv_prod['category'].iloc[0]]
    top_style = inv_prod['category'].iloc[0] + ' (Category Proxy)'

pivot_data = style_data.pivot_table(index='color', columns='size', values='stock_on_hand', aggfunc='sum', fill_value=0)

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_data, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title(f'85. Phân bổ Tồn kho theo Size-Màu (Mẫu: {top_style})')
plt.xlabel('Kích thước (Size)')
plt.ylabel('Màu sắc (Color)')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 86. Mức độ phức tạp SKU theo Danh mục (SKU Proliferation)
# -----------------------------------------------------------------------------
sku_counts = products.groupby('category')['product_id'].nunique().reset_index().rename(columns={'product_id': 'sku_count'})

plt.figure(figsize=(8, 8))
plt.pie(sku_counts['sku_count'], labels=sku_counts['category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('86. Mức độ phức tạp SKU theo Danh mục')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 87. Tỷ lệ cạn kho theo Kích cỡ (Stockout Rate by Size)
# -----------------------------------------------------------------------------
inv_sz = pd.merge(inventory, products[['product_id', 'size']], on='product_id', how='left')
inv_sz = inv_sz.dropna(subset=['size'])
sz_stockout = inv_sz.groupby('size')['stockout_days'].sum().reset_index().sort_values('stockout_days', ascending=False)

plt.figure(figsize=(8, 6))
plt.bar(sz_stockout['size'], sz_stockout['stockout_days'], color='crimson')
plt.title('87. Tổng số ngày cạn kho theo Kích cỡ')
plt.xlabel('Kích cỡ')
plt.ylabel('Số ngày cạn kho')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 88. Chu kỳ cung ứng thời trang nhanh (Lead Time by Collection)
# -----------------------------------------------------------------------------
categories = products['category'].unique()
np.random.seed(42)
mock_lead_times = {cat: np.random.randint(30, 90) for cat in categories}
lead_time_df = pd.DataFrame(list(mock_lead_times.items()), columns=['Category', 'Avg_Lead_Time_Days']).sort_values('Avg_Lead_Time_Days')

plt.figure(figsize=(10, 6))
plt.barh(lead_time_df['Category'], lead_time_df['Avg_Lead_Time_Days'], color='purple')
plt.title('88. Thời gian cung ứng (Lead Time) trung bình theo Danh mục (Dữ liệu mô phỏng)')
plt.xlabel('Số ngày')
plt.ylabel('Danh mục')
for index, value in enumerate(lead_time_df['Avg_Lead_Time_Days']):
    plt.text(value, index, str(value), va='center')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 89. Tỷ lệ Hàng tồn kho quá hạn (Aged/Dead Inventory Rate)
# -----------------------------------------------------------------------------
inv_latest['is_aged'] = inv_latest['days_of_supply'] > 90
inv_latest_val = pd.merge(inv_latest, products[['product_id', 'price']], on='product_id', how='left')
inv_latest_val['stock_value'] = inv_latest_val['stock_on_hand'] * inv_latest_val['price']

aged_val_by_cat = inv_latest_val.groupby('category').apply(
    lambda x: (x[x['is_aged']]['stock_value'].sum() / x['stock_value'].sum() * 100) if x['stock_value'].sum() > 0 else 0
).reset_index(name='aged_rate')

plt.figure(figsize=(10, 6))
plt.bar(aged_val_by_cat['category'], aged_val_by_cat['aged_rate'], color='grey')
plt.title('89. Tỷ lệ Giá trị Tồn kho quá hạn (>90 ngày) theo Danh mục')
plt.xlabel('Danh mục')
plt.ylabel('Tỷ lệ quá hạn (%)')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 90. Xu hướng vòng đời bán hàng của 1 Style (Style Lifecycle Curve)
# -----------------------------------------------------------------------------
top_product_id = order_items.groupby('product_id')['quantity'].sum().idxmax()
top_product_name = products.loc[products['product_id'] == top_product_id, 'product_name'].values[0]

oi_orders = pd.merge(order_items[order_items['product_id'] == top_product_id], orders[['order_id', 'order_date']], on='order_id')
min_date = oi_orders['order_date'].min()
oi_orders['days_since_launch'] = (oi_orders['order_date'] - min_date).dt.days

daily_sales = oi_orders.groupby('days_since_launch')['quantity'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(daily_sales['days_since_launch'], daily_sales['quantity'], color='darkblue', alpha=0.3, label='Doanh số thực tế')
if len(daily_sales) > 7:
    daily_sales['qty_ma'] = daily_sales['quantity'].rolling(window=7).mean()
    plt.plot(daily_sales['days_since_launch'], daily_sales['qty_ma'], color='red', linewidth=2, label='Đường trung bình 7 ngày')
plt.title(f'90. Xu hướng vòng đời bán hàng - Mẫu: {top_product_name}')
plt.xlabel('Số ngày kể từ lúc phát sinh đơn đầu tiên')
plt.ylabel('Sản lượng bán ra')
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 91. Hiệu suất các mặt hàng Basic vs Trendy (Core vs Fashion Trend Sales)
# -----------------------------------------------------------------------------
core_segments = ['Everyday', 'Standard']
products['lifecycle_type'] = products['segment'].apply(lambda x: 'Core/Basic' if x in core_segments else 'Seasonal/Trendy')

oi_prod = pd.merge(order_items, products[['product_id', 'lifecycle_type']], on='product_id')
oi_prod['revenue'] = oi_prod['quantity'] * oi_prod['unit_price']

rev_by_type = oi_prod.groupby('lifecycle_type')['revenue'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(rev_by_type['revenue'], labels=rev_by_type['lifecycle_type'], autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('91. Đóng góp doanh thu: Basic vs Trendy')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# 92. Tổn thất doanh thu do hết hàng (Lost Sales Value due to Stockout)
# -----------------------------------------------------------------------------
inv_prod_lost = pd.merge(inventory[inventory['stockout_flag'] == 1], products[['product_id', 'price']], on='product_id')
inv_prod_lost['avg_daily_sales'] = inv_prod_lost['units_sold'] / 30
inv_prod_lost['lost_revenue'] = inv_prod_lost['avg_daily_sales'] * inv_prod_lost['stockout_days'] * inv_prod_lost['price']

lost_by_cat = inv_prod_lost.groupby('category')['lost_revenue'].sum().reset_index().sort_values('lost_revenue', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(lost_by_cat['category'], lost_by_cat['lost_revenue'], color='darkred')
plt.title('92. Tổn thất doanh thu ước tính do hết hàng theo Danh mục')
plt.xlabel('Danh mục')
plt.ylabel('Doanh thu bị mất ước tính')
plt.tight_layout()
plt.show()