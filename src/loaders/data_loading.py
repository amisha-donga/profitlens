import pandas as pd

a_sales = pd.read_csv("E:/Python/profitlens/data/raw/amazon_sales.csv", low_memory=False)

# pd.set_option('display.max_columns', None) 
# print(a_sales.head(10))
# print(a_sales.isnull().sum())
# print(a_sales.info())
# print(a_sales.describe())

i_sales = pd.read_excel("E:/Python/profitlens/data/raw/international_sales.xlsx")

# print(i_sales.head())
# print(i_sales.isnull().sum())
# print(i_sales.info())
# print(i_sales.describe())

products = pd.read_csv("E:/Python/profitlens/data/raw/products.csv")

# print(products.head())
# print(products.isnull().sum())
# print(products.info())
# print(products.describe())

pricing_2021 = pd.read_csv("E:/Python/profitlens/data/raw/pricing_march_2021.csv")

# print(pricing_2021.head())
# print(pricing_2021.isnull().sum())
# print(pricing_2021.info())
# print(pricing_2021.describe())

pricing_2022 = pd.read_csv("E:/Python/profitlens/data/raw/pricing_may_2022.csv")

# print(pricing_2022.head())
# print(pricing_2022.isnull().sum())
# print(pricing_2022.info())
# print(pricing_2022.describe())

data= pd.read_csv("E:/Python/profitlens/data/raw/expenses.csv")

# print(data.head())
# print(data.isnull().sum())
# print(data.info())
# print(data.describe())

warehouse = pd.read_csv("E:/Python/profitlens/data/raw/warehouse_compersion.csv")

# print(warehouse.head())
# print(warehouse.isnull().sum())
# print(warehouse.info())
# print(warehouse.describe())
