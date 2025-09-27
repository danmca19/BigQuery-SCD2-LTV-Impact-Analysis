SELECT
  num_versions,
  COUNT(*) AS num_customers
FROM (
  SELECT customer_id, COUNT(*) AS num_versions
  FROM `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
  GROUP BY customer_id
)
GROUP BY num_versions
ORDER BY num_versions;
