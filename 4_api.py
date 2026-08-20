

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained machine learning model
model = joblib.load("churn_model.pkl")

# Create the FastAPI application
app = FastAPI(title="Customer Churn Prediction API")

# Define the customer input data structure
class Customer(BaseModel):
    age: int
    tenure_months: int
    monthly_charges: float
    support_calls: int

# Create the root endpoint to check whether the API is running
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running!"}


# Create the prediction endpoint
@app.post("/predict")
def predict_churn(customer: Customer):
   # Prepare customer data in the format expected by the model
    input_data = pd.DataFrame([{
        "age": customer.age,
        "tenure_months": customer.tenure_months,
        "monthly_charges": customer.monthly_charges,
        "support_calls": customer.support_calls,
    }])

    # Generate the churn prediction   
    prediction = model.predict(input_data)[0]  # 0 or 1
    # Calculate the probability of customer churn
    probability = model.predict_proba(input_data)[0][1]  

    # Return the prediction result
    return {
        "churn_prediction": int(prediction), 
        "churn_probability": round(float(probability), 2),
        "message": "Customer likely to churn" if prediction == 1 else "Customer likely to stay"
    }