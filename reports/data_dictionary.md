# Data Dictionary

## Project

Mutual Fund Analytics – Bluestock Fintech Capstone Project

---

## Overview

This document describes the datasets used in the Mutual Fund Analytics project. It provides information about each dataset, its purpose, column names, data types, and descriptions.

---

# 1. Fund Master (`01_fund_master.csv`)

**Description:** Contains master information about all mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | String | Asset Management Company (AMC) |
| scheme_name | String | Name of the mutual fund scheme |
| category | String | Fund category |
| sub_category | String | Detailed scheme category |
| plan | String | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | String | Benchmark index |
| expense_ratio_pct | Float | Expense ratio (%) |
| exit_load_pct | Float | Exit load (%) |
| min_sip_amount | Float | Minimum SIP amount |
| min_lumpsum_amount | Float | Minimum lump sum investment |
| fund_manager | String | Fund manager name |
| risk_category | String | Risk category |
| sebi_category_code | String | SEBI category code |

---

# 2. NAV History (`02_nav_history.csv`)

**Description:** Historical Net Asset Value (NAV) records for mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

# 3. AUM by Fund House (`03_aum_by_fund_house.csv`)

**Description:** Assets Under Management (AUM) reported by each fund house.

| Column | Data Type | Description |
|----------|-----------|-------------|
| fund_house | String | Asset Management Company |
| date | Date | Reporting date |
| aum_cr | Float | Assets Under Management (₹ Crores) |

---

# 4. Monthly SIP Inflows (`04_monthly_sip_inflows.csv`)

**Description:** Monthly SIP investment statistics.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| sip_inflow_cr | Float | SIP inflow (₹ Crores) |
| active_sip_accounts_lakh | Float | Active SIP accounts (Lakhs) |
| yoy_growth_pct | Float | Year-over-Year growth (%) |

---

# 5. Category Inflows (`05_category_inflows.csv`)

**Description:** Monthly inflows categorized by mutual fund type.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| category | String | Mutual fund category |
| inflow_cr | Float | Category inflow (₹ Crores) |

---

# 6. Industry Folio Count (`06_industry_folio_count.csv`)

**Description:** Industry folio count by mutual fund category.

| Column | Data Type | Description |
|----------|-----------|-------------|
| month | Date | Reporting month |
| category | String | Mutual fund category |
| folio_count_lakh | Float | Investor folio count (Lakhs) |

---

# 7. Scheme Performance (`07_scheme_performance.csv`)

**Description:** Performance metrics of mutual fund schemes.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| returns_1y | Float | One-year return (%) |
| returns_3y | Float | Three-year CAGR (%) |
| returns_5y | Float | Five-year CAGR (%) |
| sharpe_ratio | Float | Sharpe Ratio |
| alpha | Float | Alpha |
| beta | Float | Beta |
| volatility | Float | Standard deviation of returns |

---

# 8. Investor Transactions (`08_investor_transactions.csv`)

**Description:** Individual investor transaction records.

| Column | Data Type | Description |
|----------|-----------|-------------|
| investor_id | String | Unique investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Mutual fund identifier |
| transaction_type | String | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction amount (₹) |
| state | String | Investor state |
| city | String | Investor city |
| city_tier | String | Tier classification |
| age_group | String | Investor age group |
| gender | String | Investor gender |
| annual_income_lakh | Float | Annual income (Lakhs) |
| payment_mode | String | Payment method |
| kyc_status | String | KYC verification status |

---

# 9. Portfolio Holdings (`09_portfolio_holdings.csv`)

**Description:** Equity holdings of mutual fund portfolios.

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| stock_symbol | String | Stock ticker |
| stock_name | String | Company name |
| sector | String | Industry sector |
| weight_pct | Float | Portfolio weight (%) |
| market_value_cr | Float | Market value (₹ Crores) |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

# 10. Benchmark Indices (`10_benchmark_indices.csv`)

**Description:** Historical benchmark index values.

| Column | Data Type | Description |
|----------|-----------|-------------|
| index_name | String | Benchmark index |
| date | Date | Trading date |
| close_price | Float | Closing index value |

---

# Data Source

All datasets were provided as part of the **Bluestock Fintech – Mutual Fund Analytics Capstone Project** and are used exclusively for educational and analytical purposes.

---

# Data Processing Summary

The following preprocessing steps were completed before loading the data into SQLite:

- Dataset inspection
- Data type validation
- Missing value analysis
- Duplicate record analysis
- Date conversion
- Data cleaning
- Data validation
- Processed dataset generation
- SQLite database integration

---

# Processed Data Location

```
data/processed/
```

The processed datasets are used for:

- SQL Analysis
- Exploratory Data Analysis (EDA)
- Dashboard Development
- Business Insights
- Reporting
