"""
queries.py

Purpose:
Executes analytical SQL queries for the project.

Author: R SHYAAM KRISHNAN
"""


from pathlib import Path
import sqlite3
import pandas as pd

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "mutual_fund.db"

# ==========================================================
# Connect Database
# ==========================================================

conn = sqlite3.connect(DB_PATH)

print("=" * 70)
print("MUTUAL FUND ANALYTICS")
print("=" * 70)


# ==========================================================
# Helper Function
# ==========================================================

def run_query(title, query):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    df = pd.read_sql_query(query, conn)

    print(df)

    return df


# ==========================================================
# Query 1
# Latest NAV of every scheme
# ==========================================================

run_query(
    "1. Latest NAV of Every Scheme",
    """
    SELECT
        amfi_code,
        MAX(date) AS latest_date,
        nav
    FROM nav_history
    GROUP BY amfi_code
    ORDER BY nav DESC;
    """
)


# ==========================================================
# Query 2
# Top 10 Highest NAV Funds
# ==========================================================

run_query(
    "2. Top 10 Highest NAV Funds",
    """
    SELECT
        fm.scheme_name,
        nh.nav
    FROM fund_master fm
    JOIN nav_history nh
    ON fm.amfi_code = nh.amfi_code

    WHERE nh.date = (
        SELECT MAX(date)
        FROM nav_history n2
        WHERE n2.amfi_code = nh.amfi_code
    )

    ORDER BY nh.nav DESC
    LIMIT 10;
    """
)


# ==========================================================
# Query 3
# Total Investment by State
# ==========================================================

run_query(
    "3. State Wise Investment",
    """
    SELECT
        state,
        ROUND(SUM(amount_inr),2) AS total_amount
    FROM investor_transactions
    GROUP BY state
    ORDER BY total_amount DESC;
    """
)


# ==========================================================
# Query 4
# Transaction Type Distribution
# ==========================================================

run_query(
    "4. Transaction Types",
    """
    SELECT
        transaction_type,
        COUNT(*) AS total_transactions
    FROM investor_transactions
    GROUP BY transaction_type;
    """
)


# ==========================================================
# Query 5
# Top Sectors by Portfolio Weight
# ==========================================================

run_query(
    "5. Sector Allocation",
    """
    SELECT
        sector,
        ROUND(SUM(weight_pct),2) AS total_weight
    FROM portfolio_holdings
    GROUP BY sector
    ORDER BY total_weight DESC;
    """
)


# ==========================================================
# Query 6
# Gender Distribution
# ==========================================================

run_query(
    "6. Investor Gender Distribution",
    """
    SELECT
        gender,
        COUNT(*) AS investors
    FROM investor_transactions
    GROUP BY gender;
    """
)


# ==========================================================
# Query 7
# City Tier Distribution
# ==========================================================

run_query(
    "7. City Tier Distribution",
    """
    SELECT
        city_tier,
        COUNT(*) AS investors
    FROM investor_transactions
    GROUP BY city_tier
    ORDER BY investors DESC;
    """
)


# ==========================================================
# Query 8
# Average Transaction Amount
# ==========================================================

run_query(
    "8. Average Transaction Amount",
    """
    SELECT
        ROUND(AVG(amount_inr),2) AS average_transaction
    FROM investor_transactions;
    """
)


# ==========================================================
# Query 9
# Top 10 Stocks by Market Value
# ==========================================================

run_query(
    "9. Top Stocks by Market Value",
    """
    SELECT
        stock_name,
        market_value_cr
    FROM portfolio_holdings
    ORDER BY market_value_cr DESC
    LIMIT 10;
    """
)


# ==========================================================
# Query 10
# Risk Category Distribution
# ==========================================================

run_query(
    "10. Risk Category Distribution",
    """
    SELECT
        risk_category,
        COUNT(*) AS funds
    FROM fund_master
    GROUP BY risk_category;
    """
)

conn.close()

print("\n")
print("=" * 70)
print("ALL QUERIES EXECUTED SUCCESSFULLY")
print("=" * 70)
