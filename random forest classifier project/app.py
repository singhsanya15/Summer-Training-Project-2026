import streamlit as st
import pandas as pd
import joblib

model = joblib.load("weather.pkl")

st.set_page_config(page_title="Weather Type Prediction 🌤️")

st.title("🌤️Weather Type Prediction App")
st.write("This app predicts the waether type according to input details ")

st.sidebar.title("ℹ️ About")

st.sidebar.info("""
This Weather Prediction App predicts weather type using a Machine Learning model.

### Features
                
✔️ Instant Prediction

✔️ User Friendly

✔️ Streamlit + Python
""")

Temperature = st.number_input("🌡Temperature (°C)", value=20.0)
Humidity = st.number_input("💧 Humidity (%)", value=70.0)
Wind_Speed = st.number_input("🌬 Wind Speed (km/h)", value=10.0)
Precipitation = st.number_input("🌧 Precipitation (%)", value=20.0)
Pressure = st.number_input("🌍 Atmospheric Pressure ", value=1010.0)
Visibility = st.number_input("👀 Visibility (km)", value=5.0)
UV_Index = st.number_input("☀️ UV Index", value=3.0)

if st.button(" 🔍 Predict"):
    data = pd.DataFrame([[Temperature, Humidity, Wind_Speed, Precipitation,
                           Pressure, Visibility, UV_Index]],
                         columns=["Temperature", "Humidity", "Wind Speed",
                                  "Precipitation (%)", "Atmospheric Pressure",
                                  "Visibility (km)", "UV Index"])

    pred = model.predict(data)[0]  

    if pred[0] == 1:
        result = "Rainy 🌧"
    elif pred[1] == 1:
        result = "Snowy ❄️"
    elif pred[2] == 1:
        result = "Sunny ☀️"
    else:
        result = "Cloudy ☁️"

    st.success(f"Predicted Weather Type: {result}")

