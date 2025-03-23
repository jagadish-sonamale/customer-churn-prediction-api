from fastapi import FastAPI
import uvicorn

from app.routes.churn_prediction_router import router as predict_router

app = FastAPI(ttitle="Churn Prediction API")

app.include_router(predict_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)