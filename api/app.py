from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="E2E MLOps Platform API")
Instrumentator().instrument(app).expose(app)
model = joblib.load("models/model.pkl")
CLASSES = ["Class_0", "Class_1", "Class_2"]

class WineFeatures(BaseModel):
    features: list

@app.get("/")
def root():
    return {"message": "MLOps API is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: WineFeatures):
    arr = np.array(data.features).reshape(1, -1)
    pred = model.predict(arr)[0]
    proba = model.predict_proba(arr)[0].tolist()
    return {
        "prediction": int(pred),
        "label": CLASSES[pred],
        "confidence": round(max(proba), 4)
    }