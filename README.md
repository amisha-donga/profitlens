# ProfitLens — E-Commerce Sales Data Analysis

> End-to-end data analysis project on Amazon India e-commerce sales data using Python, SQL, and Power BI.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0-darkblue?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-teal?style=flat)
![SQL](https://img.shields.io/badge/SQL-SQLite-green?style=flat&logo=sqlite)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?style=flat&logo=powerbi)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat)

---

## About the Project

ProfitLens is a data analyst portfolio project that analyses real-world Amazon India e-commerce sales data across 7 datasets covering domestic sales, international B2B orders, product pricing, expenses, and warehouse comparisons.

The goal is to extract actionable business insights from raw sales data using a complete end-to-end workflow — data loading, cleaning, exploratory analysis, SQL querying, and dashboard visualisation.

**Dataset source:** [Kaggle — Unlock Profits with E-Commerce Sales Data](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data)

---

## Key Business Questions Answered

- Which product category generates the most revenue?
- What is the monthly revenue trend and peak sales month?
- Which states drive the highest order volume?
- Who are the top international B2B customers?
- What is the B2B vs B2C order and revenue split?
- Which sizes sell the most in international markets?
- What does the expense breakdown look like by category?

---

## Datasets Used

| # | File | Records | Description |
|---|------|---------|-------------|
| 1 | Amazon Sale Report | 1,16,000+ orders | Domestic India sales (Mar–Jun 2022) |
| 2 | International Sale Report | 10,836 orders | International B2B customer orders |
| 3 | Expenses | 13 items | Business expense log |
| 4 | Sale Report | — | Product & SKU details |
| 5 | Pricing March 2021 | — | Historical pricing data |
| 6 | Pricing May 2022 | — | Current pricing data |
| 7 | Cloud Warehouse Comparison | — | Warehouse performance data |

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Data cleaning, EDA, visualisation |
| Pandas | Data manipulation and aggregation |
| Matplotlib & Seaborn | Charts and visual analysis |
| SQL (SQLite) | Querying and business analysis |
| Power BI | Interactive dashboard (in progress) |
| Jupyter Notebook | Analysis notebooks |
| Git & GitHub | Version control |

---

## Project Structure

```
profitlens/
├── data/
│   ├── raw/                        ← original source files
│   └── processed/                  ← cleaned CSV files
│
├── src/
│   ├── loaders/
│   │   └── data_loading.py         ← load all 7 files
│   ├── cleaning/
│   │   ├── amazon_sales_data_cleaning.py
│   │   ├── international_sales_data_cleaning.py
│   │   ├── expenses_data_cleaning.py
│   │   ├── products_data_cleaning.py
│   │   ├── pricing_march_2021_data_cleaning.py
│   │   ├── pricing_may_2022_data_cleaning.py
│   │   └── warehouse_comperison_data_cleaning.py
│   ├── analysis/
│   │   ├── data_analysis.ipynb              ← Amazon sales EDA (9 charts)
│   │   ├── international_sales_analysis.ipynb  ← International sales EDA (7 charts)
│   │   └── expenses_analysis.ipynb          ← Expense analysis (3 charts)
│   └── output/
│       ├── amazon_sales/           ← 9 saved chart PNGs
│       ├── expenses/               ← 3 saved chart PNGs
│       └── international_sales/    ← 7 saved chart PNGs
│
├── README.md
└── requirements.txt
```

---

## Analysis Completed

### Amazon Domestic Sales (1,16,000+ orders)
- Monthly revenue trend — peak month identified
- Revenue by product category
- Order status distribution (delivered vs cancelled)
- Top 10 states by revenue
- Orders by day of week
- Fulfillment method and service level breakdown
- Revenue heatmap — category × month
- B2B vs B2C orders and revenue comparison
- Order amount distribution (median vs mean)

### International Sales (10,836 orders | 118 customers)
- Monthly revenue and quantity trend (Jun 2021 – Apr 2022)
- Top 10 customers by gross revenue
- Top 10 product styles by revenue
- Size distribution — orders and revenue
- Customer × month revenue heatmap
- Order quantity and amount distribution
- Base amount vs gross amount monthly gap

### Expense Analysis (13 items | ₹8,095 total)
- Expense breakdown by item with % contribution
- Category-wise spend — donut and bar chart
- Pareto analysis — which items drive 80% of spend

---

## Key Insights

1. **May 2022** was the peak revenue month for domestic sales
2. **Set** and **Kurta** are the top-selling product categories
3. **Maharashtra, Karnataka** and **Uttar Pradesh** drive the most domestic revenue
4. **MULBERRIES BOUTIQUE** is the top international customer — drives 17.6% of international revenue
5. **L and M sizes** are the best-selling sizes in international orders
6. **Accommodation (32%) and Transport (27%)** together account for 60% of total expenses
7. B2C orders dominate domestic sales; international orders are 90% single-unit purchases

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amisha-donga/profitlens.git
cd profitlens

# 2. Install required libraries
pip install -r requirements.txt

# 3. Run notebooks in order
# Open Jupyter and run:
# src/analysis/data_analysis.ipynb
# src/analysis/international_sales_analysis.ipynb
# src/analysis/expenses_analysis.ipynb
```

---

## Requirements

```
pandas
matplotlib
seaborn
openpyxl
jupyter
```

---

## Work in Progress

- [x] Data loading scripts
- [x] Data cleaning scripts (7 files)
- [x] Amazon sales EDA notebook
- [x] International sales EDA notebook
- [x] Expense analysis notebook
- [ ] Remaining 4 dataset notebooks
- [ ] SQL analysis queries
- [ ] Power BI interactive dashboard
- [ ] Final insights report (PDF)

---

## Author

**Amisha**
Aspiring Data Analyst | Ahmedabad, Gujarat
[GitHub](https://github.com/amisha-donga)

---

*This project is part of my data analyst portfolio. Dataset used for educational and portfolio purposes only.*
