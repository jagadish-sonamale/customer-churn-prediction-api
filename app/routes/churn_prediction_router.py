# app/routes/churn_prediction_router.py

from fastapi import APIRouter
from app.schemas.request_model import ChurnRequest
from app.models.predictor import preprocess_input, run_inference

router = APIRouter()

@router.post("/predict")
def predict_churn(data: ChurnRequest):
    input_scaled = preprocess_input(data)
    prediction = run_inference(input_scaled)
    return {"churn_probability": prediction}
