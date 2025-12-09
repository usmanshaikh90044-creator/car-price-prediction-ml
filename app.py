import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

year = st.number_input("Year", min_value=1990, max_value=2025)
km_driven = st.number_input("Kilometers Driven", min_value=0)

st.markdown("### Fuel Type")
st.markdown("0 = CNG | 1 = Diesel | 2 = Petrol")
fuel = st.number_input("Fuel", min_value=0, max_value=2)

st.markdown("### Seller Type")
st.markdown("0 = Dealer | 1 = Individual")
seller_type = st.number_input("Seller Type", min_value=0, max_value=1)

st.markdown("### Transmission")
st.markdown("0 = Automatic | 1 = Manual")
transmission = st.number_input("Transmission", min_value=0, max_value=1)

st.markdown("### Owner")
st.markdown("0 = First | 1 = Second | 2 = Third | 3 = Fourth+ | 4 = Test Drive")
owner = st.number_input("Owner", min_value=0, max_value=4)

mileage = st.number_input("Mileage")
engine = st.number_input("Engine CC")
max_power = st.number_input("Max Power")
torque = st.number_input("Torque")
seats = st.number_input("Seats", min_value=1)

if st.button("Predict Price"):
    input_data = np.array([[year, km_driven, fuel, seller_type,
                            transmission, owner, mileage,
                            engine, max_power, torque, seats]])

    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Car Price: ₹ {int(prediction[0])}")
