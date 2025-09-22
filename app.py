from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# ---------------- Load Model + Vectorizer ----------------
tfidf = joblib.load("model/tfidf_vectorizer.pkl")
clf = joblib.load("model/logreg_model.pkl")

# Map class IDs back to labels
id2label = {0: "negative", 1: "neutral", 2: "positive"}

# ---------------- FastAPI Setup ----------------
app = FastAPI(
    title="Email Reply Classifier API",
    description="Classify email replies as positive, neutral, or negative",
    version="1.0"
)

class Request(BaseModel):
    text: str

class Response(BaseModel):
    label: str
    confidence: float

# ---------------- Root Endpoint ----------------
@app.get("/")
def root():
    return {"message": "Welcome to Email Reply Classifier API! Go to /docs to test the UI."}

# ---------------- Predict Endpoint ----------------
@app.post("/predict", response_model=Response)
def predict(request: Request):
    text = [request.text]  # vectorizer expects list
    features = tfidf.transform(text)
    probs = clf.predict_proba(features)[0]  # probability for each class
    pred_id = np.argmax(probs)
    label = id2label[pred_id]
    confidence = float(probs[pred_id])
    return {"label": label, "confidence": confidence}
