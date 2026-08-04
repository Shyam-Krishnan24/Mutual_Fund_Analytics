"""
database_setup.py

Purpose:
Creates the SQLite database and required tables
for Mutual Fund Analytics.

Author: R SHYAAM KRISHNAN
"""


from pathlib import Path
import sqlite3

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "mutual_fund.db"

print("=" * 60)
print("CREATING SQLITE DATABASE")
print("=" * 60)

print(f"\nDatabase Location : {DB_PATH}")

# ==========================================================
# Create Connection
# ==========================================================

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

# ==========================================================
# Fund Master Table
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS fund_master (

    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT

)
""")

print("✓ fund_master table created")

# ==========================================================
# NAV History Table
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS nav_history (

    amfi_code INTEGER,
    date DATE,
    nav REAL

)
""")

print("✓ nav_history table created")

# ==========================================================
# Investor Transactions Table
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS investor_transactions (

    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT

)
""")

print("✓ investor_transactions table created")

# ==========================================================
# Portfolio Holdings Table
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio_holdings (

    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date DATE

)
""")

print("✓ portfolio_holdings table created")

# ==========================================================
# Commit Changes
# ==========================================================

conn.commit()

conn.close()

print("\nDatabase Created Successfully!")

print(DB_PATH)

print("=" * 60)