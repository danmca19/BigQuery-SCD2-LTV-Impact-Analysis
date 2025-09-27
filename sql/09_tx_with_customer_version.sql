CREATE OR REPLACE VIEW `scd2-ltv-analysis.tracking_risco_cliente.tx_with_customer_version` AS
SELECT
  t.transaction_id,
  t.customer_id,
  t.transaction_date,
  t.amount,
  c.risk_segment,
  c.effective_start_date,
  c.effective_end_date
FROM `scd2-ltv-analysis.tracking_risco_cliente.fact_transactions` t
LEFT JOIN `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` c
  ON t.customer_id = c.customer_id
  AND t.transaction_date BETWEEN c.effective_start_date AND c.effective_end_date;
