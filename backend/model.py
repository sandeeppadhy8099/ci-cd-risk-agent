import pandas as pd
from xgboost import XGBClassifier
import joblib

def train_model():
    data = pd.read_csv("../data/dataset.csv")

    X = data.drop("label", axis=1)
    y = data["label"]

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X, y)

    joblib.dump(model, "../models/xgb_model.pkl")

    print("✅ Model trained and saved!")

def load_model():
    return joblib.load("../models/xgb_model.pkl")