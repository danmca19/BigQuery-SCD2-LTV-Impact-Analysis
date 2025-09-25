import os
from google.cloud import bigquery
from bigquery_utils import client, PROJECT_ID, DATASET_ID

def create_dataset_if_not_exists():
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    try:
        client.get_dataset(dataset_ref)
    except Exception:
        client.create_dataset(dataset_ref)
        print(f"Created dataset {DATASET_ID}")

if __name__ == "__main__":
    create_dataset_if_not_exists()
    print("Staging dataset ready.")
