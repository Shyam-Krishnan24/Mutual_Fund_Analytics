from pathlib import Path
import pandas as pd

# ==========================================================
# Project Paths
# ==========================================================

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Create processed folder if it doesn't exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Debug Information
# ==========================================================

print("=" * 60)
print("TASK 1 - CLEAN NAV HISTORY")
print("=" * 60)

print("\nProject Directory :", BASE_DIR)
print("Raw Directory     :", RAW_DIR)
print("Processed Folder  :", PROCESSED_DIR)

csv_path = RAW_DIR / "02_nav_history.csv"

print("CSV File Exists   :", csv_path.exists())

if not csv_path.exists():
    raise FileNotFoundError(f"\nDataset not found:\n{csv_path}")

# ==========================================================
# Load Dataset
# ==========================================================

nav = pd.read_csv(csv_path)

print(f"\nOriginal Shape : {nav.shape}")

# ==========================================================
# Convert Date Column
# ==========================================================

nav["date"] = pd.to_datetime(nav["date"])

# ==========================================================
# Sort Data
# ==========================================================

nav = nav.sort_values(
    by=["amfi_code", "date"]
)

# ==========================================================
# Remove Duplicate Rows
# ==========================================================

duplicates = nav.duplicated().sum()

print(f"\nDuplicate Rows : {duplicates}")

nav = nav.drop_duplicates()

# ==========================================================
# Forward Fill Missing NAV Values
# ==========================================================

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# ==========================================================
# Validate NAV Values
# ==========================================================

invalid_nav = nav[nav["nav"] <= 0]

print(f"Invalid NAV Records : {len(invalid_nav)}")

# ==========================================================
# Missing Values
# ==========================================================

print("\nMissing Values")

print(nav.isnull().sum())

# ==========================================================
# Dataset Information
# ==========================================================

print("\nDataset Info")

print(nav.info())

# ==========================================================
# Save Clean Dataset
# ==========================================================

output_file = PROCESSED_DIR / "clean_nav.csv"

nav.to_csv(output_file, index=False)

print("\nClean dataset saved successfully!")

print(output_file)

print(f"\nFinal Shape : {nav.shape}")

print("=" * 60)
print("NAV CLEANING COMPLETED")
print("=" * 60)



# ==========================================================
# TASK 2 - CLEAN INVESTOR TRANSACTIONS
# ==========================================================

print("\n" + "=" * 60)
print("TASK 2 - CLEAN INVESTOR TRANSACTIONS")
print("=" * 60)

transaction_path = RAW_DIR / "08_investor_transactions.csv"

transactions = pd.read_csv(transaction_path)

print(f"\nOriginal Shape : {transactions.shape}")

# ----------------------------------------------------------
# Convert Transaction Date
# ----------------------------------------------------------

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# ----------------------------------------------------------
# Remove Duplicate Rows
# ----------------------------------------------------------

duplicates = transactions.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

transactions = transactions.drop_duplicates()

# ----------------------------------------------------------
# Remove Leading/Trailing Spaces
# ----------------------------------------------------------

string_columns = transactions.select_dtypes(include="object").columns

for col in string_columns:
    transactions[col] = transactions[col].str.strip()

# ----------------------------------------------------------
# Standardize Text Columns
# ----------------------------------------------------------

transactions["transaction_type"] = transactions["transaction_type"].str.title()

transactions["payment_mode"] = transactions["payment_mode"].str.title()

transactions["kyc_status"] = transactions["kyc_status"].str.title()

transactions["gender"] = transactions["gender"].str.title()

transactions["city_tier"] = transactions["city_tier"].str.upper()

# ----------------------------------------------------------
# Validate Amount
# ----------------------------------------------------------

invalid_amount = transactions[transactions["amount_inr"] <= 0]

print(f"Invalid Amount Records : {len(invalid_amount)}")

# ----------------------------------------------------------
# Validate Income
# ----------------------------------------------------------

invalid_income = transactions[
    transactions["annual_income_lakh"] < 0
]

print(f"Invalid Income Records : {len(invalid_income)}")

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\nMissing Values")

print(transactions.isnull().sum())

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nDataset Info")

print(transactions.info())

# ----------------------------------------------------------
# Save Clean Dataset
# ----------------------------------------------------------

output_file = PROCESSED_DIR / "clean_investor_transactions.csv"

transactions.to_csv(output_file, index=False)

print("\nClean dataset saved successfully!")

print(output_file)

print(f"\nFinal Shape : {transactions.shape}")

print("=" * 60)
print("INVESTOR TRANSACTIONS CLEANING COMPLETED")
print("=" * 60)

# ==========================================================
# TASK 3 - CLEAN PORTFOLIO HOLDINGS
# ==========================================================

print("\n" + "=" * 60)
print("TASK 3 - CLEAN PORTFOLIO HOLDINGS")
print("=" * 60)

portfolio_path = RAW_DIR / "09_portfolio_holdings.csv"

if not portfolio_path.exists():
    raise FileNotFoundError(f"\nDataset not found:\n{portfolio_path}")

portfolio = pd.read_csv(portfolio_path)

print(f"\nOriginal Shape : {portfolio.shape}")

# ----------------------------------------------------------
# Convert Portfolio Date
# ----------------------------------------------------------

portfolio["portfolio_date"] = pd.to_datetime(portfolio["portfolio_date"])

# ----------------------------------------------------------
# Remove Duplicate Rows
# ----------------------------------------------------------

duplicates = portfolio.duplicated().sum()
print(f"Duplicate Rows : {duplicates}")
portfolio = portfolio.drop_duplicates()

# ----------------------------------------------------------
# Trim String Columns
# ----------------------------------------------------------

string_columns = portfolio.select_dtypes(include="object").columns
for col in string_columns:
    portfolio[col] = portfolio[col].str.strip()

# ----------------------------------------------------------
# Standardize Text Columns
# ----------------------------------------------------------

portfolio["stock_symbol"] = portfolio["stock_symbol"].str.upper()
portfolio["stock_name"] = portfolio["stock_name"].str.title()
portfolio["sector"] = portfolio["sector"].str.title()

# ----------------------------------------------------------
# Sort and Reorder
# ----------------------------------------------------------

portfolio = portfolio.sort_values(by=["amfi_code", "portfolio_date", "stock_symbol"])

# ----------------------------------------------------------
# Validate Numeric Values
# ----------------------------------------------------------

invalid_weights = portfolio[portfolio["weight_pct"] < 0]
invalid_market_value = portfolio[portfolio["market_value_cr"] < 0]
invalid_price = portfolio[portfolio["current_price_inr"] <= 0]

print(f"Invalid Weight Records : {len(invalid_weights)}")
print(f"Invalid Market Value Records : {len(invalid_market_value)}")
print(f"Invalid Current Price Records : {len(invalid_price)}")

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\nMissing Values")
print(portfolio.isnull().sum())

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nDataset Info")
print(portfolio.info())

# ----------------------------------------------------------
# Save Clean Dataset
# ----------------------------------------------------------

output_file = PROCESSED_DIR / "clean_portfolio_holdings.csv"
portfolio.to_csv(output_file, index=False)

print("\nClean dataset saved successfully!")
print(output_file)
print(f"\nFinal Shape : {portfolio.shape}")

print("=" * 60)
print("PORTFOLIO HOLDINGS CLEANING COMPLETED")
print("=" * 60)


# ==========================================================
# TASK 4 - CLEAN FUND MASTER
# ==========================================================

print("\n" + "=" * 60)
print("TASK 4 - CLEAN FUND MASTER")
print("=" * 60)

fund_path = RAW_DIR / "01_fund_master.csv"

fund = pd.read_csv(fund_path)

print(f"\nOriginal Shape : {fund.shape}")

fund["launch_date"] = pd.to_datetime(fund["launch_date"])

fund = fund.drop_duplicates()

string_cols = fund.select_dtypes(include="object").columns

for col in string_cols:
    fund[col] = fund[col].str.strip()

fund["fund_house"] = fund["fund_house"].str.title()
fund["scheme_name"] = fund["scheme_name"].str.title()
fund["category"] = fund["category"].str.title()
fund["plan"] = fund["plan"].str.title()
fund["risk_category"] = fund["risk_category"].str.title()

print(fund.isnull().sum())

fund.to_csv(PROCESSED_DIR / "clean_fund_master.csv", index=False)

print("Fund Master cleaned successfully!")

# ==========================================================
# TASK 5 - CLEAN AUM BY FUND HOUSE
# ==========================================================

print("\n" + "=" * 60)
print("TASK 5 - CLEAN AUM BY FUND HOUSE")
print("=" * 60)

aum_path = RAW_DIR / "03_aum_by_fund_house.csv"

aum = pd.read_csv(aum_path)

aum["date"] = pd.to_datetime(aum["date"])

aum = aum.drop_duplicates()

aum["fund_house"] = aum["fund_house"].str.strip().str.title()

numeric_cols = ["aum_lakh_crore", "aum_crore", "num_schemes"]

for col in numeric_cols:
    aum = aum[aum[col] >= 0]

print(aum.isnull().sum())

aum.to_csv(PROCESSED_DIR / "clean_aum_by_fund_house.csv", index=False)

print("AUM Dataset cleaned successfully!")

# ==========================================================
# TASK 6 - CLEAN MONTHLY SIP INFLOWS
# ==========================================================

print("\n" + "=" * 60)
print("TASK 6 - CLEAN MONTHLY SIP INFLOWS")
print("=" * 60)

sip_path = RAW_DIR / "04_monthly_sip_inflows.csv"

sip = pd.read_csv(sip_path)

sip["month"] = pd.to_datetime(sip["month"])

sip = sip.drop_duplicates()

numeric_cols = sip.columns.drop("month")

for col in numeric_cols:
    sip = sip[sip[col] >= 0]

print(sip.isnull().sum())

sip.to_csv(PROCESSED_DIR / "clean_monthly_sip_inflows.csv", index=False)

print("Monthly SIP cleaned successfully!")

# ==========================================================
# TASK 7 - CLEAN CATEGORY INFLOWS
# ==========================================================

print("\n" + "=" * 60)
print("TASK 7 - CLEAN CATEGORY INFLOWS")
print("=" * 60)

category_path = RAW_DIR / "05_category_inflows.csv"

category = pd.read_csv(category_path)

category["month"] = pd.to_datetime(category["month"])

category = category.drop_duplicates()

category["category"] = category["category"].str.strip().str.title()

print(category.isnull().sum())

category.to_csv(PROCESSED_DIR / "clean_category_inflows.csv", index=False)

print("Category Inflows cleaned successfully!")

# ==========================================================
# TASK 8 - CLEAN INDUSTRY FOLIO COUNT
# ==========================================================

print("\n" + "=" * 60)
print("TASK 8 - CLEAN INDUSTRY FOLIO COUNT")
print("=" * 60)

folio_path = RAW_DIR / "06_industry_folio_count.csv"

folio = pd.read_csv(folio_path)

folio["month"] = pd.to_datetime(folio["month"])

folio = folio.drop_duplicates()

numeric_cols = folio.columns.drop("month")

for col in numeric_cols:
    folio = folio[folio[col] >= 0]

print(folio.isnull().sum())

folio.to_csv(PROCESSED_DIR / "clean_industry_folio_count.csv", index=False)

print("Industry Folio Count cleaned successfully!")

# ==========================================================
# TASK 9 - CLEAN SCHEME PERFORMANCE
# ==========================================================

print("\n" + "=" * 60)
print("TASK 9 - CLEAN SCHEME PERFORMANCE")
print("=" * 60)

scheme_path = RAW_DIR / "07_scheme_performance.csv"

scheme = pd.read_csv(scheme_path)

scheme = scheme.drop_duplicates()

string_cols = scheme.select_dtypes(include="object").columns

for col in string_cols:
    scheme[col] = scheme[col].str.strip()

scheme["scheme_name"] = scheme["scheme_name"].str.title()
scheme["fund_house"] = scheme["fund_house"].str.title()
scheme["category"] = scheme["category"].str.title()
scheme["plan"] = scheme["plan"].str.title()

print(scheme.isnull().sum())

scheme.to_csv(PROCESSED_DIR / "clean_scheme_performance.csv", index=False)

print("Scheme Performance cleaned successfully!")

# ==========================================================
# TASK 10 - CLEAN BENCHMARK INDICES
# ==========================================================

print("\n" + "=" * 60)
print("TASK 10 - CLEAN BENCHMARK INDICES")
print("=" * 60)

benchmark_path = RAW_DIR / "10_benchmark_indices.csv"

benchmark = pd.read_csv(benchmark_path)

benchmark["date"] = pd.to_datetime(benchmark["date"])

benchmark = benchmark.drop_duplicates()

string_cols = benchmark.select_dtypes(include="object").columns

for col in string_cols:
    benchmark[col] = benchmark[col].str.strip()

print(benchmark.isnull().sum())

benchmark.to_csv(PROCESSED_DIR / "clean_benchmark_indices.csv", index=False)

print("Benchmark cleaned successfully!")