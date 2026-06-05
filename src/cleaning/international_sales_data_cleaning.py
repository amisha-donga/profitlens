import pandas as pd

i_sales = pd.read_excel("E:/Python/profitlens/data/raw/international_sales.xlsx", dtype=str)
print(f"Original raws : {len(i_sales)}")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(i_sales.shape)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# ----------------------Rename Columns----------------------
i_sales.rename(columns= {
    "DATE" : "order_date",
    "Months" : "order_month",
    "CUSTOMER" : "customer_name",
    "Style" : "style",
    "SKU" : "sku",
    "Size" : "product_size",
    "PCS" : "quantity",
    "RATE" : "amount",
    "GROSS AMT" : "gross_amount"
}, inplace=True)

# ----------------------Change Data Types----------------------
for col in ["quantity", "amount", "gross_amount"]:
    i_sales[col] = pd.to_numeric(i_sales[col], errors="coerce")

# fix Date
i_sales["order_date"] = i_sales["order_date"].astype(str).str.strip()

i_sales = i_sales[i_sales["order_date"].str.match(r'^\d{2}-\d{2}-(\d{2}|\d{4})$', na=False)].copy()
print(f"After removing junk rows : {len(i_sales)}")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


def fix_date(val):
    val = str(val).strip()
    if len(val) == 10:
        return pd.to_datetime(val, format='%m-%d-%Y')
    elif len(val) == 8:
        return pd.to_datetime(val, format='%m-%d-%y')
    return pd.NaT 

i_sales["order_date"] = i_sales["order_date"].apply(fix_date)

# ----------------------Remove unnecessary Column----------------------
i_sales.drop(["index"], axis=1, inplace=True)

print(i_sales.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Missing Values----------------------
print(i_sales.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Fix sku null data
print("SKU UNIQUE Values: ", i_sales["sku"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print("Product Size UNIQUE Values: ", i_sales["product_size"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# Free items -> label as FREE-ITEM
free = i_sales["sku"].isna() &  (i_sales["product_size"] == "FREE")
i_sales.loc[free, "sku"] = "FREE-ITEM"

# Other rows with missing sku -> build from style + product_size
missing = i_sales["sku"].isna()
i_sales.loc[missing, "sku"] = i_sales.loc[missing, "style"] + "-" + i_sales.loc[missing, "product_size"]

print(i_sales.isnull().sum())

# ----------------------Save Cleaned File----------------------

i_sales.to_csv("data/processed/international_sales_cleaned.csv", index=False)

print("Done! File Saved...")