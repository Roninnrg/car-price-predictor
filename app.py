import streamlit as st
import requests

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("Оценка стоимости автомобиля")
st.write("Узнайте рыночную стоимость вашего авто с помощью ИИ (Цены указаны в индийских лакхах: 1 лакх ≈ 100 000 ₹)")

with st.form("Подать заявку"):
    # Передаем целые числа в value и step=1, чтобы убрать отображение десятых долей .00
    Year = st.number_input("Год выпуска", min_value=2000, max_value=2026, value=2015, step=1)
    Present_Price = st.number_input("Цена новой машины в салоне (в лакхах, например: 5.59)", min_value=0.1, max_value=100.0, value=5.59, step=0.1)
    Kms_Driven = st.number_input("Пробег в километрах", min_value=0, max_value=500000, value=25000, step=1000)
    Owner = st.number_input("Количество владельцев", min_value=0, max_value=10, value=0, step=1)
    
    Seller_Type_Individual = st.checkbox("Я являюсь частным лицом (не дилер)")
    Fuel_Type_Diesel = st.checkbox("Тип топлива: Дизель")
    Fuel_Type_Petrol = st.checkbox("Тип топлива: Бензин")
    Transmission_Manual = st.checkbox("Коробка передач: Механика")
    
    submit = st.form_submit_button("рассчитать стоимость")

if submit:
    data = {
        "Year": int(Year),
        "Present_Price": float(Present_Price),
        "Kms_Driven": int(Kms_Driven),
        "Owner": int(Owner),
        "Seller_Type_Individual": bool(Seller_Type_Individual),
        "Fuel_Type_Diesel": bool(Fuel_Type_Diesel),
        "Fuel_Type_Petrol": bool(Fuel_Type_Petrol),
        "Transmission_Manual": bool(Transmission_Manual)
    }
    
    response = requests.post("http://127.0.0.1:8000/car", json=data)
    predicted_price = response.json()["predicted_price"]
    
    # Выводим результат с указанием валюты датасета
    st.success(f"Рекомендуемая цена продажи вашего автомобиля: {predicted_price:.2f} лакх (≈ {predicted_price * 100:.0f} 000 рупий)")
