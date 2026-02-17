from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

# Load model and columns
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "manufacturing_model.pkl")
columns_path = os.path.join(BASE_DIR, "model", "columns.pkl")

model = joblib.load(model_path)
columns = joblib.load(columns_path)


@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: dict):
    # Convert input to dataframe
    df = pd.DataFrame([data])
    
    # Convert text to dummies
    df = pd.get_dummies(df)
    
    # Match training columns
    df = df.reindex(columns=columns, fill_value=0)
    
    # Predict
    prediction = model.predict(df)[0]
    
    return {"Predicted_Parts_Per_Hour": float(prediction)}
