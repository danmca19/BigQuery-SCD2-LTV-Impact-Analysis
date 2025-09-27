INSERT INTO `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
(customer_id, name, risk_segment, record_hash, effective_start_date, effective_end_date, is_current, source_load_ts)
SELECT
  customer_id,
  name,
  risk_segment,
  TO_HEX(SHA256(CONCAT(COALESCE(risk_segment,''), '||', COALESCE(name,''), '||', COALESCE(customer_id,'')))) AS record_hash,
  COALESCE(signup_date, CURRENT_DATE()) AS effective_start_date,
  DATE '9999-12-31' AS effective_end_date,
  TRUE AS is_current,
  load_ts
FROM `scd2-ltv-analysis.tracking_risco_cliente.staging_customers`;
