-- contagem de linhas (verifica carga)
SELECT
  (SELECT COUNT(*) FROM `scd2-ltv-analysis.tracking_risco_cliente.customers_rawdata`) AS customers_count,
  (SELECT COUNT(*) FROM `scd2-ltv-analysis.tracking_risco_cliente.transactions_rawdata`) AS transactions_count;
