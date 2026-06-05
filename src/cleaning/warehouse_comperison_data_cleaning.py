import pandas as pd
import numpy as np

warehouse = pd.read_csv("E:/Python/profitlens/data/raw/warehouse_compersion.csv")
print(warehouse.shape)
print(warehouse.head(10))
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


def clean_text(s):
    """Strip whitespace and bullet characters from a string"""
    if pd.isna(s):
        return np.nan
    return str(s).strip().lstrip("•").strip()

# TABLE 1 — PRICING COMPARISO═════════════════════════════════════════════════════════════════════
pricing_warehouse = warehouse.iloc[1:5][["Shiprocket", "Unnamed: 1", "INCREFF"]].copy()
pricing_warehouse.columns = ["Service", "Shiprocket_Price", "INCREFF_Price"]

pricing_warehouse["Shiprocket_Price"] = pricing_warehouse["Shiprocket_Price"].str.replace("₹", "", regex=False).str.strip()
pricing_warehouse["Service"] = pricing_warehouse["Service"].str.strip()
pricing_warehouse["INCREFF_Price"] = pricing_warehouse["INCREFF_Price"].str.strip()
pricing_warehouse = pricing_warehouse.reset_index(drop=True)

print("=== TABLE 1: PRICING COMPARISON ===")
print(pricing_warehouse.to_string(index=False))
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# TABLE 2 — SCOPE OF WORK / SOP (rows 5–23)═══════════════════════════════════════════════════════
sop_warehouse = warehouse.iloc[6:24][["Shiprocket", "Unnamed: 1", "INCREFF"]].copy()
sop_warehouse.columns = ["Section", "Sub_Step", "Description"]

sop_warehouse["Section"] = sop_warehouse["Section"].ffill()

sop_warehouse = sop_warehouse[~(sop_warehouse["Sub_Step"].isna() & sop_warehouse["Description"].isna())]

for col in ["Section", "Sub_Step", "Description"]:
    sop_warehouse[col] = sop_warehouse[col].apply(clean_text)

sop_warehouse = sop_warehouse.reset_index(drop=True)

print("\n=== TABLE 2: SCOPE OF WORK (SOP) ===")
print(sop_warehouse.to_string(index=False))
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# TABLE 3 — KPI & COMMERCIALS (rows 37–49)════════════════════════════════════════════════════════
kpi_warehouse = warehouse.iloc[38:50][["Shiprocket", "Unnamed: 1", "INCREFF"]].copy()
kpi_warehouse.columns = ["Performance_Measure", "Measurement", "Target"]

kpi_warehouse["Performance_Measure"] = kpi_warehouse["Performance_Measure"].ffill()

kpi_warehouse = kpi_warehouse[kpi_warehouse["Measurement"].notna()]

for col in ["Performance_Measure", "Measurement", "Target"]:
    kpi_warehouse[col] = kpi_warehouse[col].apply(clean_text)

kpi_warehouse = kpi_warehouse.reset_index(drop=True)

print("\n=== TABLE 3: KPI & COMMERCIALS ===")
print(kpi_warehouse.to_string(index=False))
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Save Cleaned File----------------------
pricing_warehouse.to_csv("data/processed/pricing_comparison_cleaned.csv", index=False)
print("Saved: pricing_comparison_cleaned.csv")

sop_warehouse.to_csv("data/processed/scope_of_work_cleaned.csv", index=False)
print("Saved: scope_of_work_cleaned.csv")

kpi_warehouse.to_csv("data/processed/kpi_commercials_cleaned.csv", index=False)
print("Saved: kpi_commercials_cleaned.csv")
