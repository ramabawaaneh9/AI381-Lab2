
import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model.joblib")

metadata_path = Path("artifacts/metadata.json")
metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}


class PredictionInput(BaseModel):
    tenure_months: float
    monthly_fee: float
    support_calls: int
    contract: str
    internet_service: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": metadata.get("model_version", "local"),
        "mlflow_run_id": metadata.get("mlflow_run_id", "unknown"),
    }


@app.post("/predict")
def predict(data: PredictionInput):
    input_df = pd.DataFrame([{
        "tenure_months": data.tenure_months,
        "monthly_fee": data.monthly_fee,
        "support_calls": data.support_calls,
        "contract": data.contract,
        "internet_service": data.internet_service,
    }])

    probability = float(model.predict_proba(input_df)[0][1])

    return {
        "churn_probability": probability,
        "prediction": int(probability >= 0.5),
    }
