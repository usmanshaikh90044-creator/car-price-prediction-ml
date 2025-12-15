import pickle
import pandas as pd
import streamlit as st
import os

# -------------------------------
# Safe file loading
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "model_rf.pkl"), "rb"))
encoders = pickle.load(open(os.path.join(BASE_DIR, "label_encoders.pkl"), "rb"))

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Enter car details to predict the selling price.")

year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2018)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)

fuel = st.selectbox("Fuel Type", encoders["fuel"].classes_)
seller_type = st.selectbox("Seller Type", encoders["seller_type"].classes_)
transmission = st.selectbox("Transmission", encoders["transmission"].classes_)
owner = st.selectbox("Owner Type", encoders["owner"].classes_)

mileage = st.number_input("Mileage (km/l)", min_value=0.0, value=18.0)
engine = st.number_input("Engine (cc)", min_value=0, value=1197)
max_power = st.number_input("Max Power (bhp)", min_value=0.0, value=82.0)
torque = st.number_input("Torque (Nm)", min_value=0.0, value=113.0)
seats = st.number_input("Seats", min_value=1, max_value=10, value=5)

if st.button("Predict Price"):
    input_data = {
        "year": year,
        "km_driven": km_driven,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "torque": torque,
        "seats": seats
    }

    input_df = pd.DataFrame([input_data])

    for col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Car Price: ₹ {round(prediction, 2)}")
