-- inspecionar esquema das tabelas
SELECT column_name, data_type
FROM `scd2-ltv-analysis.tracking_risco_cliente`.INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'customers_rawdata';

