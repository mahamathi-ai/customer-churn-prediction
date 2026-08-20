"""
STEP 2: Train an ML model
---------------------------
Namma customers.csv file-la irunthu data load pannurom, 
oru Logistic Regression model train pannurom - idhu customer 
churn pannuvangala nu predict panna kathukkum.

Train pannina apparam, model-a oru file aa save pannurom,
adhu FastAPI step-la use pannurom.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Data-va load pannurom
df = pd.read_csv("customers.csv")
print("Data loaded! Shape:", df.shape)  # (rows, columns)

# Step 2: Features (X) and Target (y) pirikkurom
# Features = model-ku input aa kudukkura columns
# Target = model predict panna vendiya column (churn)
X = df[["age", "tenure_months", "monthly_charges", "support_calls"]]
y = df["churn"]

# Step 3: Data-va training and testing ku pirikkurom
# 80% data - model-a train panna (kathukka)
# 20% data - model evalo nalla kathukiruchu nu test panna
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# Step 4: Model create pannurom, train pannurom
model = LogisticRegression()
model.fit(X_train, y_train)  # idhu than "training" - model pattern kathukum

# Step 5: Model evalo nalla predict pannuthu nu check pannurom
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2%}")  # example: 78.50%

# Step 6: Model-a oru file aa save pannurom (FastAPI step-la use panna)
joblib.dump(model, "churn_model.pkl")
print("Model saved as churn_model.pkl")