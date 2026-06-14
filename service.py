
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class ClientData(BaseModel):
    Year:int
    Present_Price:float
    Kms_Driven:int
    Owner:int
    Seller_Type_Individual:bool
    Fuel_Type_Diesel: bool
    Fuel_Type_Petrol: bool
    Transmission_Manual: bool
app = FastAPI()

model = joblib.load("model.pkl")

@app.post("/car")
def predict_car_price(data: ClientData):
    features = [
        data.Year,
        data.Present_Price,
        data.Kms_Driven,
        data.Owner,
        data.Fuel_Type_Diesel,
        data.Fuel_Type_Petrol,
        data.Seller_Type_Individual,
        data.Transmission_Manual
    ]
    
    predicted_price = model.predict([features])[0]
    return {"predicted_price": float(predicted_price)}