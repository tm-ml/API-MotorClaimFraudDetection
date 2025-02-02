"""Main module for FastAPI application."""
import pandas as pd
from fastapi import FastAPI

from app.model.custom_transformers import DropColumn, LogTransformer, IsZeroIndicator, Mapper, SelectColumn
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from app.validation.validation import InputSchema, PredictionOut


app = FastAPI()


@app.get("/")
def home():
    """Fraud check endpoint"""
    return {"fraud_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: InputSchema):
    """Predict endpoint."""
    input_dict = payload.model_dump()
    input_df = pd.DataFrame([input_dict])
    result  = predict_pipeline(input_df)
    result = int(result)
    # print(f'The result is: {result}')
    return {"Result": result}



