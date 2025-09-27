WITH seq AS (
  SELECT
    customer_id,
    ARRAY_AGG(risk_segment ORDER BY effective_start_date) AS segments
  FROM `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
  GROUP BY customer_id
),
flag AS (
  SELECT
    customer_id,
    (SELECT COUNT(1)
     FROM UNNEST(GENERATE_ARRAY(0, ARRAY_LENGTH(segments)-2)) AS i
     WHERE segments[OFFSET(i)] = 'Medium' AND segments[OFFSET(i+1)] = 'High') > 0 AS medium_to_high
  FROM seq
)
SELECT
  SUM(CASE WHEN medium_to_high THEN 1 ELSE 0 END) AS num_medium_to_high,
  COUNT(*) AS total_customers,
  ROUND(100 * SAFE_DIVIDE(SUM(CASE WHEN medium_to_high THEN 1 ELSE 0 END), COUNT(*)), 2) AS pct_medium_to_high
FROM flag;
