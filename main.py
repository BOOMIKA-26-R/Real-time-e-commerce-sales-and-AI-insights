import pandas as pd
import numpy as np
from fastapi import FastAPI
import joblib
from sklearn.ensemble import RandomForestRegressor

app = FastAPI()


X = np.random.rand(100, 1) * 100  
y = X.flatten() * 1.5 + np.random.randn(100) 
model = RandomForestRegressor(n_estimators=10).fit(X, y)

@app.get("/")
def home():
    return {"status": "E-commerce API is Live"}

@app.get("/predict")
def predict(traffic: float):

    prediction = model.predict([[traffic]])

    return {"predicted_revenue": float(prediction[0])}

@app.get("/live-data")
def get_live_data():

    categories = ["Electronics", "Fashion", "Home Decor"]
    data = {
        "category": np.random.choice(categories),
        "sales": round(np.random.uniform(20, 500), 2),
        "traffic": np.random.randint(50, 1000),
        "customer_sentiment": np.random.uniform(-1, 1) # Task 8: AI Sentiment
    }
    return data
