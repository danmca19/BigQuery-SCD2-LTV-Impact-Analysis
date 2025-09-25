CREATE TABLE IF NOT EXISTS `{project}.{dataset}.dim_customers` (
  customer_id INT64,
  name STRING,
  risk_segment STRING,
  effective_start_date DATE,
  effective_end_date DATE,
  is_current BOOL
);