from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "CitySense360 API running"}

@app.get("/predict/traffic")
def predict_traffic(v1: int, v2: int, v3: int):
    from app.traffic_model import predict_next
    result = predict_next(v1, v2, v3)
    return {"prediction": int(result)}
