import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/crop_disease_model.pkl")

st.title(" Crop Disease Detection 🍂")
st.write(
    "Enter the crop symptoms below to predict the most likely crop disease."
)

st.markdown("---")


leaf_spots = st.slider("🍂 Leaf Spots", 0.0, 10.0, 5.0)

yellowing = st.slider("🟡 Yellowing", 0.0, 10.0, 5.0)

wilting = st.slider("🥀 Wilting", 0.0, 10.0, 5.0)

white_powder = st.slider("⚪ White Powder", 0.0, 10.0, 5.0)

humidity = st.slider(
    "💧 Humidity (%)",
    0,
    100,
    60
)


# ----------------------------
# Prediction
# ----------------------------

if st.button("🔍 Predict Disease"):

    input_data = pd.DataFrame({
        "leaf_spots": [leaf_spots],
        "yellowing": [yellowing],
        "wilting": [wilting],
        "white_powder": [white_powder],
        "humidity": [humidity]
    })

    prediction = model.predict(input_data)

    st.success(f"🌱 Predicted Disease: **{prediction[0]}**")

    st.balloons()