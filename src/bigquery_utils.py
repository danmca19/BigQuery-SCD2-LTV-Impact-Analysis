from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")

client = bigquery.Client(project=PROJECT_ID)

def load_csv_to_bq(table_name, csv_path, schema):
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"
    job_config = bigquery.LoadJobConfig(schema=schema, skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)
    with open(csv_path, "rb") as f:
        job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()
    print(f"Loaded {csv_path} into {table_id}.")
