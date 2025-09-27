CREATE OR REPLACE TABLE `scd2-ltv-analysis.tracking_risco_cliente.customer_ltv` AS
SELECT
  c.customer_id,
  c.risk_segment,
  SUM(t.amount) AS lifetime_value
FROM `scd2-ltv-analysis.tracking_risco_cliente.fact_transactions` t
JOIN `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` c
  ON t.customer_id = c.customer_id
  AND t.transaction_date BETWEEN c.effective_start_date AND c.effective_end_date
GROUP BY c.customer_id, c.risk_segment;
