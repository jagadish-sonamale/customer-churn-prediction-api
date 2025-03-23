from fastapi import APIRouter
from app.services.prediction_service import churn_predict
from app.schemas.request_model import PredictionRequest

router = APIRouter()

@router.post("/predict")
def predict(data: PredictionRequest):
    prediction = churn_predict(data)
    if prediction >= 0.5:
        return {"prediction": "1"}
    return {"prediction": "0"} 