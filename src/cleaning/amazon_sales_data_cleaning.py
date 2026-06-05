import pandas as pd
import os

# ------------------Amazon_sales.CSV File Cleaning--------------------------------------------------------
a_sales = pd.read_csv("E:/Python/profitlens/data/raw/amazon_sales.csv", low_memory=False)
print(a_sales.head(10))
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# ----------------------Rename Columns----------------------
a_sales.rename(columns= {
    "Order ID" : "order_id",
    "Date" : "order_date",
    "Status" : "order_status",
    "Fulfilment" : "fulfillment",
    "Sales Channel " : "sales_channel",
    "ship-service-level" : "service_level",
    "Style" : "style",
    "SKU" : "sku",
    "Category" : "category",
    "Size" : "product_size",
    "ASIN" : "asin",
    "Courier Status" : "courier_status",
    "Qty" : "quantity",
    "Amount" : "amount",
    "ship-city" : "city",
    "ship-state" : "state",
    "ship-postal-code" : "postal_code",
    "ship-country" : "country",
    "promotion-ids" : "promotion_ids"
}, inplace=True)


# ----------------------Remove unnecessary Columns----------------------
a_sales.drop(["index", "promotion_ids", "fulfilled-by", "Unnamed: 22"], axis=1, inplace=True)
print(a_sales.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# ----------------------Change Data Types----------------------
a_sales["order_date"] = pd.to_datetime(a_sales["order_date"])
a_sales["postal_code"] = a_sales["postal_code"].fillna("").astype(str)
print(a_sales.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# ----------------------Missing Values----------------------
print(a_sales.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Clean Currency Column
print(a_sales["currency"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

print(a_sales["currency"].value_counts())
a_sales["currency"] = a_sales["currency"].fillna("INR")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Clean city column
a_sales["city"] = a_sales["city"].str.lower().str.strip()

# Mapping Accuracy
city_check = a_sales.groupby("postal_code")["city"].nunique()
print(city_check)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

city_issue = city_check[city_check>1]
print(city_issue)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# calculate Accuracy
total = len(city_check)
consistent = (city_check == 1).sum()
accuracy = (consistent/total) * 100
print(f"Mapping Accuracy : {accuracy : 2f} %")

a_sales["city"] = a_sales["city"].fillna("unkown")

print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Clean State column
a_sales["state"] = a_sales["state"].str.lower().str.strip()
a_sales["state"] = a_sales["state"].fillna("unknown")

# Clean country column
print(a_sales["country"].unique())
a_sales["country"] = a_sales["country"].fillna("IN")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Clean courier_status column
print(a_sales["courier_status"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Clean courier_status column
print(a_sales["courier_status"].value_counts())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# Clean amount column
clean_sale = a_sales[
    (a_sales["amount"].notna()) &
    (a_sales["quantity"] > 0)
]
print(clean_sale["amount"].isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

print(a_sales.shape)
print(clean_sale.shape)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

print(clean_sale.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


os.makedirs("data", exist_ok=True)
clean_sale.to_csv("data/processed/amazon_sales_cleaned.csv", index=False)
print("\nDone! File Saved...")