import streamlit as st
import pandas as pd
import joblib

# Load model and label encoder
model = joblib.load("models/yield.pkl")
encoder = joblib.load("models/crop_encoder.pkl")

st.title(" Crop Yield Prediction 🌾 ")
st.write("Enter the crop and environmental details to predict the expected yield.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

crop = st.selectbox(
    "🌱 Crop",
    list(encoder.classes_)
)

area = st.number_input(
    "📍 Area (hectares)",
    min_value=0.1,
    value=1.0,
    step=0.1
)

rainfall = st.number_input(
    "🌧 Rainfall (mm)",
    min_value=0.0,
    value=800.0
)

temperature = st.number_input(
    "🌡 Temperature (°C)",
    min_value=0.0,
    value=25.0
)

fertilizer_used = st.number_input(
    "🧪 Fertilizer Used (kg)",
    min_value=0.0,
    value=100.0
)

soil_quality = st.slider(
    "🌍 Soil Quality",
    1,
    10,
    5
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🌾 Predict Yield"):

    crop_encoded = encoder.transform([crop])[0]

    input_df = pd.DataFrame({
        "crop": [crop_encoded],
        "area": [area],
        "rainfall": [rainfall],
        "temperature": [temperature],
        "fertilizer_used": [fertilizer_used],
        "soil_quality": [soil_quality]
    })

    prediction = model.predict(input_df)

    st.success(f"🌾 Predicted Crop Yield: **{prediction[0]:.2f} tons/hectare**")

    st.balloons()