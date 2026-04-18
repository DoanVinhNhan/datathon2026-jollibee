import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
DATA_DIR  = 'dataset/'

# Đọc các file dữ liệu cần thiết
reviews_df = pd.read_csv(DATA_DIR + 'reviews.csv')
products_df = pd.read_csv(DATA_DIR + 'products.csv')
customers_df = pd.read_csv(DATA_DIR + 'customers.csv')
orders_df = pd.read_csv(DATA_DIR + 'orders.csv')

# Chuyển đổi định dạng ngày tháng
reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'])
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])

# =============================================================================
# 21. Điểm đánh giá trung bình theo Danh mục (Avg Review by Category)
# =============================================================================
rev_prod = reviews_df.merge(products_df, on='product_id', how='inner')
avg_rev_cat = rev_prod.groupby('category')['rating'].mean().reset_index()

plt.figure(figsize=(10, 6))
bars = plt.bar(avg_rev_cat['category'], avg_rev_cat['rating'], color='skyblue', edgecolor='black')
plt.title('21. Avg Review Score by Category', fontsize=14)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Average Review Score', fontsize=12)
plt.ylim(0, 5)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', ha='center', va='bottom', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# =============================================================================
# 22. Tỷ lệ Đánh giá Tích cực / Tiêu cực (Sentiment Distribution)
# =============================================================================
reviews_df['review_month'] = reviews_df['review_date'].dt.to_period('M')

def categorize_sentiment(rating):
    if rating <= 2:
        return 'Negative (1-2)'
    elif rating == 3:
        return 'Neutral (3)'
    else:
        return 'Positive (4-5)'

reviews_df['sentiment'] = reviews_df['rating'].apply(categorize_sentiment)
sentiment_dist = reviews_df.groupby(['review_month', 'sentiment']).size().unstack(fill_value=0)
sentiment_pct = sentiment_dist.div(sentiment_dist.sum(axis=1), axis=0) * 100

sentiment_pct.index = sentiment_pct.index.astype(str)

plt.figure(figsize=(15, 6))
if 'Negative (1-2)' in sentiment_pct.columns:
    plt.plot(sentiment_pct.index, sentiment_pct['Negative (1-2)'], label='Negative', color='red', marker='o', markersize=4)
if 'Neutral (3)' in sentiment_pct.columns:
    plt.plot(sentiment_pct.index, sentiment_pct['Neutral (3)'], label='Neutral', color='orange', marker='o', markersize=4)
if 'Positive (4-5)' in sentiment_pct.columns:
    plt.plot(sentiment_pct.index, sentiment_pct['Positive (4-5)'], label='Positive', color='green', marker='o', markersize=4)

plt.title('22. Sentiment Distribution by Month', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Percentage of Reviews (%)', fontsize=12)
plt.xticks(rotation=90, fontsize=8)
plt.legend(title='Sentiment')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# =============================================================================
# 24. Điểm đánh giá theo Nhóm tuổi (Review Score by Age Group)
# =============================================================================
rev_cust = reviews_df.merge(customers_df, on='customer_id', how='inner')
avg_rev_age = rev_cust.dropna(subset=['age_group']).groupby('age_group')['rating'].mean().reset_index()

plt.figure(figsize=(10, 6))
bars = plt.bar(avg_rev_age['age_group'], avg_rev_age['rating'], color='lightgreen', edgecolor='black')
plt.title('24. Avg Review Score by Age Group', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Average Review Score', fontsize=12)
plt.ylim(0, 5)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', ha='center', va='bottom', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# =============================================================================
# 26. Lượng đánh giá theo Giới tính (Review Volume by Gender)
# =============================================================================
vol_gender = rev_cust.dropna(subset=['gender']).groupby('gender').size().reset_index(name='review_count')

plt.figure(figsize=(8, 6))
bars = plt.bar(vol_gender['gender'].astype(str), vol_gender['review_count'], color=['#ff9999', '#66b3ff', '#99ff99'], edgecolor='black')
plt.title('26. Review Volume by Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Total Reviews', fontsize=12)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + (max(vol_gender['review_count']) * 0.02), f'{int(yval):,}', ha='center', va='bottom', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# =============================================================================
# 28. Xu hướng điểm đánh giá theo thời gian mua (Review Score Trend)
# =============================================================================
rev_ord = reviews_df.merge(orders_df, on='order_id', how='inner')
rev_ord['order_month'] = rev_ord['order_date'].dt.to_period('M')
trend_score = rev_ord.groupby('order_month')['rating'].mean().reset_index()
trend_score['order_month'] = trend_score['order_month'].astype(str)

plt.figure(figsize=(15, 6))
plt.plot(trend_score['order_month'], trend_score['rating'], marker='.', linestyle='-', color='purple', linewidth=1.5)
plt.title('28. Review Score Trend by Order Month', fontsize=14)
plt.xlabel('Order Month', fontsize=12)
plt.ylabel('Average Review Score', fontsize=12)
plt.xticks(rotation=90, fontsize=8)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# =============================================================================
# 30. Tỷ lệ phản hồi đánh giá (Review Response Rate)
# =============================================================================
delivered_orders = orders_df[orders_df['order_status'] == 'delivered']
deliv_cust = delivered_orders.merge(customers_df, on='customer_id', how='inner')

# Count(Customers) đã nhận hàng (delivered) theo nhóm tuổi
deliv_cust_count = deliv_cust.dropna(subset=['age_group']).groupby('age_group')['customer_id'].nunique().reset_index(name='delivered_customers')

# Count(Reviews) theo nhóm tuổi
rev_cust_count = rev_cust.dropna(subset=['age_group']).groupby('age_group')['review_id'].nunique().reset_index(name='total_reviews')

response_rate = deliv_cust_count.merge(rev_cust_count, on='age_group', how='left')
response_rate['total_reviews'] = response_rate['total_reviews'].fillna(0)
response_rate['response_rate_pct'] = (response_rate['total_reviews'] / response_rate['delivered_customers']) * 100

plt.figure(figsize=(10, 6))
bars = plt.bar(response_rate['age_group'], response_rate['response_rate_pct'], color='coral', edgecolor='black')
plt.title('30. Review Response Rate by Age Group (Delivered Orders)', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Response Rate (%)', fontsize=12)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()