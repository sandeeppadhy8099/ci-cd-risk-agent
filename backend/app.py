from fastapi import FastAPI
import numpy as np
from model import load_model
from rl_agent import get_state, choose_action

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "CI/CD Risk Agent Running"}

@app.post("/predict")
def predict(build_time:int, test_failures:int, code_changes:int, past_failures:int, deploy_time:int):

    features = np.array([[build_time, test_failures, code_changes, past_failures, deploy_time]])

    risk = model.predict_proba(features)[0][1]

    state = get_state(risk)
    action = choose_action(state)

    return {
        "risk_score": float(risk),
        "state": state,
        "action": action
    }