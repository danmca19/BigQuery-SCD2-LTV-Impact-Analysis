CREATE OR REPLACE TABLE `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` (
  customer_id STRING,
  name STRING,
  risk_segment STRING,
  record_hash STRING,
  effective_start_date DATE,
  effective_end_date DATE,
  is_current BOOL,
  source_load_ts TIMESTAMP
)
PARTITION BY DATE(effective_start_date);
