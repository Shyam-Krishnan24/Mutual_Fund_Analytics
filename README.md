# 📊 Mutual Fund Analytics

A comprehensive data analytics project developed as part of the **Bluestock Fintech Mutual Fund Analytics Internship**. This project focuses on collecting, cleaning, analyzing, and visualizing Indian mutual fund data to generate meaningful business insights through SQL, Python, and Power BI.

---

# 📌 Project Overview

The objective of this project is to analyze mutual fund datasets and build an interactive analytics dashboard that helps understand fund performance, investor behavior, market trends, and portfolio allocation.

The project follows a complete Data Analytics workflow:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQLite Database Integration
- SQL Analytics
- Performance Analysis
- Power BI Dashboard Development

---

# 🎯 Project Objectives

- Clean and preprocess mutual fund datasets.
- Validate data quality and consistency.
- Perform exploratory data analysis.
- Analyze fund performance using financial metrics.
- Store processed data in SQLite.
- Execute SQL-based analytical queries.
- Build an interactive Power BI dashboard.
- Generate actionable business insights.

---

# 📁 Project Structure

```
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── mutual_fund.db
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── data_cleaning.py
│   ├── database_setup.py
│   ├── load_to_sqlite.py
│   └── queries.py
│
├── notebooks/
│   ├── Day1_EDA.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│
├── reports/
│   ├── EDA_Findings.md
│   └── fund_scorecard.csv
│
├── README.md
├── data_dictionary.md
└── requirements.txt
```

---

# 📂 Datasets Used

The project uses ten datasets covering different aspects of the Indian Mutual Fund industry.

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

# 🛠 Technologies Used

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLite3
- SQLAlchemy
- Requests

### Database

- SQLite

### Visualization

- Power BI

### Development Tools

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

# ⚙️ Project Workflow

## Day 1 – Data Ingestion

- Created project structure.
- Loaded all datasets using Pandas.
- Explored datasets.
- Fetched live NAV data using MFAPI.
- Validated AMFI codes.
- Generated initial EDA notebook.

---

## Day 2 – Data Cleaning

- Cleaned all datasets.
- Removed duplicate records.
- Converted date columns.
- Handled missing values.
- Standardized text columns.
- Created processed datasets.
- Built SQLite database.
- Loaded cleaned data into SQLite.

---

## Day 3 – Exploratory Data Analysis

Performed exploratory analysis including:

- NAV Trend Analysis
- AUM Growth Analysis
- SIP Inflow Analysis
- Category-wise Inflow Analysis
- Investor Demographics
- State-wise Investment Analysis
- Industry Folio Analysis
- Benchmark Analysis
- Correlation Analysis

Generated:

- EDA notebook
- Business observations
- EDA findings report

---

## Day 4 – Fund Performance Analytics

Analyzed fund performance using:

- 1-Year Returns
- 3-Year Returns
- 5-Year Returns
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Expense Ratio
- Fund Scorecard

Generated performance reports and ranking analysis.

---

## Day 5 – Dashboard Development

Power BI dashboard includes:

### Executive Dashboard

- Total Mutual Funds
- Total Fund Houses
- Total AUM
- Total Investors
- NAV Trend
- Category Distribution
- Risk Analysis

### Fund Performance

- Top Performing Funds
- Sharpe Ratio Analysis
- Alpha vs Beta
- Fund Rankings
- Expense Ratio Analysis

### Investor Analytics

- State-wise Investments
- Gender Distribution
- Age Group Analysis
- City Tier Analysis
- Transaction Analysis

### Market Analysis

- SIP Trend
- Industry Folio Growth
- Benchmark Performance
- Portfolio Sector Allocation

---

# 📈 SQL Analytics

Implemented SQL queries to analyze:

- Latest NAV
- Highest NAV Funds
- State-wise Investments
- Transaction Distribution
- Sector Allocation
- Gender Distribution
- City Tier Analysis
- Average Investment
- Portfolio Holdings
- Risk Categories

---

# 📊 Key Insights

- Mutual fund investments show consistent long-term growth.
- SIP inflows have increased significantly over time.
- Large-cap and equity-oriented funds attract the highest investments.
- Tier-1 cities contribute the majority of investors.
- Leading fund houses dominate Assets Under Management.
- Portfolio holdings are diversified across multiple sectors.
- Benchmark indices demonstrate sustained market growth.
- Risk-adjusted metrics help identify high-performing schemes.

---

# 📁 Reports Generated

- Data Dictionary
- EDA Findings
- Fund Scorecard
- SQL Analytics
- Dashboard Visualizations

---

# 🚀 Future Enhancements

- Live data integration using APIs
- Predictive NAV forecasting
- Portfolio recommendation system
- Investor segmentation using Machine Learning
- Real-time dashboard updates
- Cloud deployment

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/your-username/MutualFundAnalytics.git
```

Move into the project

```bash
cd MutualFundAnalytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run data ingestion

```bash
python scripts/data_ingestion.py
```

Run cleaning

```bash
python scripts/data_cleaning.py
```

Create SQLite database

```bash
python scripts/database_setup.py
```

Load data

```bash
python scripts/load_to_sqlite.py
```

Run SQL analytics

```bash
python scripts/queries.py
```

Open Power BI dashboard

```
dashboard/MutualFundAnalytics.pbix
```

---

# 📸 Dashboard Preview

> Dashboard screenshots will be added after completing the Power BI dashboard.

---

# 👨‍💻 Author

Developed as part of the **Bluestock Fintech Mutual Fund Analytics Internship** using Python, SQL, SQLite, Power BI, and data analytics best practices.

---

# ⭐ Acknowledgements

Special thanks to **Bluestock Fintech** for providing the Mutual Fund Analytics Capstone Project and datasets for practical learning in data analytics.