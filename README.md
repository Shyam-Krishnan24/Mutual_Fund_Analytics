# 📊 Mutual Fund Analytics

> **Bluestock Fintech Capstone Project**
>
> A complete end-to-end Data Analytics project that analyzes Indian Mutual Fund datasets using **Python, SQL, SQLite, Jupyter Notebook, and Power BI** to generate actionable business insights through data cleaning, exploratory analysis, financial performance evaluation, and interactive dashboards.

---

# 👨‍💻 Author

**R SHYAAM KRISHNAN**

---

# 📌 Project Overview

The Indian Mutual Fund industry produces vast amounts of financial and transactional data. This project transforms raw datasets into meaningful insights by implementing a complete analytics pipeline—from data ingestion and cleaning to database integration, SQL analysis, exploratory data analysis (EDA), performance evaluation, and Power BI dashboard development.

The final solution provides an interactive dashboard that enables users to analyze mutual fund performance, investor behavior, market trends, and portfolio composition.

---

# 🎯 Project Objectives

- Load and preprocess multiple mutual fund datasets.
- Perform data cleaning and validation.
- Analyze NAV trends, AUM growth, SIP inflows, and investor behavior.
- Store processed datasets in SQLite.
- Execute SQL-based analytical queries.
- Evaluate fund performance using financial metrics.
- Build an interactive Power BI dashboard.
- Generate business insights for investment analysis.

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
- SQLAlchemy
- Requests

### Database

- SQLite

### Visualization

- Power BI

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── data_cleaning.py
│   ├── database_setup.py
│   ├── load_to_sqlite.py
│   ├── queries.py
|   ├── recommender.py
│   └── README.md
│
├── notebooks/
│   ├── Day1_EDA.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── README.md
│
├── database/
│   ├── mutual_fund.db
│   └── README.md
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│   └── README.md
│
├── dashboard/
│   ├── MutualFundAnalytics.pbix
│   ├── Dashboard_Screenshots/
│   └── README.md
│
├── reports/
│   ├── EDA_Findings.md
│   ├── Fund_Report.pdf
│   ├── fund_scorecard.csv
│   └── README.md
│
├── run_pipeline.py
├── data_dictionary.md
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📁 Datasets Used

The project analyzes ten datasets related to the Indian Mutual Fund industry.

| Dataset | Description |
|----------|-------------|
| Fund Master | Mutual fund scheme information |
| NAV History | Historical Net Asset Values |
| AUM by Fund House | Assets Under Management |
| Monthly SIP Inflows | SIP investment trends |
| Category Inflows | Category-wise inflows |
| Industry Folio Count | Investor participation |
| Scheme Performance | Returns and financial metrics |
| Investor Transactions | Investment transactions |
| Portfolio Holdings | Portfolio composition |
| Benchmark Indices | Market benchmark performance |

Additionally, live NAV data was collected using the **MFAPI**.

---

# 🔄 Project Workflow

```text
Raw Datasets
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning & Validation
      │
      ▼
Processed Datasets
      │
      ▼
SQLite Database
      │
      ▼
SQL Analysis
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Performance Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Business Insights
```

---

# ✅ Project Implementation

## Day 1 – Data Ingestion

- Created project folder structure
- Loaded all datasets using Pandas
- Performed initial dataset inspection
- Retrieved live NAV data from MFAPI
- Validated AMFI scheme codes
- Generated requirements.txt

---

## Day 2 – Data Cleaning

Completed preprocessing for all datasets:

- Removed duplicate records
- Converted date columns
- Standardized categorical values
- Handled missing values
- Validated financial data
- Generated cleaned datasets
- Created SQLite database
- Loaded processed datasets into SQLite

---

## Day 3 – Exploratory Data Analysis

Performed comprehensive EDA including:

- NAV Trend Analysis
- AUM Growth Analysis
- Monthly SIP Analysis
- Category-wise Inflow Analysis
- Investor Demographics
- Industry Folio Growth
- Benchmark Performance
- Portfolio Holdings Analysis
- Correlation Analysis

Generated:

- EDA notebook
- Business observations
- Analytical visualizations

---

## Day 4 – Performance Analytics

Evaluated mutual fund performance using:

- 1-Year Return
- 3-Year Return
- 5-Year Return
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Expense Ratio
- Morningstar Rating
- Fund Scorecard

---

## Day 5 – Dashboard Development

Developed an interactive Power BI dashboard consisting of four analytical pages.

### Executive Overview

- Total Mutual Funds
- Total Fund Houses
- Total AUM
- Total Investors
- NAV Trend
- Category Distribution

### Fund Performance

- Top Performing Funds
- Sharpe Ratio Ranking
- Alpha vs Beta
- Fund Scorecard
- Expense Ratio Analysis

### Investor Analytics

- State-wise Investments
- Gender Distribution
- Age Group Analysis
- City Tier Analysis
- Transaction Type Analysis

### Market Analytics

- SIP Trend
- Category Inflows
- Industry Folio Growth
- Portfolio Allocation
- Benchmark Performance

---

# 💾 Database

SQLite was used to store cleaned datasets and execute SQL analytics.

The database includes:

- Fund Master
- NAV History
- AUM
- SIP Inflows
- Category Inflows
- Industry Folios
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

# 📈 SQL Analytics

Implemented analytical SQL queries for:

- Latest NAV
- Highest NAV Funds
- State-wise Investments
- Transaction Distribution
- Sector Allocation
- Gender Analysis
- City Tier Analysis
- Average Investment
- Portfolio Holdings
- Risk Category Analysis

---

# 📊 Dashboard Features

The Power BI dashboard enables users to:

- Analyze mutual fund performance
- Compare fund houses
- Track NAV trends
- Evaluate investor demographics
- Monitor SIP growth
- Explore benchmark movements
- Study portfolio allocation
- Rank funds using performance metrics

---

# 📌 Key Insights

- Mutual fund investments demonstrated consistent long-term growth.
- SIP inflows increased steadily over the analysis period.
- Equity-oriented funds attracted the highest investor participation.
- Large fund houses managed the highest Assets Under Management (AUM).
- Tier-1 cities contributed the majority of investments.
- Risk-adjusted metrics effectively differentiated high-performing schemes.
- Portfolio holdings showed diversified sector allocation.
- Benchmark indices reflected sustained market growth.

---

# 📄 Reports Generated

- Data Dictionary
- Exploratory Data Analysis Report
- Fund Performance Report
- Fund Scorecard
- SQL Analytics
- Dashboard Visualizations

---

# 🚀 Future Enhancements

- Live API integration for real-time NAV updates
- Machine Learning-based return prediction
- Portfolio recommendation system
- Investor segmentation
- Automated dashboard refresh
- Cloud deployment

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/MutualFundAnalytics.git
```

### Navigate to Project

```bash
cd MutualFundAnalytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Complete Pipeline

```bash
python run_pipeline.py
```

The pipeline executes:

1. Data Ingestion
2. Live NAV Fetch
3. Data Cleaning
4. Database Creation
5. SQLite Loading
6. SQL Analytics

---

# 📸 Dashboard Preview

Dashboard screenshots are available in:

```text
dashboard/
└── Dashboard_Screenshots/
```

---

# 📜 License

This project was developed for educational purposes as part of the **Bluestock Fintech Mutual Fund Analytics Capstone Project**.

---

# 🙏 Acknowledgements

Special thanks to **Bluestock Fintech** for providing the Mutual Fund Analytics Capstone Project and datasets, enabling hands-on learning in data analytics, financial analysis, SQL, and Power BI.
