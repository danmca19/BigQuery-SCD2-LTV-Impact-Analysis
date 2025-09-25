import pandas as pd

def test_customers_csv_exists():
    df = pd.read_csv('data/customers.csv')
    assert 'customer_id' in df.columns
    assert len(df) > 0
