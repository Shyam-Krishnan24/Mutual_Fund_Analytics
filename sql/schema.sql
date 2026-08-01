-- =========================================================
-- BLUESTOCK MUTUAL FUND ANALYTICS
-- SQLite Database Schema
-- =========================================================

DROP TABLE IF EXISTS fund_master;

CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

------------------------------------------------------------

DROP TABLE IF EXISTS nav_history;

CREATE TABLE nav_history (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

------------------------------------------------------------

DROP TABLE IF EXISTS investor_transactions;

CREATE TABLE investor_transactions (
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
);

------------------------------------------------------------

DROP TABLE IF EXISTS portfolio_holdings;

CREATE TABLE portfolio_holdings (
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date DATE
);