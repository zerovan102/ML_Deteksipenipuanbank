import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Fraud Detection API", description="AI powered Real-time Bank Fraud Detection")

# Define the data structure matching the pipeline requirements
class Transaction(BaseModel):
    TransactionAmount: float
    TransactionType: int
    Location: int
    Channel: int
    CustomerAge: int
    CustomerOccupation: int
    TransactionDuration: int
    LoginAttempts: int
    AccountBalance: float
    TransactionHour: int
    DayOfWeek: int
    TimeSinceLast: float

# Attempt to load the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'fraud_detection_pipeline.pkl')
try:
    pipeline = joblib.load(model_path)
except Exception as e:
    pipeline = None
    print(f"Warning: Could not load the pipeline model. Ensure it exists. Error: {e}")

@app.post("/predict")
async def predict_fraud(transaction: Transaction):
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Machine Learning Model is currently unavailable/loading.")
    
    # Convert input to DataFrame (pipeline expects a DataFrame with raw feature columns)
    input_data = pd.DataFrame([transaction.dict()])
    
    try:
        model = pipeline.named_steps['classifier']
        prediction = model.predict(input_data)
        # Assuming the model returns cluster labels (0-3). Fraud could be defined as cluster 3 (highest risk) etc.
        # Often clustering outputs an integer.
        fraud_risk = int(prediction[0])
        
        # Calculate a mock probability based on risk tier
        if fraud_risk == 3:
            probability = 98.5
            status = "CRITICAL RISK"
        elif fraud_risk == 2:
            probability = 72.1
            status = "HIGH RISK"
        elif fraud_risk == 1:
            probability = 34.0
            status = "MODERATE RISK"
        else:
            probability = 5.2
            status = "LOW RISK"
            
        return {
            "prediction": fraud_risk,
            "status": status,
            "probability": probability,
            "message": "Transaction analyzed successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Mount static files for the frontend, serving index.html natively
static_dir = os.path.join(os.path.dirname(__file__), 'static')

@app.get("/")
async def root():
    return FileResponse(os.path.join(static_dir, 'index.html'))

# Mount everything else in static folder
app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
