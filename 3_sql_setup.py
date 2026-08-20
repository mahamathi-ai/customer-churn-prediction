"""
STEP 3: SQL - Data-va database-la store panni, query pannurom
----------------------------------------------------------------
Namma customers.csv data-va oru SQLite database-la store pannurom.
SQLite = oru simple, file-based database - namma computer-lave 
irukum, separate server install panna vendam.

Apparam SQL queries vachu, data-va "ketkurom" (query pannurom).
Support role interview-la SQL romba kekkuvanga, so idhu practice ku useful.
"""

import pandas as pd
import sqlite3

# Step 1: CSV data-va load pannurom
df = pd.read_csv("customers.csv")

# Step 2: Database-oda "connection" create pannurom
# "churn.db" nu oru file create aagum - idhu than namma database
conn = sqlite3.connect("churn.db")

# Step 3: DataFrame-a database table aa maathurom
# table name: "customers"
# if_exists="replace" - already table irundha, replace pannidum
df.to_sql("customers", conn, if_exists="replace", index=False)
print("Data loaded into SQLite database (churn.db)")

# Step 4: Ippo SQL queries run pannalam!

# Query 1: Total customers evalo irukanga
query1 = "SELECT COUNT(*) as total FROM customers"
result1 = pd.read_sql(query1, conn)
print("\n--- Total Customers ---")
print(result1)

# Query 2: Evalo peru churn pannanga
query2 = "SELECT COUNT(*) as churned FROM customers WHERE churn = 1"
result2 = pd.read_sql(query2, conn)
print("\n--- Churned Customers ---")
print(result2)

# Query 3: High-risk customers - evalo support calls pannanga, evalo bill
query3 = """
SELECT customer_id, age, support_calls, monthly_charges, churn
FROM customers
ORDER BY support_calls DESC
LIMIT 5
"""
result3 = pd.read_sql(query3, conn)
print("\n--- Top 5 customers with most support calls ---")
print(result3)

# Query 4: Average monthly charges - churned vs not churned customers
query4 = """
SELECT churn, AVG(monthly_charges) as avg_charges, COUNT(*) as count
FROM customers
GROUP BY churn
"""
result4 = pd.read_sql(query4, conn)
print("\n--- Average charges: churned vs not churned ---")
print(result4)

# Connection close pannurom (nalla practice, memory leak avoid panna)
conn.close()
print("\nDone! Database saved as churn.db")