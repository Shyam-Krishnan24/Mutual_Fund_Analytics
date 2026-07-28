import pandas as pd

# ============================================================
# 01_fund_master file
# ============================================================
print("============================================================")
print("01_fund_master")
print("============================================================")
df1 = pd.read_csv(r"data/raw/01_fund_master.csv")
print(df1.shape)
print(df1.dtypes)
print(df1.head())
print("The Missing values count are: ")
print(df1.isnull().sum())
print("The duplicate values count are: ")
print(df1.duplicated().sum())
print()


# ============================================================
# 02_nav_history
# ============================================================
print("============================================================")
print("02_nav_history")
print("============================================================")
df2 = pd.read_csv(r"data/raw/02_nav_history.csv")
print(df2.shape)
print(df2.dtypes)
print(df2.head())
print("The Missing values count are: ")
print(df2.isnull().sum())
print("The duplicate values count are: ")
print(df2.duplicated().sum())
print()


# ============================================================
# 03_aum_by_fund_house file
# ============================================================
print("============================================================")
print("03_aum_by_fund_house")
print("============================================================")
df3 = pd.read_csv(r"data/raw/03_aum_by_fund_house.csv")
print(df3.shape)
print(df3.dtypes)
print(df3.head())
print("The Missing values count are: ")
print(df3.isnull().sum())
print("The duplicate values count are: ")
print(df3.duplicated().sum())
print()


# ============================================================
# 04_monthly_sip_inflows
# ============================================================
print("============================================================")
print("04_monthly_sip_inflows")
print("============================================================")
df4 = pd.read_csv(r"data/raw/04_monthly_sip_inflows.csv")
print(df4.shape)
print(df4.dtypes)
print(df4.head())
print("The Missing values count are: ")
print(df4.isnull().sum())
print("The duplicate values count are: ")
print(df4.duplicated().sum())
print()


# ============================================================
# 05_category_inflows
# ============================================================
print("============================================================")
print("05_category_inflows")
print("============================================================")
df5 = pd.read_csv(r"data/raw/05_category_inflows.csv")
print(df5.shape)
print(df5.dtypes)
print(df5.head())
print("The Missing values count are: ")
print(df5.isnull().sum())
print("The duplicate values count are: ")
print(df5.duplicated().sum())
print()


# ============================================================
# 06_industry_folio_count
# ============================================================
print("============================================================")
print("06_industry_folio_count")
print("============================================================")
df6 = pd.read_csv(r"data/raw/06_industry_folio_count.csv")
print(df6.shape)
print(df6.dtypes)
print(df6.head())
print("The Missing values count are: ")
print(df6.isnull().sum())
print("The duplicate values count are: ")
print(df6.duplicated().sum())
print()


# ============================================================
# 07_scheme_performance
# ============================================================
print("============================================================")
print("07_scheme_performance")
print("============================================================")
df7 = pd.read_csv(r"data/raw/07_scheme_performance.csv")
print(df7.shape)
print(df7.dtypes)
print(df7.head())
print("The Missing values count are: ")
print(df7.isnull().sum())
print("The duplicate values count are: ")
print(df7.duplicated().sum())
print()


# ============================================================
# 08_investor_transactions
# ============================================================
print("============================================================")
print("08_investor_transactions")
print("============================================================")
df8 = pd.read_csv(r"data/raw/08_investor_transactions.csv")
print(df8.shape)
print(df8.dtypes)
print(df8.head())
print("The Missing values count are: ")
print(df8.isnull().sum())
print("The duplicate values count are: ")
print(df8.duplicated().sum())
print()


# ============================================================
# 09_portfolio_holdings
# ============================================================
print("============================================================")
print("09_portfolio_holdings")
print("============================================================")
df9 = pd.read_csv(r"data/raw/09_portfolio_holdings.csv")
print(df9.shape)
print(df9.dtypes)
print(df9.head())
print("The Missing values count are: ")
print(df9.isnull().sum())
print("The duplicate values count are: ")
print(df9.duplicated().sum())
print()

# ============================================================
# 10_benchmark_indices
# ============================================================
print("============================================================")
print("10_benchmark_indices")
print("============================================================")
df10 = pd.read_csv(r"data/raw/10_benchmark_indices.csv")
print(df10.shape)
print(df10.dtypes)
print(df10.head())
print("The Missing values count are: ")
print(df10.isnull().sum())
print("The duplicate values count are: ")
print(df10.duplicated().sum())
print()

