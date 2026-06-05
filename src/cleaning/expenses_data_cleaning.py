import pandas as pd

# ----------------------Load CSV File----------------------
data = pd.read_csv("E:/Python/profitlens/data/raw/expenses.csv")
print(data.shape)
print(data.info())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------RECEIVED AMOUNTS TABLE----------------------
received_data = data[["Recived Amount", "Unnamed: 1"]].copy()
received_data.columns = ["Date", "Amount"]

received_data = received_data[received_data["Date"] != "Particular"]
received_data = received_data[received_data["Date"].notna()]

received_data.rename(columns={
    "Date" : "date",
    "Amount" : "amount"
}, inplace=True)

total_received_data = received_data[received_data["date"] == "Total"]
received = received_data[received_data["date"] != "Total"].copy()

received["date"] = pd.to_datetime(received["date"], format="%m-%d-%y")
received["amount"] = pd.to_numeric(received["amount"], errors="coerce").astype("Int64")
received = received.reset_index(drop=True)

total_received = int(total_received_data["amount"].values[0])

print("=== RECEIVED AMOUNTS ===")
print(received.to_string(index=False))
print(f"\nTotal Received: {total_received}")
print(received.info())
print(received.shape)
print(received.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------EXPENSES TABLE----------------------
expenses_data = data[["Expance", "Unnamed: 3"]].copy()
expenses_data.columns = ["Particular", "Amount"]

expenses_data = expenses_data[expenses_data["Particular"] != "Particular"]

expenses_data.rename(columns={
    "Particular" : "particular",
    "Amount" : "amount"
},inplace=True)

subtotal_data = expenses_data[expenses_data["particular"].isna() & expenses_data["amount"].notna()].head(1)
pending_data = expenses_data[expenses_data["particular"] == "Pending Amount"]

expenses = expenses_data[
    expenses_data["particular"].notna() &
    (expenses_data["particular"] != "Pending Amount")
].copy()
 
expenses["amount"] = pd.to_numeric(expenses["amount"], errors="coerce").astype("Int64")
expenses = expenses.reset_index(drop=True)

subtotal_expenses = int(pd.to_numeric(subtotal_data["amount"].values[0]))
pending_expenses = int(pd.to_numeric(pending_data["amount"].values[0]))

print("\n=== EXPENSES ===")
print(expenses.to_string(index=False))
print(f"\nTotal Expenses : {subtotal_expenses}")
print(f"Pending Amount : {pending_expenses}")
print(expenses.info())
print(expenses.shape)
print(expenses.isnull().sum())
print("=    =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =")


# ----------------------Save Cleaned File----------------------
received.to_csv("data/processed/received_amounts_cleaned.csv", index=False)
print("\nSaved: received_amounts_cleaned.csv")

expenses.to_csv("data/processed/expenses_cleaned.csv", index=False)
print("Saved: expenses_cleaned.csv")
