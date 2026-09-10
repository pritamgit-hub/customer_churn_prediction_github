-- Customer Churn Analysis
-- SQLite/PostgreSQL compatible with minor syntax adjustments.

-- 1. Overall churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn;

-- 2. Churn by contract
SELECT
    contract,
    COUNT(*) AS customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(100.0 * SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY contract
ORDER BY churn_rate_pct DESC;

-- 3. Average monthly charges by churn status
SELECT
    churn,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY churn;

-- 4. Churn by payment method
SELECT
    payment_method,
    COUNT(*) AS customers,
    ROUND(100.0 * SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM customer_churn
GROUP BY payment_method
ORDER BY churn_rate_pct DESC;

-- 5. High-risk customers: short tenure and month-to-month contract
SELECT customer_id, tenure_months, monthly_charges, contract, payment_method, churn
FROM customer_churn
WHERE contract = 'Month-to-month'
  AND tenure_months <= 12
ORDER BY monthly_charges DESC;
