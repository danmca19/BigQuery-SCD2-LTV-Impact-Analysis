MERGE `{project}.{dataset}.dim_customers` T
USING `{project}.{dataset}.staging_customers` S
ON T.customer_id = S.customer_id AND T.is_current = TRUE
WHEN MATCHED AND T.risk_segment != S.risk_segment THEN
  UPDATE SET T.effective_end_date = CURRENT_DATE(), T.is_current = FALSE
WHEN NOT MATCHED THEN
  INSERT (customer_id, name, risk_segment, effective_start_date, effective_end_date, is_current)
  VALUES (S.customer_id, S.name, S.risk_segment, CURRENT_DATE(), DATE '9999-12-31', TRUE);