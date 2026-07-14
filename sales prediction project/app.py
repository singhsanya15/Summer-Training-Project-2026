import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("sales_prediction_model.pkl")

# Page Title
st.set_page_config(page_title="Unit Price Prediction", page_icon="💰")

st.title("💰 Unit Price Prediction App")

st.write("Enter the Quantity Sold to predict the Unit Price.")

# Input
quantity = st.number_input(
    "Quantity Sold",
    min_value=0,
    step=1
)

# Prediction
if st.button("Predict Unit Price"):

    input_data = pd.DataFrame({
        "Quantity_Sold": [quantity]
    })
    prediction = model.predict(input_data)

    st.success(f"Predicted Unit Price: ₹ {prediction}")