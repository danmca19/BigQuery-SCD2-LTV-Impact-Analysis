import nbformat as nbf

# -------------------------------
# 1️⃣ Exploratory Analysis Notebook
# -------------------------------
nb1 = nbf.v4.new_notebook()
nb1_cells = []

# Markdown
nb1_cells.append(nbf.v4.new_markdown_cell("""
# 📊 Exploratory Analysis of Customers and Transactions

This notebook explores the `customers_rawdata` and `transactions_rawdata` datasets to understand distributions, patterns, and potential insights.
"""))

# Code: Install packages + auth
nb1_cells.append(nbf.v4.new_code_cell("""
!pip install --quiet google-cloud-bigquery pandas matplotlib seaborn
from google.colab import auth
auth.authenticate_user()

from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client = bigquery.Client()
"""))

# Code: Load customers
nb1_cells.append(nbf.v4.new_code_cell("""
query_customers = '''
SELECT * 
FROM `scd2-ltv-analysis.tracking_risco_cliente.customers_rawdata`
LIMIT 1000
'''
customers_df = client.query(query_customers).to_dataframe()
customers_df.head()
"""))

# Code: Load transactions
nb1_cells.append(nbf.v4.new_code_cell("""
query_transactions = '''
SELECT * 
FROM `scd2-ltv-analysis.tracking_risco_cliente.transactions_rawdata`
LIMIT 1000
'''
transactions_df = client.query(query_transactions).to_dataframe()
transactions_df.head()
"""))

# Code: Plot risk segment distribution
nb1_cells.append(nbf.v4.new_code_cell("""
plt.figure(figsize=(6,4))
sns.countplot(x='risk_segment', data=customers_df, order=['Low','Medium','High'])
plt.title('Customer Risk Segment Distribution')
plt.show()
"""))

# Code: Plot transaction amount distribution
nb1_cells.append(nbf.v4.new_code_cell("""
plt.figure(figsize=(6,4))
sns.histplot(transactions_df['amount'], bins=50, kde=True)
plt.title('Transaction Amount Distribution')
plt.show()
"""))

nb1['cells'] = nb1_cells

# Save notebook
with open("exploratory_analysis.ipynb", "w") as f:
    nbf.write(nb1, f)
