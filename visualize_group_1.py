import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc dữ liệu
orders = pd.read_csv(DATA_DIR + 'orders.csv')
order_items = pd.read_csv(DATA_DIR + 'order_items.csv')
products = pd.read_csv(DATA_DIR + 'products.csv')
payments = pd.read_csv(DATA_DIR + 'payments.csv')
sales = pd.read_csv(DATA_DIR + 'sales.csv')
geography = pd.read_csv(DATA_DIR + 'geography.csv')

# Tiền xử lý kiểu thời gian
orders['order_date'] = pd.to_datetime(orders['order_date'])
sales['Date'] = pd.to_datetime(sales['Date'])

max_date_orders = orders['order_date'].max()
max_year_orders = max_date_orders.year
max_month_orders = max_date_orders.month

# 1. Xu hướng doanh thu tổng quan (Revenue Trend)
df1 = orders[orders['order_status'].isin(['delivered', 'completed'])].merge(payments, on='order_id', how='inner')
df1['year_month'] = df1['order_date'].dt.to_period('M')
trend_df = df1.groupby('year_month')['payment_value'].sum().reset_index()
trend_df['year_month'] = trend_df['year_month'].dt.to_timestamp()

plt.figure(figsize=(14, 6))
plt.plot(trend_df['year_month'], trend_df['payment_value'], color='royalblue', linestyle='-')
plt.title('1. Xu Hướng Doanh Thu Tổng Quan (Theo Tháng)', fontsize=14, fontweight='bold')
plt.xlabel('Thời Gian (Năm-Tháng)')
plt.ylabel('Tổng Doanh Thu')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 2. Cơ cấu doanh thu theo Danh mục (Revenue by Category) - YTD
df2_orders = orders[orders['order_date'].dt.year == max_year_orders]
df2 = df2_orders.merge(order_items, on='order_id').merge(products, on='product_id')
df2['item_revenue'] = df2['quantity'] * df2['unit_price']
cat_rev = df2.groupby('category')['item_revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(cat_rev, labels=cat_rev.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title(f'2. Cơ Cấu Doanh Thu Theo Danh Mục (YTD - {max_year_orders})', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 3. Số lượng đơn hàng theo Trạng thái (Tháng hiện tại)
df3 = orders[(orders['order_date'].dt.year == max_year_orders) & (orders['order_date'].dt.month == max_month_orders)]
status_counts = df3['order_status'].value_counts()

plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar', color='mediumaquamarine', edgecolor='black')
plt.title(f'3. Số Lượng Đơn Hàng Theo Trạng Thái ({max_month_orders}/{max_year_orders})', fontsize=14, fontweight='bold')
plt.xlabel('Trạng Thái Đơn Hàng')
plt.ylabel('Số Lượng Đơn Hàng')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(status_counts):
    plt.text(i, v + (v*0.02), str(v), ha='center', va='bottom')
plt.tight_layout()
plt.show()

# 4. Giá trị trung bình đơn hàng theo Phân khúc (AOV by Segment)
df4 = order_items.merge(products, on='product_id')
df4['item_revenue'] = df4['quantity'] * df4['unit_price']
seg_rev = df4.groupby('segment')['item_revenue'].sum()
seg_orders = df4.groupby('segment')['order_id'].nunique()
aov_seg = (seg_rev / seg_orders).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
aov_seg.plot(kind='bar', color='coral', edgecolor='black')
plt.title('4. Giá Trị Trung Bình Đơn Hàng (AOV) Theo Phân Khúc', fontsize=14, fontweight='bold')
plt.xlabel('Phân Khúc Sản Phẩm (Segment)')
plt.ylabel('AOV')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 5. Sản lượng bán ra hàng ngày (Last 30 Days)
start_date_30 = max_date_orders - pd.Timedelta(days=30)
df5_orders = orders[orders['order_date'] > start_date_30]
df5 = df5_orders.merge(order_items, on='order_id')
daily_qty = df5.groupby('order_date')['quantity'].sum().reset_index()

plt.figure(figsize=(14, 6))
plt.plot(daily_qty['order_date'], daily_qty['quantity'], marker='o', color='forestgreen', linestyle='-')
plt.title('5. Sản Lượng Bán Ra Hàng Ngày (30 Ngày Gần Nhất)', fontsize=14, fontweight='bold')
plt.xlabel('Ngày Đặt Hàng')
plt.ylabel('Sản Lượng (Quantity)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 8. Top 10 Sản phẩm bán chạy nhất (Top 10 Products)
df8 = order_items.merge(products, on='product_id')
top10_products = df8.groupby('product_name')['quantity'].sum().nlargest(10).sort_values(ascending=True)

plt.figure(figsize=(10, 6))
top10_products.plot(kind='barh', color='plum', edgecolor='black')
plt.title('8. Top 10 Sản Phẩm Bán Chạy Nhất', fontsize=14, fontweight='bold')
plt.xlabel('Tổng Số Lượng Bán Ra (Quantity)')
plt.ylabel('Tên Sản Phẩm')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 9. Tương quan Số lượng đơn và AOV (Orders vs. AOV Scatter)
df9_orders = orders[orders['order_status'].isin(['delivered', 'completed'])]
df9 = df9_orders.merge(order_items, on='order_id').merge(products, on='product_id')
df9['item_revenue'] = df9['quantity'] * df9['unit_price']
cat_rev_9 = df9.groupby('category')['item_revenue'].sum()
cat_orders_9 = df9.groupby('category')['order_id'].nunique()
cat_aov_9 = cat_rev_9 / cat_orders_9

plt.figure(figsize=(10, 6))
plt.scatter(cat_orders_9, cat_aov_9, color='darkorange', s=150, edgecolor='black', alpha=0.8)
for i, category in enumerate(cat_orders_9.index):
    plt.annotate(category, (cat_orders_9.iloc[i], cat_aov_9.iloc[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')
plt.title('9. Tương Quan Số Lượng Đơn Hàng và AOV Theo Danh Mục', fontsize=14, fontweight='bold')
plt.xlabel('Số Lượng Đơn Hàng (Orders Count)')
plt.ylabel('Giá Trị Trung Bình Đơn (AOV)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 10. So sánh Doanh thu cùng kỳ năm trước (YoY Revenue Comparison)
sales['year'] = sales['Date'].dt.year
sales['month'] = sales['Date'].dt.month
max_sales_year = sales['year'].max()

sales_ty = sales[sales['year'] == max_sales_year].groupby('month')['Revenue'].sum()
sales_ly = sales[sales['year'] == (max_sales_year - 1)].groupby('month')['Revenue'].sum()

df10 = pd.DataFrame({'Năm Nay': sales_ty, 'Năm Trước': sales_ly}).fillna(0)

df10.plot(kind='bar', figsize=(12, 6), color=['cornflowerblue', 'lightslategray'], edgecolor='black')
plt.title(f'10. So Sánh Doanh Thu Theo Tháng (YoY: {max_sales_year} vs {max_sales_year - 1})', fontsize=14, fontweight='bold')
plt.xlabel('Tháng')
plt.ylabel('Doanh Thu (Revenue)')
plt.xticks(rotation=0)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 70. Đóng góp Doanh thu theo Vùng lãnh thổ (Geographic Revenue)
df70 = orders.merge(payments, on='order_id').merge(geography, on='zip')
geo_rev = df70.groupby('region')['payment_value'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
geo_rev.plot(kind='bar', color='indianred', edgecolor='black')
plt.title('70. Đóng Góp Doanh Thu Theo Vùng Lãnh Thổ', fontsize=14, fontweight='bold')
plt.xlabel('Vùng Địa Lý (Region)')
plt.ylabel('Tổng Doanh Thu')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()