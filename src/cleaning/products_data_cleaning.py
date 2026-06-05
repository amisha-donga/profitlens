import pandas as pd


# ----------------------Load CSV File----------------------
products = pd.read_csv("E:/Python/profitlens/data/raw/products.csv")
print(products.shape)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(products.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Rename Columns----------------------
products.rename(columns={
    "SKU Code" :"sku",
    "Design No." : "design_id",
    "Stock" : "stock",
    "Category" : "category",
    "Size" : "size",
    "Color" : "color"
}, inplace=True)


# ----------------------Change Data Types----------------------
products["stock"] = products["stock"].astype("Int64")
print(products.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# set column's value
print(products["color"].unique())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
products["color"] = products["color"].str.title()





# ----------------------Remove unnecessary Column----------------------
products.drop(["index"], axis=1, inplace=True)




# ----------------------Missing Values----------------------
print(products.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Drop fully empty rows
empty_row = ["sku", "design_id", "stock", "category", "size", "color"]
fully_empty = products[empty_row].isnull().all(axis=1)
products = products[~fully_empty]
print(f"Droppped {fully_empty.sum()} fully empty rows")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Reconstruct missing sku
missing = products["sku"].isna() & products["design_id"].notna() & products["color"].notna() & products["size"].notna()
products.loc[missing, "sku"] = (
    products.loc[missing, "design_id"] + "-" +
    products.loc[missing, "color"].str.upper().str.replace(" ", " ") + "-" +
    products.loc[missing, "size"]
)
print(f"Reconstructed {missing.sum()} missing sku")
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(products.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")

# Other missing values
for col in ["sku", "design_id", "category", "size", "color"]:
    products[col] = products[col].fillna("unknown")

print(products.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")
print(products.shape)
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Save Cleaned File----------------------
products.to_csv("data/processed/products_cleaned.csv", index=False)

print("Done! File Saved...")
