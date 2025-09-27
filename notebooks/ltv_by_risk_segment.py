nb2 = nbf.v4.new_notebook()
nb2_cells = []

# Markdown
nb2_cells.append(nbf.v4.new_markdown_cell("""
# 📊 LTV by Risk Segment with SCD Type 2

This notebook analyzes the impact of **risk segment transitions** (SCD2) on **Customer Lifetime Value (LTV)**.
"""))

# Code: Install packages + auth
nb2_cells.append(nbf.v4.new_code_cell("""
!pip install --quiet google-cloud-bigquery pandas matplotlib seaborn
from google.colab import auth
auth.authenticate_user()

from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

client = bigquery.Client()
"""))

# Code: LTV by current risk segment
nb2_cells.append(nbf.v4.new_code_cell("""
query_ltv = '''
WITH joined AS (
    SELECT t.customer_id, d.risk_segment, t.amount, t.transaction_date
    FROM `scd2-ltv-analysis.tracking_risco_cliente.transactions_rawdata` t
    JOIN `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` d
      ON t.customer_id = d.customer_id
     AND t.transaction_date BETWEEN d.valid_from AND COALESCE(d.valid_to, CURRENT_DATE())
)
SELECT risk_segment,
       COUNT(DISTINCT customer_id) AS num_customers,
       SUM(amount)/COUNT(DISTINCT customer_id) AS avg_ltv
FROM joined
GROUP BY risk_segment
ORDER BY avg_ltv DESC
'''
ltv_df = client.query(query_ltv).to_dataframe()
ltv_df
"""))

# Code: Plot LTV by risk segment
nb2_cells.append(nbf.v4.new_code_cell("""
plt.figure(figsize=(8,5))
plt.bar(ltv_df['risk_segment'], ltv_df['avg_ltv'], color=['green','orange','red'])
plt.title('Average LTV by Risk Segment')
plt.xlabel('Risk Segment')
plt.ylabel('Average LTV ($)')
plt.show()
"""))

# Code: Analyze risk transitions
nb2_cells.append(nbf.v4.new_code_cell("""
query_transitions = '''
WITH transitions AS (
    SELECT customer_id,
           risk_segment,
           LAG(risk_segment) OVER(PARTITION BY customer_id ORDER BY valid_from) AS prev_segment,
           valid_from
    FROM `scd2-ltv-analysis.tracking_risco_cliente.dim_customers`
)
SELECT prev_segment, risk_segment AS new_segment, COUNT(DISTINCT customer_id) AS num_customers
FROM transitions
WHERE prev_segment IS NOT NULL AND prev_segment <> risk_segment
GROUP BY prev_segment, new_segment
ORDER BY num_customers DESC
'''
transitions_df = client.query(query_transitions).to_dataframe()
transitions_df
"""))

# Code: LTV impact of transitions
nb2_cells.append(nbf.v4.new_code_cell("""
query_ltv_transitions = '''
WITH joined AS (
    SELECT t.customer_id, d.risk_segment, t.amount, t.transaction_date
    FROM `scd2-ltv-analysis.tracking_risco_cliente.transactions_rawdata` t
    JOIN `scd2-ltv-analysis.tracking_risco_cliente.dim_customers` d
      ON t.customer_id = d.customer_id
     AND t.transaction_date BETWEEN d.valid_from AND COALESCE(d.valid_to, CURRENT_DATE())
),
ltv_per_customer AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM joined
    GROUP BY customer_id
),
risk_changes AS (
    SELECT customer_id, COUNT(DISTINCT risk_segment) AS num_segments
    FROM joined
    GROUP BY customer_id
)
SELECT CASE WHEN num_segments > 1 THEN 'Changed Risk' ELSE 'Stable Risk' END AS risk_status,
       AVG(total_spent) AS avg_ltv
FROM ltv_per_customer l
JOIN risk_changes r USING(customer_id)
GROUP BY risk_status
'''
ltv_transitions_df = client.query(query_ltv_transitions).to_dataframe()
ltv_transitions_df
"""))

# Code: Plot LTV impact of transitions
nb2_cells.append(nbf.v4.new_code_cell("""
plt.figure(figsize=(6,5))
plt.bar(ltv_transitions_df['risk_status'], ltv_transitions_df['avg_ltv'], color=['blue','gray'])
plt.title('LTV Comparison: Customers with vs. without Risk Transitions')
plt.ylabel('Average LTV ($)')
plt.show()
"""))

nb2['cells'] = nb2_cells

# Save notebook
with open("ltv_by_risk_segment.ipynb", "w") as f:
    nbf.write(nb2, f)

print("✅ Notebooks created successfully for Colab:")
print("- exploratory_analysis.ipynb")
print("- ltv_by_risk_segment.ipynb")