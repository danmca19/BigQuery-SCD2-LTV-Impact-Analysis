SELECT
  risk_segment,
  COUNT(DISTINCT customer_id) AS num_customers,
  ROUND(AVG(lifetime_value),2) AS avg_ltv,
  ROUND(SUM(lifetime_value),2) AS total_revenue
FROM `scd2-ltv-analysis.tracking_risco_cliente.customer_ltv`
GROUP BY risk_segment
ORDER BY avg_ltv DESC;
