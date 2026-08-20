"""
STEP 4: FastAPI - Model-a oru API aa maathurom
--------------------------------------------------
Namma trained model (churn_model.pkl) ippo oru "file" aa mattum
irukku - adhukku direct access illama, vera oru program/website 
use panna mudiyathu.

FastAPI vachu, namma model-a oru "web service" aa maathurom.
Adhaal, customer details kudutha, model real-time-la 
"churn aaguvangala illaya" nu predict pannu tharum.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Step 1: Trained model-a load pannurom (Step 2-la save panniruntha file)
model = joblib.load("churn_model.pkl")

# Step 2: FastAPI app create pannurom
app = FastAPI(title="Customer Churn Prediction API")

# Step 3: Input format define pannurom
# Idhu oru "template" - API-ku evlo type oda data varanum nu solrom
class Customer(BaseModel):
    age: int
    tenure_months: int
    monthly_charges: float
    support_calls: int

# Step 4: Root endpoint - API work aaguthaanu check panna (simple test)
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running!"}

# Step 5: Prediction endpoint - idhu than main logic
@app.post("/predict")
def predict_churn(customer: Customer):
    # Customer data-va model-ku puriyara format-ku maathurom
    input_data = pd.DataFrame([{
        "age": customer.age,
        "tenure_months": customer.tenure_months,
        "monthly_charges": customer.monthly_charges,
        "support_calls": customer.support_calls,
    }])

    # Model prediction pannuthu
    prediction = model.predict(input_data)[0]  # 0 or 1
    probability = model.predict_proba(input_data)[0][1]  # churn chance %

    return {
        "churn_prediction": int(prediction),  # 1 = will churn, 0 = will stay
        "churn_probability": round(float(probability), 2),
        "message": "Customer likely to churn" if prediction == 1 else "Customer likely to stay"
    }