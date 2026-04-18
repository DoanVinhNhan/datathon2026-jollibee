# Báo cáo Khám phá Dữ liệu Cơ bản (Data Understanding, Missing & Distribution)

## Bảng: customers.csv
- **Số dòng:** 121,930
- **Số cột:** 7

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| customer_id | int64 | 121,930 | 1 | 157563 | 78736.90 |
| zip | int64 | 31,491 | 1001 | 99950 | 50990.17 |
| city | object | 42 | - | - | - |
| signup_date | object | 3,941 | - | - | - |
| gender | object | 3 | - | - | - |
| age_group | object | 5 | - | - | - |
| acquisition_channel | object | 6 | - | - | - |

---
## Bảng: geography.csv
- **Số dòng:** 39,948
- **Số cột:** 4

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| zip | int64 | 39,948 | 1 | 99950 | 50895.08 |
| city | object | 42 | - | - | - |
| region | object | 3 | - | - | - |
| district | object | 39 | - | - | - |

---
## Bảng: inventory.csv
- **Số dòng:** 60,247
- **Số cột:** 17

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| snapshot_date | object | 126 | - | - | - |
| product_id | int64 | 1,624 | 1 | 2412 | 1311.41 |
| stock_on_hand | int64 | 1,895 | 3 | 2673 | 189.30 |
| units_received | int64 | 360 | 1 | 817 | 18.05 |
| units_sold | int64 | 303 | 1 | 670 | 15.42 |
| stockout_days | int64 | 29 | 0 | 28 | 1.16 |
| days_of_supply | float64 | 9,289 | 5.20 | 68100.00 | 912.68 |
| fill_rate | float64 | 29 | 0.07 | 1.00 | 0.96 |
| stockout_flag | int64 | 2 | 0 | 1 | 0.67 |
| overstock_flag | int64 | 2 | 0 | 1 | 0.76 |
| reorder_flag | int64 | 1 | 0 | 0 | 0.00 |
| sell_through_rate | float64 | 4,017 | 0.00 | 0.85 | 0.15 |
| product_name | object | 1,465 | - | - | - |
| category | object | 4 | - | - | - |
| segment | object | 8 | - | - | - |
| year | int64 | 11 | 2012 | 2022 | 2017.22 |
| month | int64 | 12 | 1 | 12 | 6.62 |

---
## Bảng: order_items.csv
- **Số dòng:** 714,669
- **Số cột:** 7

### Dữ liệu bị khuyết (Missing Values)
| Cột | Số ô trống | Tỷ lệ (%) |
| --- | --- | --- |
| promo_id | 438,353 | 61.34% |
| promo_id_2 | 714,463 | 99.97% |

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| order_id | int64 | 646,945 | 1 | 834397 | 411615.08 |
| product_id | int64 | 1,598 | 1 | 2412 | 1234.93 |
| quantity | int64 | 8 | 1 | 8 | 4.50 |
| unit_price | float64 | 501,330 | 392.57 | 43056.00 | 5114.69 |
| discount_amount | float64 | 204,449 | 0.00 | 35235.47 | 1048.89 |
| promo_id | object | 50 | - | - | - |
| promo_id_2 | object | 2 | - | - | - |

---
## Bảng: orders.csv
- **Số dòng:** 646,945
- **Số cột:** 8

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| order_id | int64 | 646,945 | 1 | 834397 | 417189.47 |
| order_date | object | 3,833 | - | - | - |
| customer_id | int64 | 90,246 | 1 | 157563 | 84906.20 |
| zip | int64 | 29,932 | 1001 | 99950 | 55410.74 |
| order_status | object | 6 | - | - | - |
| payment_method | object | 5 | - | - | - |
| device_type | object | 3 | - | - | - |
| order_source | object | 6 | - | - | - |

---
## Bảng: payments.csv
- **Số dòng:** 646,945
- **Số cột:** 4

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| order_id | int64 | 646,945 | 1 | 834397 | 417189.47 |
| payment_method | object | 5 | - | - | - |
| payment_value | float64 | 595,420 | 389.74 | 331570.40 | 24238.33 |
| installments | int64 | 5 | 1 | 12 | 3.45 |

---
## Bảng: products.csv
- **Số dòng:** 2,412
- **Số cột:** 8

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| product_id | int64 | 2,412 | 1 | 2412 | 1206.50 |
| product_name | object | 2,172 | - | - | - |
| category | object | 4 | - | - | - |
| segment | object | 8 | - | - | - |
| size | object | 4 | - | - | - |
| color | object | 10 | - | - | - |
| price | float64 | 1,990 | 9.06 | 40950.00 | 4928.22 |
| cogs | float64 | 2,381 | 5.18 | 38902.50 | 3868.35 |

---
## Bảng: promotions.csv
- **Số dòng:** 50
- **Số cột:** 10

### Dữ liệu bị khuyết (Missing Values)
| Cột | Số ô trống | Tỷ lệ (%) |
| --- | --- | --- |
| applicable_category | 40 | 80.00% |

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| promo_id | object | 50 | - | - | - |
| promo_name | object | 50 | - | - | - |
| promo_type | object | 2 | - | - | - |
| discount_value | float64 | 6 | 10.00 | 50.00 | 18.50 |
| start_date | object | 50 | - | - | - |
| end_date | object | 50 | - | - | - |
| applicable_category | object | 2 | - | - | - |
| promo_channel | object | 5 | - | - | - |
| stackable_flag | int64 | 2 | 0 | 1 | 0.24 |
| min_order_value | int64 | 5 | 0 | 200000 | 46000.00 |

---
## Bảng: returns.csv
- **Số dòng:** 39,939
- **Số cột:** 7

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| return_id | object | 39,939 | - | - | - |
| order_id | int64 | 36,062 | 2 | 833351 | 409061.98 |
| product_id | int64 | 1,286 | 3 | 2412 | 1244.23 |
| return_date | object | 3,806 | - | - | - |
| return_reason | object | 5 | - | - | - |
| return_quantity | int64 | 8 | 1 | 8 | 2.74 |
| refund_amount | float64 | 39,560 | 458.81 | 160937.94 | 12784.46 |

---
## Bảng: reviews.csv
- **Số dòng:** 113,551
- **Số cột:** 7

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| review_id | object | 113,551 | - | - | - |
| order_id | int64 | 111,369 | 1 | 833296 | 408999.52 |
| product_id | int64 | 1,412 | 3 | 2412 | 1232.02 |
| customer_id | int64 | 48,676 | 2 | 157563 | 85694.34 |
| review_date | object | 3,825 | - | - | - |
| rating | int64 | 5 | 1 | 5 | 3.94 |
| review_title | object | 18 | - | - | - |

---
## Bảng: sales.csv
- **Số dòng:** 3,833
- **Số cột:** 3

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| Date | object | 3,833 | - | - | - |
| Revenue | float64 | 3,833 | 279813.94 | 20905271.35 | 4286584.03 |
| COGS | float64 | 3,833 | 236576.31 | 16535857.67 | 3695134.49 |

---
## Bảng: shipments.csv
- **Số dòng:** 566,067
- **Số cột:** 4

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| order_id | int64 | 566,067 | 1 | 834325 | 415816.87 |
| ship_date | object | 3,831 | - | - | - |
| delivery_date | object | 3,831 | - | - | - |
| shipping_fee | float64 | 1,856 | 0.00 | 32.00 | 4.96 |

---
## Bảng: web_traffic.csv
- **Số dòng:** 3,652
- **Số cột:** 7

### Dữ liệu bị khuyết (Missing Values)
*Không có dữ liệu bị khuyết.*

### Phân phối dữ liệu (Data Distribution)
| Cột | Kiểu | Unique Cnt | Min | Max | Mean |
| --- | --- | --- | --- | --- | --- |
| date | object | 3,652 | - | - | - |
| sessions | int64 | 3,447 | 7973 | 50947 | 25041.77 |
| unique_visitors | int64 | 3,382 | 6136 | 40430 | 19031.40 |
| page_views | int64 | 3,620 | 30451 | 275560 | 108615.22 |
| bounce_rate | float64 | 261 | 0.00 | 0.01 | 0.00 |
| avg_session_duration_sec | float64 | 1,771 | 100.10 | 319.90 | 210.28 |
| traffic_source | object | 6 | - | - | - |

---
