"""
STEP 1: Create sample customer data
------------------------------------
Namaku oru dataset venum - customers pathi info (age, bill amount, 
tenure) and avanga churn pannanga (left the company) illa continue 
pannanga nu.

Real projects la, indha data database or CSV file la irukum. 
Naanga ipo practice ku, random data generate pannurom (pandas + numpy vachu).
"""

import pandas as pd
import numpy as np

# Reproducibility ku - same random data every time varum
np.random.seed(42)

# 1000 customers create pannurom
n = 1000

data = {
    "customer_id": range(1, n + 1),
    "age": np.random.randint(18, 70, n),
    "tenure_months": np.random.randint(1, 72, n),          # evalo months customer aa irundhanga
    "monthly_charges": np.round(np.random.uniform(20, 120, n), 2),  # monthly bill
    "support_calls": np.random.randint(0, 10, n),          # support ku evalo thadava call pannanga
}

df = pd.DataFrame(data)

# Churn logic: konjam realistic aa iruka, simple rule vachu decide pannurom
churn_prob = (
    0.3
    - 0.003 * df["tenure_months"]
    + 0.05 * df["support_calls"]
    + 0.002 * df["monthly_charges"]
)
churn_prob = churn_prob.clip(0, 1)

df["churn"] = (np.random.rand(n) < churn_prob).astype(int)  # 1 = churned, 0 = stayed

# CSV file aa save pannurom
df.to_csv("customers.csv", index=False)

print("Data created! Sample rows:")
print(df.head())
print(f"\nTotal customers: {len(df)}")
print(f"Churned customers: {df['churn'].sum()}")