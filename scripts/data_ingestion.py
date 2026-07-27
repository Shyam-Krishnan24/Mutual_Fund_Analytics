import pandas as pd
import os
from pathlib import Path

# Checking the file info and accessing the files

folder="data/raw"
files=os.listdir(folder)
for f in files:
    if f.endswith(".csv"):
        df=pd.read_csv(os.path.join(folder, f))

        print("="*50)
        print(f)
        print(df.shape)
        print(df.dtypes)
        print(df.head())
        print(df.isnull().sum())
        print(df.duplicated().sum()) 

# Replacing the null values with mean values (handling missing values)
df1=pd.read_csv(r"D:\Workplace\Bluestocks Internship\MutualFundAnalytics\data\raw\04_monthly_sip_inflows.csv")
print(df1.shape)
df1["yoy_growth_pct"]=df1["yoy_growth_pct"].fillna(df1["yoy_growth_pct"].mean())
print(df1.dtypes)
print(df1.head(10))
print(df1.isnull().sum())

# Dates should be converted from str to int 
from pathlib import Path

# Create processed folder if it doesn't exist
processed_folder = Path("data/processed")
processed_folder.mkdir(exist_ok=True)

# Dictionary of files and their date columns
date_columns = {
    "01_fund_master.csv": ["launch_date"],
    "02_nav_history.csv": ["date"],
    "03_aum_by_fund_house.csv": ["date"],
    "04_monthly_sip_inflows.csv": ["month"],
    "05_category_inflows.csv": ["month"],
    "06_industry_folio_count.csv": ["month"],
    "08_investor_transactions.csv": ["transaction_date"],
    "09_portfolio_holdings.csv": ["portfolio_date"],
    "10_benchmark_indices.csv": ["date"]
}

# Read each file, clean it, convert dates, and save
for file in files:
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(folder, file))

        # Handle missing values
        if file == "04_monthly_sip_inflows.csv":
            df["yoy_growth_pct"] = df["yoy_growth_pct"].fillna(df["yoy_growth_pct"].mean())

        # Convert date columns
        if file in date_columns:
            for col in date_columns[file]:
                df[col] = pd.to_datetime(df[col])

        # Save cleaned file
        df.to_csv(processed_folder / file, index=False)
        print(f"{file} processed and saved successfully.")
