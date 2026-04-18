import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc các dataset cần thiết
returns = pd.read_csv(DATA_DIR + 'returns.csv')
orders = pd.read_csv(DATA_DIR + 'orders.csv')
order_items = pd.read_csv(DATA_DIR + 'order_items.csv')
products = pd.read_csv(DATA_DIR + 'products.csv')
customers = pd.read_csv(DATA_DIR + 'customers.csv')
shipments = pd.read_csv(DATA_DIR + 'shipments.csv')
reviews = pd.read_csv(DATA_DIR + 'reviews.csv')
payments = pd.read_csv(DATA_DIR + 'payments.csv')
geography = pd.read_csv(DATA_DIR + 'geography.csv')

# ==============================================================================
# 23. Lý do trả hàng phổ biến (Top Return Reasons)
# ==============================================================================
plt.figure(figsize=(10, 6))
reason_counts = returns['return_reason'].value_counts()
reason_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('23. Top Return Reasons')
plt.xlabel('Return Reason')
plt.ylabel('Number of Returns')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 25. Tỷ lệ trả hàng theo Nguồn khách (Return Rate by Acquisition Channel)
# ==============================================================================
orders_customers = orders.merge(customers[['customer_id', 'acquisition_channel']], on='customer_id', how='left')
total_orders_by_channel = orders_customers.groupby('acquisition_channel')['order_id'].nunique()

returned_orders = returns['order_id'].unique()
orders_customers['is_returned'] = orders_customers['order_id'].isin(returned_orders)
returned_orders_by_channel = orders_customers[orders_customers['is_returned']].groupby('acquisition_channel')['order_id'].nunique()

return_rate_channel = (returned_orders_by_channel / total_orders_by_channel * 100).fillna(0).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
return_rate_channel.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('25. Return Rate by Acquisition Channel')
plt.xlabel('Acquisition Channel')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 27. Tương quan Điểm đánh giá và Tỷ lệ hoàn trả (Satisfaction vs. Returns)
# ==============================================================================
reviews_products = reviews.merge(products[['product_id', 'category']], on='product_id', how='left')
avg_rating_cat = reviews_products.groupby('category')['rating'].mean()

oi_products = order_items.merge(products[['product_id', 'category']], on='product_id', how='left')
qty_by_cat = oi_products.groupby('category')['quantity'].sum()

ret_products = returns.merge(products[['product_id', 'category']], on='product_id', how='left')
ret_qty_by_cat = ret_products.groupby('category')['return_quantity'].sum()

return_rate_cat = (ret_qty_by_cat / qty_by_cat * 100).fillna(0)
df_corr = pd.DataFrame({'Avg Rating': avg_rating_cat, 'Return Rate (%)': return_rate_cat}).dropna()

fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.bar(df_corr.index, df_corr['Return Rate (%)'], color='orange', alpha=0.6, label='Return Rate (%)')
ax2.plot(df_corr.index, df_corr['Avg Rating'], color='blue', marker='o', linewidth=2, label='Avg Rating')

ax1.set_xlabel('Category')
ax1.set_ylabel('Return Rate (%)', color='orange')
ax2.set_ylabel('Average Rating', color='blue')
plt.title('27. Satisfaction vs. Returns by Category')
fig.tight_layout()
plt.show()

# ==============================================================================
# 29. Danh mục sản phẩm bị hoàn trả nhiều nhất (Highest Return Categories)
# ==============================================================================
plt.figure(figsize=(10, 6))
return_rate_cat.sort_values(ascending=False).plot(kind='bar', color='salmon', edgecolor='black')
plt.title('29. Highest Return Categories')
plt.xlabel('Category')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================================================================
# 51. Phân tích rủi ro kích cỡ (Sizing Risk Analysis - Q9)
# ==============================================================================
oi_size = order_items.merge(products[['product_id', 'size']], on='product_id', how='left')
oi_size_cnt = oi_size['size'].value_counts()

ret_size = returns.merge(products[['product_id', 'size']], on='product_id', how='left')
ret_size_cnt = ret_size['size'].value_counts()

size_return_rate = (ret_size_cnt / oi_size_cnt * 100).dropna().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
size_return_rate.plot(kind='bar', color='purple', edgecolor='black')
plt.title('51. Sizing Risk Analysis (Return Rate by Size)')
plt.xlabel('Size')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================================================================
# 52. Phân bổ lý do trả hàng theo Danh mục (Return Reasons by Category - Q3)
# ==============================================================================
streetwear_returns = ret_products[ret_products['category'] == 'Streetwear']
streetwear_reason_counts = streetwear_returns['return_reason'].value_counts()

plt.figure(figsize=(10, 6))
streetwear_reason_counts.plot(kind='bar', color='gold', edgecolor='black')
plt.title('52. Return Reasons for Streetwear')
plt.xlabel('Return Reason')
plt.ylabel('Number of Returns')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 53. Tỷ lệ hoàn trả theo Màu sắc (Color Return Rate)
# ==============================================================================
oi_color = order_items.merge(products[['product_id', 'color']], on='product_id', how='left')
oi_color_cnt = oi_color['color'].value_counts()

ret_color = returns.merge(products[['product_id', 'color']], on='product_id', how='left')
ret_color_cnt = ret_color['color'].value_counts()

color_return_rate = (ret_color_cnt / oi_color_cnt * 100).dropna().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
color_return_rate.plot(kind='bar', color='teal', edgecolor='black')
plt.title('53. Return Rate by Color')
plt.xlabel('Color')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 54. Tỷ lệ trả hàng do "Sai Form/Size" theo Thương hiệu nội bộ
# ==============================================================================
wrong_size_returns = ret_products[ret_products['return_reason'].isin(['wrong_size', 'fit_issue'])]
wrong_size_segment_counts = wrong_size_returns['segment'].value_counts()

wrong_size_segment_pct = (wrong_size_segment_counts / wrong_size_segment_counts.sum() * 100)

plt.figure(figsize=(10, 6))
wrong_size_segment_pct.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='Set3')
plt.title('54. % Wrong Size Returns by Segment')
plt.ylabel('')
plt.tight_layout()
plt.show()

# ==============================================================================
# 55. Chi phí chìm từ Hàng hoàn trả (Sunk Cost of Returns)
# ==============================================================================
returns['return_date'] = pd.to_datetime(returns['return_date'])
returns['year_month'] = returns['return_date'].dt.to_period('M').dt.to_timestamp()

ret_ship = returns.merge(shipments[['order_id', 'shipping_fee']], on='order_id', how='left')
ret_ship['sunk_cost'] = ret_ship['refund_amount'] + ret_ship['shipping_fee'].fillna(0)

sunk_cost_monthly = ret_ship.groupby('year_month')['sunk_cost'].sum()

plt.figure(figsize=(12, 6))
sunk_cost_monthly.plot(kind='line', color='red', linewidth=2, marker='o')
plt.title('55. Monthly Sunk Cost of Returns')
plt.xlabel('Month')
plt.ylabel('Total Sunk Cost')
plt.grid(True)
plt.tight_layout()
plt.show()

# ==============================================================================
# 56. Tương quan Giá trị đơn hàng và Khả năng hoàn trả (AOV vs Return Probability)
# ==============================================================================
order_values = payments.groupby('order_id')['payment_value'].sum().reset_index()
order_values['is_returned'] = order_values['order_id'].isin(returns['order_id'])

bins = [0, 5000, 10000, 20000, 50000, 100000, np.inf]
labels = ['<5k', '5k-10k', '10k-20k', '20k-50k', '50k-100k', '>100k']
order_values['AOV_Bracket'] = pd.cut(order_values['payment_value'], bins=bins, labels=labels)

aov_return_rate = order_values.groupby('AOV_Bracket')['is_returned'].mean() * 100

plt.figure(figsize=(10, 6))
aov_return_rate.plot(kind='bar', color='mediumseagreen', edgecolor='black')
plt.title('56. Return Probability by AOV Bracket')
plt.xlabel('AOV Bracket')
plt.ylabel('Return Probability (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 57. Tỷ lệ hàng lỗi theo Nhà cung cấp (Defective Rate by Supplier proxy)
# ==============================================================================
# Trích xuất từ đầu tiên của product_name làm định danh cho Brand/Supplier
products['brand'] = products['product_name'].apply(lambda x: str(x).split()[0] if pd.notnull(x) else 'Unknown')

oi_brand = order_items.merge(products[['product_id', 'brand']], on='product_id', how='left')
oi_brand_qty = oi_brand.groupby('brand')['quantity'].sum()

ret_brand = returns.merge(products[['product_id', 'brand']], on='product_id', how='left')
defective_returns = ret_brand[ret_brand['return_reason'] == 'defective']
defective_brand_qty = defective_returns.groupby('brand')['return_quantity'].sum()

defective_rate_brand = (defective_brand_qty / oi_brand_qty * 100).fillna(0).sort_values(ascending=False)

plt.figure(figsize=(12, 6))
defective_rate_brand.plot(kind='bar', color='darkorange', edgecolor='black')
plt.title('57. Defective Rate by Brand (Supplier Proxy)')
plt.xlabel('Brand')
plt.ylabel('Defective Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================================================================
# 58. Tốc độ xử lý hàng hoàn vào lại kho (Return-to-Shelf Time)
# ==============================================================================
# Sử dụng khoảng thời gian từ delivery_date tới return_date làm proxy cho Return Processing Time
ship_ret = returns[['order_id', 'return_date']].drop_duplicates().merge(shipments[['order_id', 'delivery_date']], on='order_id', how='inner')

ship_ret['return_date'] = pd.to_datetime(ship_ret['return_date'])
ship_ret['delivery_date'] = pd.to_datetime(ship_ret['delivery_date'])
ship_ret['return_days'] = (ship_ret['return_date'] - ship_ret['delivery_date']).dt.days

# Lọc bỏ các giá trị âm (bất thường)
ship_ret = ship_ret[ship_ret['return_days'] >= 0]

order_region = orders[['order_id', 'zip']].merge(geography[['zip', 'region']], on='zip', how='left')
ship_ret_region = ship_ret.merge(order_region[['order_id', 'region']], on='order_id', how='left')

avg_return_time = ship_ret_region.groupby('region')['return_days'].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_return_time.plot(kind='barh', color='cornflowerblue', edgecolor='black')
plt.title('58. Avg Return Processing Time by Region')
plt.xlabel('Average Days (Delivery to Return)')
plt.ylabel('Region')
plt.tight_layout()
plt.show()