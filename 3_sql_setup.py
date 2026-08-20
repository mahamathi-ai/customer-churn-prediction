

import pandas as pd
import sqlite3

# Load the customer dataset
df = pd.read_csv("customers.csv")

# Connect to the SQLite database
conn = sqlite3.connect("churn.db")

# Store the DataFrame as a customers table
df.to_sql("customers", conn, if_exists="replace", index=False)
print("Data loaded into SQLite database (churn.db)")


# Query the total number of customers
query1 = "SELECT COUNT(*) as total FROM customers"
result1 = pd.read_sql(query1, conn)
print("\n--- Total Customers ---")
print(result1)

# Query the number of churned customers
query2 = "SELECT COUNT(*) as churned FROM customers WHERE churn = 1"
result2 = pd.read_sql(query2, conn)
print("\n--- Churned Customers ---")
print(result2)

# Find the five customers with the most support calls
query3 = """
SELECT customer_id, age, support_calls, monthly_charges, churn
FROM customers
ORDER BY support_calls DESC
LIMIT 5
"""
result3 = pd.read_sql(query3, conn)
print("\n--- Top 5 customers with most support calls ---")
print(result3)

# Compare average monthly charges by churn status
query4 = """
SELECT churn, AVG(monthly_charges) as avg_charges, COUNT(*) as count
FROM customers
GROUP BY churn
"""
result4 = pd.read_sql(query4, conn)
print("\n--- Average charges: churned vs not churned ---")
print(result4)

# Close the database connection
conn.close()
print("\nDone! Database saved as churn.db")