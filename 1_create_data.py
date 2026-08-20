
import pandas as pd
import numpy as np

# Set a random seed to generate reproducible data
np.random.seed(42)

# Define the number of customers
n = 1000

# Generate customer information
data = {
    "customer_id": range(1, n + 1),
    "age": np.random.randint(18, 70, n),
    "tenure_months": np.random.randint(1, 72, n),          
    "monthly_charges": np.round(np.random.uniform(20, 120, n), 2),  l
    "support_calls": np.random.randint(0, 10, n),          
}

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Calculate the probability of customer churn
churn_prob = (
    0.3
    - 0.003 * df["tenure_months"]
    + 0.05 * df["support_calls"]
    + 0.002 * df["monthly_charges"]
)
churn_prob = churn_prob.clip(0, 1)

# Generate the churn target variable
df["churn"] = (np.random.rand(n) < churn_prob).astype(int)  

# Save the generated dataset as a CSV file
df.to_csv("customers.csv", index=False)

print("Data created! Sample rows:")
print(df.head())
print(f"\nTotal customers: {len(df)}")
print(f"Churned customers: {df['churn'].sum()}")