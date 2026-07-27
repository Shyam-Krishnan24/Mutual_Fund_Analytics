# Mutual Fund Analytics

## Project Overview

This project focuses on cleaning, processing, and analyzing mutual fund datasets to build an analytics dashboard and derive meaningful insights from the Indian mutual fund industry.

---

## Project Structure

```
MutualFundAnalytics/
│
├── data/
│   ├── raw/           # Original datasets
│   └── processed/     # Cleaned datasets
│
├── scripts/           # Data cleaning scripts
├── notebooks/         # Exploratory Data Analysis
├── dashboard/         # Power BI/Tableau dashboard
├── README.md
└── requirements.txt
```

---

## Data Cleaning Log

### Step 1: Dataset Inspection

Performed an initial inspection of all datasets present in the `data/raw` directory.

The following checks were completed for every CSV file:

- Dataset shape (rows × columns)
- Data types
- Preview of the first five records
- Missing value count
- Duplicate row count

This helped understand the structure and quality of each dataset before cleaning.

---

### Step 2: Missing Value Handling

Identified missing values across all datasets.

Currently completed:

- `04_monthly_sip_inflows.csv`
  - Filled missing values in the `yoy_growth_pct` column using the column mean.

```python
df["yoy_growth_pct"] = df["yoy_growth_pct"].fillna(
    df["yoy_growth_pct"].mean()
)
```

---

### Step 3: Date Conversion

Created a mapping of datasets to their respective date columns.

Converted all date-related columns from string format to `datetime`.

Converted columns include:

| Dataset | Date Column |
|----------|-------------|
| 01_fund_master.csv | launch_date |
| 02_nav_history.csv | date |
| 03_aum_by_fund_house.csv | date |
| 04_monthly_sip_inflows.csv | month |
| 05_category_inflows.csv | month |
| 06_industry_folio_count.csv | month |
| 08_investor_transactions.csv | transaction_date |
| 09_portfolio_holdings.csv | portfolio_date |
| 10_benchmark_indices.csv | date |

---

### Step 4: Processed Dataset Generation

After cleaning:

- Missing values handled
- Date columns converted

All cleaned datasets are saved into:

```
data/processed/
```

Original datasets remain unchanged in:

```
data/raw/
```

---

## Cleaning Tasks Completed

- Dataset inspection
- Data type verification
- Missing value analysis
- Duplicate value analysis
- Missing value imputation (`yoy_growth_pct`)
- Date column conversion
- Processed dataset generation

---

## Tasks Planned

The following steps are planned for the next phase:

- Data validation
- Outlier detection
- Exploratory Data Analysis (EDA)
- Feature engineering
- SQL database integration
- Dashboard development
- Business insights and reporting

---

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- SQL (planned)
- Power BI / Tableau (planned)

---

## Author

Developed as part of the **Bluestock Fintech – Mutual Fund Analytics Internship**.