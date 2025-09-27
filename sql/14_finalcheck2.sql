SELECT customer_id, effective_start_date, effective_end_date, prev_end
FROM (
  SELECT
    customer_id,
    effective_start_date,
    effective_end_date,
    LAG(effective_end_date) OVER (PARTITION BY customer_id ORDER BY effective_start_date) AS prev_end
  FROM `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
)
WHERE prev_end IS NOT NULL AND prev_end > effective_start_date;
