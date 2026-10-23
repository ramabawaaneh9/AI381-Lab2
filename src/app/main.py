from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.joblib")


class PredictionInput(BaseModel):
    tenure_months: float
    monthly_fee: float
    support_calls: int
    contract: str
    internet_service: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: PredictionInput):
    input_df = pd.DataFrame([{
        "tenure_months": data.tenure_months,
        "monthly_fee": data.monthly_fee,
        "support_calls": data.support_calls,
        "contract": data.contract,
        "internet_service": data.internet_service,
    }])

    prediction = model.predict(input_df)[0]

    return {
        "prediction": int(prediction)
    }