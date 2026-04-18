import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

customers = pd.read_csv(DATA_DIR + 'customers.csv')
orders = pd.read_csv(DATA_DIR + 'orders.csv')
order_items = pd.read_csv(DATA_DIR + 'order_items.csv')
products = pd.read_csv(DATA_DIR + 'products.csv')
payments = pd.read_csv(DATA_DIR + 'payments.csv')

orders['order_date'] = pd.to_datetime(orders['order_date'])
customers['signup_date'] = pd.to_datetime(customers['signup_date'])

# -------------------------------------------------------------------
# 59. Phân bổ khoảng cách mua lặp lại (Inter-order Gap - Q1)
# -------------------------------------------------------------------
order_counts = orders.groupby('customer_id')['order_id'].nunique()
multi_order_customers = order_counts[order_counts > 1].index
orders_multi = orders[orders['customer_id'].isin(multi_order_customers)].sort_values(['customer_id', 'order_date'])

orders_multi['prev_order_date'] = orders_multi.groupby('customer_id')['order_date'].shift(1)
orders_multi['gap_days'] = (orders_multi['order_date'] - orders_multi['prev_order_date']).dt.days

median_gaps = orders_multi.dropna(subset=['gap_days']).groupby('customer_id')['gap_days'].median().reset_index()

bins = [-1, 30, 90, 180, np.inf]
labels = ['<30 ngày', '30-90 ngày', '90-180 ngày', '>180 ngày']
median_gaps['bracket'] = pd.cut(median_gaps['gap_days'], bins=bins, labels=labels)
gap_counts = median_gaps['bracket'].value_counts().reindex(labels)

plt.figure(figsize=(8, 5))
gap_counts.plot(kind='bar', color='#4C72B0', edgecolor='black')
plt.title('59. Phân bổ khoảng cách mua lặp lại (Inter-order Gap)')
plt.xlabel('Khoảng cách giữa 2 lần mua')
plt.ylabel('Số lượng khách hàng')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 60. Tần suất mua hàng theo Nhóm tuổi (Purchase Frequency by Age - Q6)
# -------------------------------------------------------------------
cust_valid_age = customers[customers['age_group'].notna()]
orders_age_merged = orders.merge(cust_valid_age[['customer_id', 'age_group']], on='customer_id')

orders_per_age = orders_age_merged.groupby('age_group')['order_id'].nunique().reset_index(name='total_orders')
cust_per_age = cust_valid_age.groupby('age_group')['customer_id'].nunique().reset_index(name='total_customers')

freq_by_age = pd.merge(orders_per_age, cust_per_age, on='age_group')
freq_by_age['avg_orders'] = freq_by_age['total_orders'] / freq_by_age['total_customers']

plt.figure(figsize=(8, 5))
plt.bar(freq_by_age['age_group'], freq_by_age['avg_orders'], color='#55A868', edgecolor='black')
plt.title('60. Tần suất mua hàng theo Nhóm tuổi')
plt.xlabel('Nhóm tuổi')
plt.ylabel('Số đơn hàng trung bình / Khách hàng')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 61. Số sản phẩm trên mỗi giao dịch (UPT - Units Per Transaction)
# -------------------------------------------------------------------
qty_per_order = order_items.groupby('order_id')['quantity'].sum().reset_index()
orders_qty_merged = orders[['order_id', 'device_type']].merge(qty_per_order, on='order_id')

upt_by_channel = orders_qty_merged.groupby('device_type')['quantity'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(upt_by_channel['device_type'].astype(str), upt_by_channel['quantity'], color='#C44E52', edgecolor='black')
plt.title('61. Số sản phẩm trên mỗi giao dịch (UPT) theo Kênh')
plt.xlabel('Kênh mua sắm (Device Type)')
plt.ylabel('Số lượng sản phẩm trung bình/đơn')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 62. Phân khúc Khách hàng theo RFM (RFM Customer Segments)
# -------------------------------------------------------------------
current_date = orders['order_date'].max()

rfm_r = orders.groupby('customer_id')['order_date'].max().reset_index()
rfm_r['Recency'] = (current_date - rfm_r['order_date']).dt.days

rfm_f = orders.groupby('customer_id')['order_id'].nunique().reset_index()
rfm_f.columns = ['customer_id', 'Frequency']

payment_totals = payments.groupby('order_id')['payment_value'].sum().reset_index()
orders_payments = orders[['order_id', 'customer_id']].merge(payment_totals, on='order_id')
rfm_m = orders_payments.groupby('customer_id')['payment_value'].sum().reset_index()
rfm_m.columns = ['customer_id', 'Monetary']

rfm = rfm_r.merge(rfm_f, on='customer_id').merge(rfm_m, on='customer_id')

r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

rfm['R'] = pd.qcut(rfm['Recency'], q=4, labels=r_labels, duplicates='drop').astype(int)
rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=f_labels).astype(int)
rfm['M'] = pd.qcut(rfm['Monetary'], q=4, labels=m_labels).astype(int)
rfm['RFM_Score'] = rfm['R'] + rfm['F'] + rfm['M']

def assign_segment(score):
    if score >= 10: return 'VIP'
    elif score >= 8: return 'Loyal'
    elif score >= 5: return 'At-Risk'
    else: return 'Churn'

rfm['Segment'] = rfm['RFM_Score'].apply(assign_segment)
segment_counts = rfm['Segment'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=140, 
        colors=['#8172B2', '#64B5CD', '#CCB974', '#C44E52'])
plt.title('62. Phân khúc Khách hàng theo RFM')
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 63. Lưới Phân tích Giỏ hàng (Market Basket - Cross-sell Matrix)
# -------------------------------------------------------------------
cart_sizes = order_items.groupby('order_id')['product_id'].count()
valid_orders = cart_sizes[cart_sizes > 1].index

oi_filtered = order_items[order_items['order_id'].isin(valid_orders)]
oi_cats = oi_filtered.merge(products[['product_id', 'category']], on='product_id')

pairs = oi_cats[['order_id', 'category']].merge(oi_cats[['order_id', 'category']], on='order_id')
pairs = pairs[pairs['category_x'] != pairs['category_y']]

cross_matrix = pd.crosstab(pairs['category_x'], pairs['category_y'])

plt.figure(figsize=(8, 6))
plt.imshow(cross_matrix, cmap='Blues')
plt.colorbar(label='Số lượng đơn hàng kết hợp')
plt.xticks(ticks=np.arange(len(cross_matrix.columns)), labels=cross_matrix.columns, rotation=45)
plt.yticks(ticks=np.arange(len(cross_matrix.index)), labels=cross_matrix.index)

for i in range(len(cross_matrix.index)):
    for j in range(len(cross_matrix.columns)):
        plt.text(j, i, cross_matrix.iloc[i, j], ha='center', va='center', color='black')

plt.title('63. Lưới Phân tích Giỏ hàng (Cross-sell Matrix)')
plt.xlabel('Danh mục Y')
plt.ylabel('Danh mục X')
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 64. Giá trị vòng đời khách hàng theo Nguồn thu hút (CLV by Acquisition Source)
# -------------------------------------------------------------------
max_acq_date = customers['signup_date'].max()
tenured_customers = customers[(max_acq_date - customers['signup_date']).dt.days > 365]

clv_merged = tenured_customers.merge(rfm_m, on='customer_id', how='left').fillna(0)
clv_by_source = clv_merged.groupby('acquisition_channel')['Monetary'].mean().reset_index()
clv_by_source = clv_by_source.sort_values(by='Monetary', ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(clv_by_source['acquisition_channel'].astype(str), clv_by_source['Monetary'], color='#DD8452', edgecolor='black')
plt.title('64. Giá trị vòng đời khách hàng (CLV) theo Nguồn thu hút')
plt.xlabel('Nguồn thu hút')
plt.ylabel('CLV trung bình (VNĐ)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 65. Tỷ lệ giữ chân khách hàng (Retention Cohort Heatmap)
# -------------------------------------------------------------------
orders_cohort = orders[['order_id', 'customer_id', 'order_date']].copy()
orders_cohort['order_month'] = orders_cohort['order_date'].dt.to_period('M')

cohorts = orders_cohort.groupby('customer_id')['order_month'].min().reset_index()
cohorts.columns = ['customer_id', 'cohort_month']

orders_cohort = orders_cohort.merge(cohorts, on='customer_id')
orders_cohort['cohort_idx'] = (orders_cohort['order_month'] - orders_cohort['cohort_month']).apply(lambda x: x.n)

cohort_data = orders_cohort.groupby(['cohort_month', 'cohort_idx'])['customer_id'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='cohort_month', columns='cohort_idx', values='customer_id')

cohort_sizes = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_sizes, axis=0) * 100

# Trực quan hoá cho các cohort thuộc năm 2021 để không bị quá tải biểu đồ
retention_2021 = retention[retention.index.year == 2021].iloc[:, :13]

plt.figure(figsize=(12, 8))
plt.imshow(retention_2021, cmap='YlGnBu', aspect='auto')
plt.colorbar(label='Tỷ lệ giữ chân (%)')
plt.xticks(ticks=np.arange(len(retention_2021.columns)), labels=retention_2021.columns)
plt.yticks(ticks=np.arange(len(retention_2021.index)), labels=retention_2021.index.astype(str))

for i in range(len(retention_2021.index)):
    for j in range(len(retention_2021.columns)):
        val = retention_2021.iloc[i, j]
        if pd.notna(val):
            plt.text(j, i, f'{val:.1f}', ha='center', va='center', color='black', fontsize=8)

plt.title('65. Tỷ lệ giữ chân khách hàng (Cohorts năm 2021, 12 tháng đầu)')
plt.xlabel('Tháng thứ N')
plt.ylabel('Tháng mua hàng đầu tiên (Cohort)')
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 66. Phân bổ Giá trị đơn hàng theo Giới tính (AOV by Gender)
# -------------------------------------------------------------------
orders_payments_gender = orders[['order_id', 'customer_id']].merge(
    payments[['order_id', 'payment_value']], on='order_id'
).merge(
    customers[['customer_id', 'gender']], on='customer_id'
)

aov_by_gender = orders_payments_gender.dropna(subset=['gender']).groupby('gender')['payment_value'].mean().reset_index()

plt.figure(figsize=(7, 5))
plt.bar(aov_by_gender['gender'], aov_by_gender['payment_value'], color='#937860', edgecolor='black', width=0.5)
plt.title('66. Phân bổ Giá trị đơn hàng theo Giới tính (AOV by Gender)')
plt.xlabel('Giới tính')
plt.ylabel('Giá trị đơn hàng trung bình (VNĐ)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()