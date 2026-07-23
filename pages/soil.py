import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/soil_fertility_model.pkl")
encoder = joblib.load("models/soil_encoder.pkl")


st.title(" Soil Fertility Prediction 🌿")

# User Inputs
N = st.number_input("Nitrogen (N)", value=40)
P = st.number_input("Phosphorus (P)", value=35)
K = st.number_input("Potassium (K)", value=50)
ph = st.number_input("Soil pH", value=6.5)
moisture = st.number_input("Moisture (%)", value=35.0)
temperature = st.number_input("Temperature (°C)", value=25.0)

# Predict Button
if st.button("Predict"):

    data = pd.DataFrame({
        "N":[N],
        "P":[P],
        "K":[K],
        "ph":[ph],
        "moisture":[moisture],
        "temperature":[temperature]
    })

    prediction = model.predict(data)
    result = encoder.inverse_transform(prediction)



    st.success(f"Soil Fertility : {result[0]}")
    st.balloons()

