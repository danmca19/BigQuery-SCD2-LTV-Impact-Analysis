-- create empty dim_customers with correct types
CREATE OR REPLACE TABLE `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` (
 customer_id STRING, name STRING, risk_segment STRING, record_hash STRING, valid_from DATE, valid_to DATE, is_current BOOL, source_load_ts TIMESTAMP
) PARTITION BY DATE(valid_from);