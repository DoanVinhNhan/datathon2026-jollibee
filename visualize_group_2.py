import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc các dữ liệu cần thiết
customers = pd.read_csv(DATA_DIR + 'customers.csv')
orders = pd.read_csv(DATA_DIR + 'orders.csv')
order_items = pd.read_csv(DATA_DIR + 'order_items.csv')
payments = pd.read_csv(DATA_DIR + 'payments.csv')
products = pd.read_csv(DATA_DIR + 'products.csv')
returns = pd.read_csv(DATA_DIR + 'returns.csv')

# --------------------------------------------------------------------------------
# 6. Tỷ trọng Phương thức thanh toán (Payment Method Breakdown)
# --------------------------------------------------------------------------------
req6 = payments.groupby('payment_method')['payment_value'].sum().reset_index()

plt.figure(figsize=(8, 6))
plt.pie(req6['payment_value'], labels=req6['payment_method'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title('6. Tỷ trọng Giá trị theo Phương thức thanh toán')
plt.show()

# --------------------------------------------------------------------------------
# 7. Doanh thu theo Phân khúc trả góp (Installment Revenue)
# --------------------------------------------------------------------------------
req7 = payments[payments['installments'] > 1].groupby('installments')['payment_value'].sum().reset_index()
req7['installments_str'] = req7['installments'].astype(str) + ' kỳ'

plt.figure(figsize=(8, 5))
plt.bar(req7['installments_str'], req7['payment_value'], color='skyblue')
plt.title('7. Doanh thu theo Phân khúc trả góp (Installments > 1)')
plt.xlabel('Kỳ hạn trả góp')
plt.ylabel('Tổng doanh thu (Payment Value)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --------------------------------------------------------------------------------
# 67. Biên lợi nhuận gộp theo Phân khúc SP (Gross Margin by Segment - Q2)
# --------------------------------------------------------------------------------
req67 = products.copy()
req67['gross_margin'] = (req67['price'] - req67['cogs']) / req67['price']
req67_agg = req67.groupby('segment')['gross_margin'].mean().reset_index().sort_values('gross_margin')

plt.figure(figsize=(10, 6))
plt.barh(req67_agg['segment'], req67_agg['gross_margin'], color='lightgreen')
plt.title('67. Biên lợi nhuận gộp trung bình theo Phân khúc SP')
plt.xlabel('Biên lợi nhuận gộp (%)')
plt.ylabel('Phân khúc (Segment)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# --------------------------------------------------------------------------------
# 68. Giá trị đơn hàng theo Kỳ hạn trả góp (AOV by Installment Terms - Q10)
# --------------------------------------------------------------------------------
req68 = payments.groupby('installments')['payment_value'].mean().reset_index()
req68['installments_str'] = req68['installments'].astype(str) + ' kỳ'

plt.figure(figsize=(8, 5))
plt.bar(req68['installments_str'], req68['payment_value'], color='coral')
plt.title('68. Giá trị đơn hàng trung bình (AOV) theo Kỳ hạn trả góp')
plt.xlabel('Kỳ hạn trả góp')
plt.ylabel('Giá trị thanh toán trung bình')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --------------------------------------------------------------------------------
# 69. Tỷ lệ hủy đơn theo Phương thức thanh toán (Cancellations by Payment - Q8)
# --------------------------------------------------------------------------------
req69_cancelled = orders[orders['order_status'] == 'cancelled'].groupby('payment_method').size().reset_index(name='cancelled_count')
req69_total = orders.groupby('payment_method').size().reset_index(name='total_count')
req69 = pd.merge(req69_cancelled, req69_total, on='payment_method')
req69['cancel_rate'] = (req69['cancelled_count'] / req69['total_count']) * 100

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(req69['payment_method'], req69['cancelled_count'], color='salmon', alpha=0.8, label='Số lượng đơn hủy')
ax1.set_xlabel('Phương thức thanh toán')
ax1.set_ylabel('Số lượng đơn hủy')
ax1.set_title('69. Số lượng và Tỷ lệ hủy đơn theo Phương thức thanh toán')

ax2 = ax1.twinx()
ax2.plot(req69['payment_method'], req69['cancel_rate'], color='darkred', marker='o', linewidth=2, label='Tỷ lệ hủy (%)')
ax2.set_ylabel('Tỷ lệ hủy (%)')

fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# --------------------------------------------------------------------------------
# 71. Lợi nhuận ròng sau Hoàn trả theo Danh mục (Net Profit post-Returns)
# --------------------------------------------------------------------------------
profit_df = pd.merge(order_items, products, on='product_id')
profit_df['gross_profit'] = profit_df['quantity'] * (profit_df['unit_price'] - profit_df['cogs'])
gross_by_cat = profit_df.groupby('category')['gross_profit'].sum().reset_index()

return_df = pd.merge(returns, products, on='product_id')
return_by_cat = return_df.groupby('category')['refund_amount'].sum().reset_index()

req71 = pd.merge(gross_by_cat, return_by_cat, on='category', how='left').fillna(0)
req71['net_profit'] = req71['gross_profit'] - req71['refund_amount']

plt.figure(figsize=(10, 6))
x = np.arange(len(req71['category']))
width = 0.35

plt.bar(x - width/2, req71['gross_profit'], width, label='Lợi nhuận gộp', color='lightblue')
plt.bar(x + width/2, req71['net_profit'], width, label='Lợi nhuận ròng (Sau hoàn trả)', color='dodgerblue')

plt.xticks(x, req71['category'])
plt.title('71. Lợi nhuận gộp và Lợi nhuận ròng sau Hoàn trả theo Danh mục')
plt.xlabel('Danh mục sản phẩm')
plt.ylabel('Lợi nhuận')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --------------------------------------------------------------------------------
# 72. Doanh thu theo Kênh thanh toán (Revenue by Payment Channel)
# --------------------------------------------------------------------------------
success_orders = orders[orders['order_status'] != 'cancelled']
req72_df = pd.merge(success_orders, payments, on='order_id')
req72 = req72_df.groupby('payment_method')['payment_value'].sum().reset_index().sort_values('payment_value', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(req72['payment_method'], req72['payment_value'], color='mediumpurple')
plt.title('72. Doanh thu thực tế theo Kênh thanh toán (Không tính đơn hủy)')
plt.xlabel('Kênh thanh toán')
plt.ylabel('Tổng doanh thu')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --------------------------------------------------------------------------------
# 73. Tương quan Khối lượng giảm giá và Tăng trưởng lợi nhuận (Discount vs Margin Impact)
# --------------------------------------------------------------------------------
req73_df = pd.merge(orders, order_items, on='order_id')
req73_df = pd.merge(req73_df, products, on='product_id')
req73_df['year_month'] = req73_df['order_date'].astype(str).str[:7]

req73_df['revenue'] = req73_df['quantity'] * req73_df['unit_price']
req73_df['total_cogs'] = req73_df['quantity'] * req73_df['cogs']

req73_agg = req73_df.groupby('year_month').agg({
    'discount_amount': 'sum',
    'revenue': 'sum',
    'total_cogs': 'sum'
}).reset_index()

req73_agg['gross_margin'] = (req73_agg['revenue'] - req73_agg['total_cogs']) / req73_agg['revenue']

plt.figure(figsize=(8, 6))
plt.scatter(req73_agg['discount_amount'], req73_agg['gross_margin'], alpha=0.7, color='teal', s=100)
plt.title('73. Tương quan Tổng giảm giá và Biên lợi nhuận gộp theo tháng')
plt.xlabel('Tổng khối lượng giảm giá (Sum of Discount)')
plt.ylabel('Biên lợi nhuận gộp (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# --------------------------------------------------------------------------------
# 74. Tỷ lệ khách hàng mua trước trả sau (BNPL Adoption Rate)
# --------------------------------------------------------------------------------
premium_items = pd.merge(order_items, products[products['segment'] == 'Premium'], on='product_id')
premium_orders_ids = premium_items['order_id'].unique()

req74_orders = orders[orders['order_id'].isin(premium_orders_ids)]
req74_df = pd.merge(req74_orders, customers, on='customer_id')
req74_df = pd.merge(req74_df, payments, on='order_id', how='left')

req74_df = req74_df.dropna(subset=['age_group'])
req74_df['is_bnpl'] = req74_df['installments'] > 1

req74_agg = req74_df.groupby('age_group').agg(
    total_orders=('order_id', 'nunique'),
    bnpl_orders=('is_bnpl', lambda x: x[x == True].count())
).reset_index()

req74_agg['bnpl_rate'] = req74_agg['bnpl_orders'] / req74_agg['total_orders'] * 100

plt.figure(figsize=(9, 6))
bars = plt.bar(req74_agg['age_group'], req74_agg['bnpl_rate'], color='orange')
plt.title('74. Tỷ lệ áp dụng Mua trước trả sau (BNPL) cho SP Premium theo Nhóm tuổi')
plt.xlabel('Nhóm tuổi')
plt.ylabel('Tỷ lệ đơn hàng BNPL (%)')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()