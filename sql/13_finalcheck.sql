SELECT customer_id, COUNT(*) AS active_versions
FROM `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
WHERE is_current = TRUE
GROUP BY customer_id
HAVING active_versions > 1;
