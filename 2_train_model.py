
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the customer dataset
df = pd.read_csv("customers.csv")
print("Data loaded! Shape:", df.shape)  # (rows, columns)

# Select input features and target variable
X = df[["age", "tenure_months", "monthly_charges", "support_calls"]]
y = df["churn"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)  

# Generate predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model using accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2%}")  # example: 78.50%

# Save the trained model for later use
joblib.dump(model, "churn_model.pkl")
print("Model saved as churn_model.pkl")