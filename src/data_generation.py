import pandas as pd, numpy as np
from faker import Faker
fake = Faker()

def generate_data(n=1000):
    customers = pd.DataFrame({
        "customer_id": range(1, n+1),
        "name": [fake.name() for _ in range(n)],
        "signup_date": pd.date_range(start="2020-01-01", periods=n, freq="D"),
        "risk_segment": np.random.choice(["Low", "Medium", "High"], size=n, p=[0.5, 0.3, 0.2])
    })
    transactions = pd.DataFrame({
        "transaction_id": range(1, n+1),
        "customer_id": np.random.choice(customers["customer_id"], size=n),
        "transaction_date": pd.date_range(start="2021-01-01", periods=n, freq="D"),
        "amount": np.random.exponential(scale=100, size=n).round(2)
    })
    customers.to_csv("data/customers.csv", index=False)
    transactions.to_csv("data/transactions.csv", index=False)
    print("Synthetic data generated.")

if __name__ == "__main__":
    generate_data()
