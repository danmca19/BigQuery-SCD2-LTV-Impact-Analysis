MERGE `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` T
USING (
  SELECT
    customer_id,
    name,
    risk_segment,
    TO_HEX(SHA256(CONCAT(COALESCE(risk_segment,''), '||', COALESCE(name,''), '||', COALESCE(customer_id,'')))) AS record_hash,
    load_ts
  FROM `scd2-ltv-analysis.tracking_risco_cliente.staging_customers`
) S
ON T.customer_id = S.customer_id AND T.is_current = TRUE
WHEN MATCHED AND T.record_hash != S.record_hash THEN
  UPDATE SET effective_end_date = DATE_SUB(CURRENT_DATE(), INTERVAL 0 DAY), is_current = FALSE
WHEN NOT MATCHED BY TARGET THEN
  INSERT (customer_id, name, risk_segment, record_hash, effective_start_date, effective_end_date, is_current, source_load_ts)
  VALUES (S.customer_id, S.name, S.risk_segment, S.record_hash, CURRENT_DATE(), DATE '9999-12-31', TRUE, S.load_ts);
