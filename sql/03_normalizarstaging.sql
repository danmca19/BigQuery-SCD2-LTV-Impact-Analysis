CREATE OR REPLACE TABLE `scd2-ltv-analysis.tracking_risco_cliente.staging_transactions` AS
SELECT
  CAST(transaction_id AS STRING) AS transaction_id,
  CAST(customer_id AS STRING) AS customer_id,
  DATE(transaction_date) AS transaction_date,
  SAFE_CAST(amount AS FLOAT64) AS amount,
  CURRENT_TIMESTAMP() AS load_ts
FROM `scd2-ltv-analysis.tracking_risco_cliente.transactions_rawdata`;
