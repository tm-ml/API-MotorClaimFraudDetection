"""Module for loading a trained pipeline and making predictions."""
import sys
import pickle
import pandas as pd

# from app.validation.validation import InputSchema
from app.model.custom_transformers import DropColumn, LogTransformer, IsZeroIndicator, Mapper, SelectColumn
from app.model import custom_transformers
from pathlib import Path


__version__ = "0.0.1"

# Base directory for loading model files:
BASE_DIR = Path(__file__).resolve(strict=True).parent


def unpickle_custom_classes():
    """Function to unpickle custom transformers."""
    sys.modules["__main__"] = custom_transformers


def load_pipeline():
    try:
        with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as file:
            model = pickle.load(file)
    except FileNotFoundError:
        print("Error: Model file not found.")
        sys.exit(1)
    return model


def predict_pipeline(input: pd.DataFrame):
    """Function to make a prediction using the trained model."""
    result = model.predict(input)
    return result[0]


unpickle_custom_classes()
model = load_pipeline()
