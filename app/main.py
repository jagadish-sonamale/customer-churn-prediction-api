# app/main.py

from fastapi import FastAPI
from app.routes import churn_prediction_router

app = FastAPI(title="Customer Churn Prediction API")

app.include_router(churn_prediction_router.router, prefix="/api/v1", tags=["Prediction"])
