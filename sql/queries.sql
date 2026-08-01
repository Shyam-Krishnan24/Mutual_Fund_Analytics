-- =========================================================
-- Mutual Fund Analytics Queries
-- =========================================================

-- 1. Total Mutual Fund Schemes
SELECT COUNT(*) AS total_schemes
FROM fund_master;

------------------------------------------------------------

-- 2. Total NAV Records
SELECT COUNT(*) AS total_nav_records
FROM nav_history;

------------------------------------------------------------

-- 3. Latest NAV of Every Scheme

SELECT
    amfi_code,
    MAX(date) AS latest_date,
    nav
FROM nav_history
GROUP BY amfi_code;

------------------------------------------------------------

-- 4. Top 10 Highest NAV Funds

SELECT
    fm.scheme_name,
    nh.nav
FROM fund_master fm
JOIN nav_history nh
ON fm.amfi_code = nh.amfi_code
ORDER BY nh.nav DESC
LIMIT 10;

------------------------------------------------------------

-- 5. State-wise Investment

SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

------------------------------------------------------------

-- 6. Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

------------------------------------------------------------

-- 7. Sector Allocation

SELECT
    sector,
    SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;

------------------------------------------------------------

-- 8. Gender Distribution

SELECT
    gender,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY gender;

------------------------------------------------------------

-- 9. Average Transaction Amount

SELECT
    AVG(amount_inr) AS average_transaction
FROM investor_transactions;

------------------------------------------------------------

-- 10. Top Holdings

SELECT
    stock_name,
    market_value_cr
FROM portfolio_holdings
ORDER BY market_value_cr DESC
LIMIT 10;
