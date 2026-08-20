# Customer Churn Prediction

An ML-based customer churn prediction project using Python, SQL, Scikit-learn, and FastAPI.

## Problem Statement

Customer churn means a customer stops using a company's service.

This project uses customer information such as age, tenure, monthly charges, and support calls to predict whether a customer is likely to churn.

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
- Uvicorn

## Project Workflow

1. Generate sample customer data
2. Prepare and process the data
3. Train a Logistic Regression model
4. Save the trained model using Joblib
5. Store customer data in SQLite
6. Create a FastAPI prediction API
7. Send customer details to the API
8. Get churn prediction and probability

## Features

The model uses the following customer information:

- Age
- Tenure in months
- Monthly charges
- Support calls

The model predicts whether a customer is likely to churn.

## Machine Learning Model

The project uses **Logistic Regression** for binary classification.

The prediction output is:

- `0` → Customer is unlikely to churn
- `1` → Customer is likely to churn

The API also returns the churn probability.

## API

The project provides a FastAPI endpoint for churn prediction.

### Endpoint

```text
POST /predict