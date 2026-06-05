import pandas as pd

# ----------------------Load CSV File----------------------
pricing_2021 = pd.read_csv("E:/Python/profitlens/data/raw/pricing_march_2021.csv")
print(pricing_2021.shape)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(pricing_2021.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Rename Columns----------------------
pricing_2021.rename(columns={
    "Sku" : "sku",
    "Style Id" : "style",
    "Catalog" : "catalog",
    "Category" : "category",
    "Weight" : "weight",
    "TP 1" : "price_1",
    "TP 2" : "price_2",
    "MRP Old" : "old_price",
    "Final MRP Old" : "final_price",
    "Ajio MRP" : "ajio_price",
    "Amazon MRP" : "amazon_price",
    "Amazon FBA MRP" : "amazon_price_fba",
    "Flipkart MRP" : "flipkart_price",
    "Limeroad MRP" : "limeroad_price",
    "Myntra MRP" : "myntra_price",
    "Paytm MRP" : "paytm_price",
    "Snapdeal MRP" : "snapdeal_price"
}, inplace=True)


# ----------------------Change Data Types----------------------
for col in ["weight", "price_1", "price_2", "old_price", "final_price", "ajio_price", "amazon_price", "amazon_price_fba", "flipkart_price", "limeroad_price", "myntra_price", "paytm_price", "snapdeal_price"] :
    pricing_2021[col] = pd.to_numeric(pricing_2021[col], errors="coerce")


# ----------------------Remove unnecessary Column----------------------
pricing_2021.drop(["index"], axis=1, inplace=True)

print(pricing_2021.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(pricing_2021.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Missing Values----------------------
# print("catalog unique value:", pricing_2021["catalog"].unique())
# print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
# print("category unique value:", pricing_2021["category"].unique())
# print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

for col in ["catalog", "category"]:
    pricing_2021[col] = pricing_2021[col].replace(["Nill", "None"],"unknown")

print("catalog unique value:", pricing_2021["catalog"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print("category unique value:", pricing_2021["category"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# print("Weight umique value: ", pricing_2021["weight"].unique())
# print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

for col in ["weight", "price_1", "price_2", "old_price", "final_price", "ajio_price", "amazon_price", "amazon_price_fba", "flipkart_price", "limeroad_price", "myntra_price", "paytm_price", "snapdeal_price"] :
    pricing_2021[col] = pricing_2021[col].fillna(0)

print("Weight umique value: ", pricing_2021["weight"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


print(pricing_2021.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Save Cleaned File----------------------
pricing_2021.to_csv("data/processed/pricing_march_2021_cleaned.csv", index=False)

print("Done! File Saved...")

