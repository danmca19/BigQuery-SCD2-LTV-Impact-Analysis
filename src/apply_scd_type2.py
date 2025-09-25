import os
from google.cloud import bigquery
from bigquery_utils import client, PROJECT_ID, DATASET_ID

def apply_merge():
    sql_path = "sql/merge_scd2.sql"
    with open(sql_path, "r") as f:
        query = f.read().format(project=PROJECT_ID, dataset=DATASET_ID)
    client.query(query).result()
    print("SCD Type 2 merge applied.")

if __name__ == "__main__":
    apply_merge()
