# Customer Churn Prediction

An ML-based customer churn prediction project using Python, SQL, Scikit-learn, and FastAPI.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SQLite
- SQL
- FastAPI
- Pydantic
- Joblib

## Project Workflow

1. Generate sample customer data
2. Train a Logistic Regression model
3. Store customer data in SQLite
4. Create a FastAPI prediction API

## Features

The model uses:

- Age
- Tenure in months
- Monthly charges
- Support calls

to predict whether a customer is likely to churn.

## How to Run

Install the required packages:

```bash
pip install pandas numpy scikit-learn fastapi uvicorn joblib