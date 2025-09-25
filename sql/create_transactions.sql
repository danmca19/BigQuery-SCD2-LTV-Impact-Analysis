CREATE TABLE IF NOT EXISTS `{project}.{dataset}.transactions` (
  transaction_id INT64,
  customer_id INT64,
  transaction_date DATE,
  amount NUMERIC
);