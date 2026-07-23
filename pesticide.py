import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/pesticide.pkl")

st.title(" Pesticide Recommendation 🧪")
st.write("Enter the crop details below to get the recommended pesticide.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

crop = st.selectbox(
    "🌾 Crop",
    [
        "Rice",
        "Wheat",
        "Maize",
        "Cotton",
        "Sugarcane",
        "Tomato",
        "Potato",
        "Onion"
    ]
)

disease = st.selectbox(
    "🦠 Disease",
    [
        "Leaf Spot",
        "Blight",
        "Rust",
        "Powdery Mildew",
        "Wilt",
        "Mosaic",
        "Healthy"
    ]
)

severity = st.selectbox(
    "⚠️ Disease Severity",
    [
        "Low",
        "Medium",
        "High"
    ]
)

humidity = st.slider(
    "💧 Humidity (%)",
    0,
    100,
    60
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🧪 Recommend Pesticide"):

    input_df = pd.DataFrame({
        "crop": [crop],
        "disease": [disease],
        "severity": [severity],
        "humidity": [humidity]
    })

    # Apply same preprocessing used during training
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction = model.predict(input_df)

    st.success(f"✅ Recommended Pesticide: **{prediction[0]}**")

    st.balloons()