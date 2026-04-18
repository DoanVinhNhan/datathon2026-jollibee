import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

import seaborn as sns

# ==========================================
# ĐỌC VÀ KẾT NỐI DỮ LIỆU
# ==========================================
orders = pd.read_csv(DATA_DIR + 'orders.csv')
shipments = pd.read_csv(DATA_DIR + 'shipments.csv')
geography = pd.read_csv(DATA_DIR + 'geography.csv')

df = orders.merge(shipments, on='order_id', how='left')
df = df.merge(geography, on='zip', how='left')

# Chuyển đổi định dạng ngày tháng
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Tính toán các chỉ số thời gian (bằng ngày)
df['delivery_time'] = (df['delivery_date'] - df['order_date']).dt.days
df['lead_time'] = (df['ship_date'] - df['order_date']).dt.days

# Các trường phụ phục vụ group by
df['order_month'] = df['order_date'].dt.to_period('M')
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month


# ==========================================
# 11. Thời gian giao hàng trung bình vùng miền
# ==========================================
plt.figure(figsize=(10, 6))
df_11 = df[df['order_status'] == 'delivered'].groupby('region')['delivery_time'].mean().reset_index()
df_11 = df_11.sort_values('delivery_time')

plt.bar(df_11['region'], df_11['delivery_time'], color='skyblue')
plt.title('11. Thời gian giao hàng trung bình theo vùng miền (Delivered Orders)')
plt.xlabel('Vùng miền (Region)')
plt.ylabel('Thời gian giao hàng trung bình (Ngày)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 12. Xu hướng thời gian chuẩn bị hàng (Lead Time Trend)
# ==========================================
plt.figure(figsize=(12, 6))
df_12 = df.dropna(subset=['lead_time']).groupby('order_month')['lead_time'].mean().reset_index()
df_12['order_month'] = df_12['order_month'].astype(str)

plt.plot(df_12['order_month'], df_12['lead_time'], marker='o', linestyle='-', color='orange')
plt.title('12. Xu hướng thời gian chuẩn bị hàng trung bình theo tháng')
plt.xlabel('Tháng đặt hàng')
plt.ylabel('Lead Time Trung bình (Ngày)')
plt.xticks(df_12['order_month'][::6], rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==========================================
# 13. Bản đồ nhiệt cước phí vận chuyển
# ==========================================
plt.figure(figsize=(14, 8))
df_13 = df.dropna(subset=['shipping_fee', 'city', 'district'])
pivot_13 = df_13.pivot_table(values='shipping_fee', index='city', columns='district', aggfunc='mean')

sns.heatmap(pivot_13, cmap='YlOrRd', cbar_kws={'label': 'Cước phí vận chuyển trung bình'})
plt.title('13. Bản đồ nhiệt cước phí vận chuyển trung bình theo Thành phố và Quận/Huyện')
plt.xlabel('Quận/Huyện (District)')
plt.ylabel('Thành phố (City)')
plt.tight_layout()
plt.show()


# ==========================================
# 14. Phân bổ Zip Code có lượng đơn cao nhất
# ==========================================
plt.figure(figsize=(10, 8))
df_14 = df['zip'].value_counts().head(20).sort_values(ascending=True)

plt.barh(df_14.index.astype(str), df_14.values, color='cornflowerblue')
plt.title('14. Top 20 Zip Code có lượng đơn hàng cao nhất')
plt.xlabel('Số lượng đơn hàng')
plt.ylabel('Mã bưu điện (Zip Code)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 15. Thời gian giao hàng theo Thiết bị đặt
# ==========================================
plt.figure(figsize=(8, 6))
df_15 = df.dropna(subset=['delivery_time']).groupby('device_type')['delivery_time'].mean().reset_index()

plt.bar(df_15['device_type'], df_15['delivery_time'], color='mediumseagreen')
plt.title('15. Thời gian giao hàng trung bình theo thiết bị đặt hàng')
plt.xlabel('Thiết bị (Device Type)')
plt.ylabel('Thời gian giao hàng trung bình (Ngày)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 16. Tổng cước phí vận chuyển theo tháng (YTD)
# ==========================================
plt.figure(figsize=(10, 6))
# Xác định năm hiện tại (năm lớn nhất trong tập dữ liệu) để lấy YTD
max_year = df['year'].max()
df_16 = df[df['year'] == max_year].groupby('month')['shipping_fee'].sum().reset_index()

plt.plot(df_16['month'], df_16['shipping_fee'], marker='s', color='crimson', linewidth=2)
plt.title(f'16. Tổng cước phí vận chuyển theo tháng (YTD - Năm {max_year})')
plt.xlabel('Tháng')
plt.ylabel('Tổng cước phí vận chuyển')
plt.xticks(np.arange(1, 13, 1))
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 17. Tương quan Cước phí và Thời gian giao hàng
# ==========================================
plt.figure(figsize=(10, 6))
df_17 = df.dropna(subset=['shipping_fee', 'delivery_time', 'region']).groupby('region').agg(
    avg_shipping_fee=('shipping_fee', 'mean'),
    avg_delivery_time=('delivery_time', 'mean')
).reset_index()

plt.scatter(df_17['avg_delivery_time'], df_17['avg_shipping_fee'], s=150, color='purple', alpha=0.7)
for i, row in df_17.iterrows():
    plt.annotate(row['region'], 
                 (row['avg_delivery_time'], row['avg_shipping_fee']), 
                 xytext=(8, 8), textcoords='offset points')

plt.title('17. Tương quan giữa Cước phí và Thời gian giao hàng trung bình theo Vùng')
plt.xlabel('Thời gian giao hàng trung bình (Ngày)')
plt.ylabel('Cước phí vận chuyển trung bình')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 18. Tỷ lệ đơn hàng giao trễ (Late Delivery Rate)
# ==========================================
plt.figure(figsize=(10, 6))
# Do không có Expected Delivery Time trong dữ liệu, giả định SLA tiêu chuẩn là 5 ngày
SLA_DAYS = 5
df_late = df.dropna(subset=['delivery_time']).copy()
df_late['is_late'] = df_late['delivery_time'] > SLA_DAYS
df_18 = df_late.groupby('region')['is_late'].mean().reset_index()
df_18['is_late_pct'] = df_18['is_late'] * 100

plt.bar(df_18['region'], df_18['is_late_pct'], color='salmon')
plt.title(f'18. Tỷ lệ đơn hàng giao trễ theo Vùng (Giả định SLA = {SLA_DAYS} ngày)')
plt.xlabel('Vùng miền (Region)')
plt.ylabel('Tỷ lệ đơn giao trễ (%)')

for i, val in enumerate(df_18['is_late_pct']):
    plt.text(i, val + 0.5, f"{val:.1f}%", ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ==========================================
# 19. Chi phí vận chuyển trung bình trên mỗi đơn
# ==========================================
plt.figure(figsize=(12, 6))
df_19 = df.dropna(subset=['shipping_fee']).groupby('order_month')['shipping_fee'].mean().reset_index()
df_19['order_month'] = df_19['order_month'].astype(str)

plt.plot(df_19['order_month'], df_19['shipping_fee'], marker='o', color='teal')
plt.title('19. Chi phí vận chuyển trung bình trên mỗi đơn hàng theo tháng')
plt.xlabel('Tháng đặt hàng')
plt.ylabel('Cước phí vận chuyển trung bình / Đơn')
plt.xticks(df_19['order_month'][::6], rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# ==========================================
# 20. Lead time theo Thiết bị đặt hàng
# ==========================================
plt.figure(figsize=(8, 6))
df_20 = df.dropna(subset=['lead_time']).groupby('device_type')['lead_time'].mean().reset_index()

plt.bar(df_20['device_type'], df_20['lead_time'], color='orchid')
plt.title('20. Thời gian chuẩn bị hàng trung bình theo thiết bị đặt hàng')
plt.xlabel('Thiết bị (Device Type)')
plt.ylabel('Lead Time Trung bình (Ngày)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()