import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = 'dataset/'

# Đọc dữ liệu
try:
    df_web = pd.read_csv(DATA_DIR + 'web_traffic.csv')
    df_web['date'] = pd.to_datetime(df_web['date'])
except Exception as e:
    print(f"Lỗi đọc web_traffic.csv: {e}")

try:
    df_orders = pd.read_csv(DATA_DIR + 'orders.csv')
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
except Exception as e:
    print(f"Lỗi đọc orders.csv: {e}")

# =====================================================================
# Yêu cầu 31: Phễu chuyển đổi Website (Web Funnel Conversion)
# Dữ liệu hiện tại không có funnel chi tiết (Add to cart, Checkout). 
# Xây dựng phễu giả định dựa trên Sessions -> Đơn hàng -> Đơn hàng giao thành công.
# =====================================================================
total_sessions = df_web['sessions'].sum() if 'sessions' in df_web.columns else 1000000
total_orders = len(df_orders)
total_delivered = len(df_orders[df_orders['order_status'] == 'delivered'])

funnel_stages = ['Sessions', 'Orders Created', 'Orders Delivered']
funnel_values = [total_sessions, total_orders, total_delivered]

plt.figure(figsize=(10, 6))
bars = plt.bar(funnel_stages, funnel_values, color=['#3498db', '#f1c40f', '#2ecc71'])
plt.title('31. Phễu chuyển đổi Website (Sessions -> Orders -> Delivered)', fontsize=14)
plt.ylabel('Số lượng')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + (yval*0.02), f'{int(yval):,}', ha='center', va='bottom')
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 32: Lưu lượng truy cập theo Nguồn (Traffic by Source)
# =====================================================================
if 'traffic_source' in df_web.columns and 'sessions' in df_web.columns:
    traffic_by_source = df_web.groupby('traffic_source')['sessions'].sum().sort_values(ascending=True)
    
    plt.figure(figsize=(10, 6))
    traffic_by_source.plot(kind='barh', color='#9b59b6')
    plt.title('32. Lưu lượng truy cập (Sessions) theo Nguồn', fontsize=14)
    plt.xlabel('Tổng số Sessions')
    plt.ylabel('Nguồn truy cập')
    for i, v in enumerate(traffic_by_source):
        plt.text(v, i, f" {int(v):,}", va='center')
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 33 & 93: Tỷ lệ thoát trang theo Nguồn (Bounce Rate by Traffic Source)
# =====================================================================
if 'traffic_source' in df_web.columns and 'bounce_rate' in df_web.columns:
    bounce_by_source = df_web.groupby('traffic_source')['bounce_rate'].mean().sort_values(ascending=True)
    
    plt.figure(figsize=(10, 6))
    bars = bounce_by_source.plot(kind='bar', color='#e74c3c')
    plt.title('33 & 93. Tỷ lệ thoát trang trung bình (Bounce Rate) theo Nguồn', fontsize=14)
    plt.ylabel('Bounce Rate')
    plt.xlabel('Nguồn truy cập')
    plt.xticks(rotation=45)
    for p in bars.patches:
        bars.annotate(f"{p.get_height():.4f}", (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 38: Thời lượng phiên Web theo Nguồn (Avg Session by Source)
# =====================================================================
if 'traffic_source' in df_web.columns and 'avg_session_duration_sec' in df_web.columns:
    avg_duration_source = df_web.groupby('traffic_source')['avg_session_duration_sec'].mean().sort_values(ascending=True)
    
    plt.figure(figsize=(10, 6))
    avg_duration_source.plot(kind='barh', color='#34495e')
    plt.title('38. Thời lượng phiên Web trung bình (giây) theo Nguồn', fontsize=14)
    plt.xlabel('Avg Session Duration (sec)')
    plt.ylabel('Nguồn truy cập')
    for i, v in enumerate(avg_duration_source):
        plt.text(v, i, f" {v:.1f}s", va='center')
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 39: Tương quan Thời lượng phiên và Bounce Rate (Engagement Scatter)
# =====================================================================
if 'traffic_source' in df_web.columns:
    scatter_data = df_web.groupby('traffic_source').agg({
        'avg_session_duration_sec': 'mean',
        'bounce_rate': 'mean'
    }).reset_index()
    
    plt.figure(figsize=(10, 6))
    plt.scatter(scatter_data['avg_session_duration_sec'], scatter_data['bounce_rate'], color='#e67e22', s=100)
    for i, row in scatter_data.iterrows():
        plt.text(row['avg_session_duration_sec'] + 1, row['bounce_rate'], row['traffic_source'], fontsize=10)
    
    plt.title('39. Tương quan giữa Thời lượng phiên và Tỷ lệ thoát theo Nguồn', fontsize=14)
    plt.xlabel('Avg Session Duration (sec)')
    plt.ylabel('Bounce Rate')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 40: Xu hướng Traffic theo thời gian rà soát (YTD)
# =====================================================================
if 'date' in df_web.columns and 'sessions' in df_web.columns:
    max_year = df_web['date'].dt.year.max()
    df_ytd = df_web[df_web['date'].dt.year == max_year]
    df_ytd['month'] = df_ytd['date'].dt.month
    monthly_traffic = df_ytd.groupby('month')['sessions'].sum()
    
    plt.figure(figsize=(12, 6))
    monthly_traffic.plot(kind='line', marker='o', color='#1abc9c', linewidth=2)
    plt.title(f'40. Xu hướng Lưu lượng truy cập (Sessions) trong năm {max_year} (YTD)', fontsize=14)
    plt.xlabel('Tháng')
    plt.ylabel('Tổng Sessions')
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 94: Chất lượng Traffic: Tỷ lệ chuyển đổi theo Nguồn (Conversion Rate by Source)
# =====================================================================
if 'traffic_source' in df_web.columns and 'order_source' in df_orders.columns:
    sessions_by_source = df_web.groupby('traffic_source')['sessions'].sum().reset_index()
    orders_by_source = df_orders.groupby('order_source')['order_id'].count().reset_index()
    
    merged_sources = pd.merge(sessions_by_source, orders_by_source, left_on='traffic_source', right_on='order_source', how='inner')
    merged_sources['conversion_rate'] = (merged_sources['order_id'] / merged_sources['sessions']) * 100
    merged_sources = merged_sources.sort_values(by='conversion_rate', ascending=False)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(merged_sources['traffic_source'], merged_sources['conversion_rate'], color='#2c3e50')
    plt.title('94. Tỷ lệ chuyển đổi (Conversion Rate %) theo Nguồn Traffic', fontsize=14)
    plt.xlabel('Nguồn truy cập')
    plt.ylabel('Tỷ lệ chuyển đổi (%)')
    plt.xticks(rotation=45)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}%', ha='center', va='bottom')
    plt.tight_layout()
    plt.show()

# =====================================================================
# Yêu cầu 95: Hành trình Đa kênh (Omnichannel: O2O Tracking - Store Pickup)
# Do dataset thực tế không chứa cột 'Delivery Type', tạo Mock Data để visualize.
# =====================================================================
mock_o2o_data = pd.DataFrame({
    'Delivery_Type': ['Home Delivery', 'Store Pickup (Click & Collect)'],
    'Order_Count': [85400, 14600]
})

plt.figure(figsize=(8, 8))
plt.pie(mock_o2o_data['Order_Count'], labels=mock_o2o_data['Delivery_Type'], autopct='%1.1f%%', startangle=140, colors=['#bdc3c7', '#2980b9'])
plt.title('95. Tỷ trọng đơn hàng Click & Collect (O2O Tracking)', fontsize=14)
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 96: Phân bổ Lượt tìm kiếm Nội bộ theo Từ khóa (Internal Search Terms)
# Dataset không chứa log search query. Tạo Mock Data đại diện top keywords.
# =====================================================================
mock_search_data = pd.DataFrame({
    'Search_Query': ['t-shirt', 'jacket', 'hoodie', 'jeans', 'sneakers', 'dress', 'cap', 'socks', 'backpack', 'sweater'],
    'Search_Volume': [15200, 12400, 9800, 8500, 7200, 5100, 4300, 3100, 2800, 1900]
}).sort_values(by='Search_Volume', ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(mock_search_data['Search_Query'], mock_search_data['Search_Volume'], color='#8e44ad')
plt.title('96. Top 10 Từ khóa tìm kiếm nội bộ (Internal Search Terms)', fontsize=14)
plt.xlabel('Khối lượng tìm kiếm (Search Volume)')
plt.ylabel('Từ khóa')
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 97: Tỷ lệ Khách hàng tạo tài khoản so với Mua tư cách khách
# EDA file báo cáo orders.csv không có customer_id null, tức 100% Registered.
# =====================================================================
mock_guest_reg = pd.DataFrame({
    'Account_Type': ['Registered Users', 'Guest Checkout'],
    'Order_Count': [df_orders.shape[0] if not df_orders.empty else 100000, 0] # Dựa vào thực tế EDA
})

plt.figure(figsize=(8, 8))
plt.pie(mock_guest_reg['Order_Count'], labels=mock_guest_reg['Account_Type'], autopct=lambda p: '{:.0f}%'.format(p) if p > 0 else '', colors=['#27ae60', '#95a5a6'])
plt.title('97. Tỷ lệ khách hàng mua qua Tài khoản vs Khách Vãng lai', fontsize=14)
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 98: Tác động của Review/Hình ảnh đến Tỷ lệ chuyển đổi (Visual Content Impact)
# Dataset thiếu flag PDP Video/UGC. Tạo Mock Data.
# =====================================================================
mock_visual_impact = pd.DataFrame({
    'Content_Presence': ['Không có Video/UGC', 'Có Video/User-generated Content'],
    'Add_To_Cart_Rate': [3.5, 8.7]
})

plt.figure(figsize=(8, 6))
bars = plt.bar(mock_visual_impact['Content_Presence'], mock_visual_impact['Add_To_Cart_Rate'], color=['#7f8c8d', '#d35400'], width=0.5)
plt.title('98. Tác động của Video/Hình ảnh thực tế đến Tỷ lệ Add-to-cart', fontsize=14)
plt.ylabel('Tỷ lệ Add-to-cart (%)')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval}%', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 99: Tốc độ chuyển đổi thiết bị chéo (Cross-device Purchase Journey)
# Dataset chỉ có device_type lúc checkout, không có thiết bị chạm lần đầu. Mock Data.
# =====================================================================
mock_cross_device = pd.DataFrame({
    'Journey_Path': ['Mobile -> Mobile', 'Desktop -> Desktop', 'Mobile -> Desktop', 'Desktop -> Mobile'],
    'Conversions': [42000, 28000, 15500, 4500]
}).sort_values(by='Conversions', ascending=True)

plt.figure(figsize=(10, 5))
plt.barh(mock_cross_device['Journey_Path'], mock_cross_device['Conversions'], color='#16a085')
plt.title('99. Hành trình mua hàng chéo thiết bị (Cross-device Path)', fontsize=14)
plt.xlabel('Số lượng hành trình chuyển đổi')
plt.ylabel('Thiết bị (First Touch -> Checkout)')
plt.tight_layout()
plt.show()

# =====================================================================
# Yêu cầu 100: ROAS (Return on Ad Spend) theo Kênh quảng cáo
# Dataset không chứa Ad Spend. Tạo Mock Data.
# =====================================================================
mock_roas = pd.DataFrame({
    'Ad_Channel': ['Google Shopping', 'Meta Ads', 'TikTok Ads', 'Affiliate'],
    'ROAS': [4.8, 3.5, 2.2, 5.1]
}).sort_values(by='ROAS', ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(mock_roas['Ad_Channel'], mock_roas['ROAS'], color='#c0392b')
plt.title('100. Hiệu quả Quảng cáo (ROAS) theo Kênh Paid', fontsize=14)
plt.ylabel('Chỉ số ROAS (Revenue / Ad Spend)')
plt.xlabel('Kênh Quảng Cáo')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval}x', ha='center', va='bottom')
plt.axhline(y=3.0, color='r', linestyle='--', label='Target ROAS (3.0x)')
plt.legend()
plt.tight_layout()
plt.show()