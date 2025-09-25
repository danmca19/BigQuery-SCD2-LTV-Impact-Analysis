from bigquery_utils import client, PROJECT_ID, DATASET_ID
import pandas as pd

def analyze_ltv():
    query = f'''
    SELECT c.risk_segment, AVG(t.amount) as avg_ltv
    FROM `{PROJECT_ID}.{DATASET_ID}.dim_customers` c
    JOIN `{PROJECT_ID}.{DATASET_ID}.transactions` t
    ON c.customer_id = t.customer_id
    WHERE c.is_current = TRUE
    GROUP BY c.risk_segment
    '''
    df = client.query(query).to_dataframe()
    print("LTV by risk segment:\n", df)
    return df

if __name__ == "__main__":
    analyze_ltv()
