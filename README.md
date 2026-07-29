---

# 📚 Data Dictionary

This section documents the datasets used in the project, including their purpose, source, and schema. The data dictionary serves as a reference for understanding the structure of each dataset and ensures consistency during data analysis and dashboard development.

---

## Dataset Source

All datasets used in this project were provided as part of the **Bluestock Fintech – Mutual Fund Analytics Capstone Project**. The datasets represent different aspects of the Indian mutual fund ecosystem, including fund details, NAV history, investor transactions, portfolio holdings, inflows, and benchmark performance.

---

## 1. Fund Master (`01_fund_master.csv`)

**Description:** Contains master information about mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Unique AMFI identifier for each mutual fund scheme |
| fund_house | String | Name of the Asset Management Company (AMC) |
| scheme_name | String | Name of the mutual fund scheme |
| category | String | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category | String | Detailed scheme classification |
| plan | String | Regular or Direct plan |
| launch_date | Date | Scheme launch date |
| benchmark | String | Benchmark index followed by the scheme |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load charged (%) |
| min_sip_amount | Float | Minimum SIP investment amount |
| min_lumpsum_amount | Float | Minimum lump sum investment |
| fund_manager | String | Name of the fund manager |
| risk_category | String | Risk classification assigned to the scheme |
| sebi_category_code | String | SEBI classification code |

---

## 2. NAV History (`02_nav_history.csv`)

**Description:** Historical Net Asset Value (NAV) records for mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| date | Date | NAV recording date |
| nav | Float | Net Asset Value |

---

## 3. AUM by Fund House (`03_aum_by_fund_house.csv`)

**Description:** Assets Under Management (AUM) of fund houses.

| Column | Data Type | Description |
|----------|-----------|-------------|
| fund_house | String | Asset Management Company |
| date | Date | Reporting date |
| aum_cr | Float | Assets Under Management (₹ Crores) |

---

## 4. Monthly SIP Inflows (`04_monthly_sip_inflows.csv`)

**Description:** Monthly SIP investment inflows.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| sip_inflow_cr | Float | SIP inflow (₹ Crores) |
| active_sip_accounts_lakh | Float | Active SIP accounts (Lakhs) |
| yoy_growth_pct | Float | Year-over-Year growth percentage |

---

## 5. Category Inflows (`05_category_inflows.csv`)

**Description:** Monthly inflows categorized by mutual fund type.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| category | String | Mutual fund category |
| inflow_cr | Float | Monthly inflow (₹ Crores) |

---

## 6. Industry Folio Count (`06_industry_folio_count.csv`)

**Description:** Number of investor folios across categories.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| category | String | Mutual fund category |
| folio_count_lakh | Float | Investor folio count (Lakhs) |

---

## 7. Scheme Performance (`07_scheme_performance.csv`)

**Description:** Performance metrics of mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| returns_1y | Float | One-year return (%) |
| returns_3y | Float | Three-year CAGR (%) |
| returns_5y | Float | Five-year CAGR (%) |
| sharpe_ratio | Float | Risk-adjusted return measure |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| volatility | Float | Standard deviation of returns |

---

## 8. Investor Transactions (`08_investor_transactions.csv`)

**Description:** Individual investor transaction records.

| Column | Data Type | Description |
|----------|-----------|-------------|
| investor_id | String | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Mutual fund identifier |
| transaction_type | String | Purchase / Redemption / SIP |
| amount_inr | Float | Transaction amount (₹) |
| state | String | Investor state |
| city | String | Investor city |
| city_tier | String | Tier classification |
| age_group | String | Investor age group |
| gender | String | Investor gender |
| annual_income_lakh | Float | Annual income (Lakhs) |
| payment_mode | String | Mode of payment |
| kyc_status | String | KYC verification status |

---

## 9. Portfolio Holdings (`09_portfolio_holdings.csv`)

**Description:** Equity holdings of mutual fund portfolios.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| stock_symbol | String | Stock ticker |
| stock_name | String | Company name |
| sector | String | Business sector |
| weight_pct | Float | Portfolio weight (%) |
| market_value_cr | Float | Market value (₹ Crores) |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

## 10. Benchmark Indices (`10_benchmark_indices.csv`)

**Description:** Historical benchmark index values used for comparison.

| Column | Data Type | Description |
|----------|-----------|-------------|
| index_name | String | Benchmark index |
| date | Date | Trading date |
| close_price | Float | Closing index value |

---

## Data Quality Summary

The following preprocessing steps were performed before loading the data into the SQLite database:

- ✔️ Dataset inspection
- ✔️ Data type verification
- ✔️ Missing value analysis
- ✔️ Duplicate record analysis
- ✔️ Missing value imputation
- ✔️ Date format standardization
- ✔️ Data validation
- ✔️ Clean dataset generation
- ✔️ SQLite database integration

---

## Processed Data

All cleaned datasets are stored in:

```text
data/processed/
```

The processed datasets are used for:

- SQL Analytics
- Exploratory Data Analysis (EDA)
- Power BI Dashboard
- Business Insight Generation
- Performance Reporting

---