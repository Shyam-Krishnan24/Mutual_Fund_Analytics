from pathlib import Path
import sqlite3
import pandas as pd

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DATABASE_DIR = BASE_DIR / "database"

DB_PATH = DATABASE_DIR / "mutual_fund.db"

print("=" * 60)
print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 60)

# ==========================================================
# CONNECT DATABASE
# ==========================================================

conn = sqlite3.connect(DB_PATH)

print("\nConnected Successfully!")

# ==========================================================
# LOAD FUND MASTER
# ==========================================================

print("\nLoading Fund Master...")

fund_master = pd.read_csv(RAW_DIR / "01_fund_master.csv")

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

print(f"✓ {len(fund_master)} records inserted")

# ==========================================================
# LOAD NAV HISTORY
# ==========================================================

print("\nLoading NAV History...")

nav = pd.read_csv(PROCESSED_DIR / "clean_nav.csv")

nav.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

print(f"✓ {len(nav)} records inserted")

# ==========================================================
# LOAD INVESTOR TRANSACTIONS
# ==========================================================

print("\nLoading Investor Transactions...")

transactions = pd.read_csv(
    PROCESSED_DIR / "clean_investor_transactions.csv"
)

transactions.to_sql(
    "investor_transactions",
    conn,
    if_exists="replace",
    index=False
)

print(f"✓ {len(transactions)} records inserted")

# ==========================================================
# LOAD PORTFOLIO HOLDINGS
# ==========================================================

print("\nLoading Portfolio Holdings...")

portfolio = pd.read_csv(
    PROCESSED_DIR / "clean_portfolio_holdings.csv"
)

portfolio.to_sql(
    "portfolio_holdings",
    conn,
    if_exists="replace",
    index=False
)

print(f"✓ {len(portfolio)} records inserted")

# ==========================================================
# VERIFY TABLES
# ==========================================================

print("\n" + "=" * 60)
print("VERIFYING DATABASE")
print("=" * 60)

tables = pd.read_sql_query(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """,
    conn
)

print(tables)

# ==========================================================
# VERIFY RECORD COUNTS
# ==========================================================

print("\nTable Record Counts\n")

table_names = [
    "fund_master",
    "nav_history",
    "investor_transactions",
    "portfolio_holdings"
]

for table in table_names:

    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )

    print(f"{table:25} : {count.iloc[0,0]}")

# ==========================================================
# CLOSE CONNECTION
# ==========================================================

conn.close()

print("\nDatabase Connection Closed")

print("=" * 60)
print("ALL DATA LOADED SUCCESSFULLY")
print("=" * 60)