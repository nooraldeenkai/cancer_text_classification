from fastapi import FastAPI
from app.ML.model import predict_pipeline
from app.models.predict import  Input, Output

app = FastAPI()



#health check to log the app is working
@app.get("/")
def home():
    return {"healthcheck": "OK"}



#language endpoint that returns detected language 
@app.post("/prediction", response_model=Output)
def predict(payload: Input):
    cancer_type = predict_pipeline(payload.text, payload.model)
    return {"cancer_type": cancer_type}