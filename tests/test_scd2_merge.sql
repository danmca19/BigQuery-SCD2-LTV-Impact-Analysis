-- Basic test to check if SCD2 merge works
SELECT COUNT(*) FROM `{project}.{dataset}.dim_customers` WHERE is_current = TRUE;