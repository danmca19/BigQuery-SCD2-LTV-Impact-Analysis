CREATE OR REPLACE TABLE `scd2-ltv-analysis.tracking_risco_cliente.staging_customers` AS
SELECT
  CAST(customer_id AS STRING) AS customer_id,
  name,
  DATE(signup_date) AS signup_date,
  SAFE_CAST(risk_segment AS STRING) AS risk_segment,
  CURRENT_TIMESTAMP() AS load_ts
FROM `scd2-ltv-analysis.tracking_risco_cliente.customers_rawdata`;
