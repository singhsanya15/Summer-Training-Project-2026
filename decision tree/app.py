import streamlit as st
import pandas as pd
import joblib

model = joblib.load("sales.pkl")


st.set_page_config(page_title="Quantity Sold Prediction", page_icon="💰")

st.title("💰 Quantity Sold Prediction App $")

st.write("Enter the Product_ID to predict the Quantity Sold: ")

quantity = st.number_input(
    "Product_ID",
    min_value=0,
    step=1
)

if st.button("Predict Quantity Sold"):

    input_data = pd.DataFrame({
        "Product_ID": [quantity]
    })
    prediction = model.predict(input_data)

    st.success(f"Predicted Quantity Sold: {prediction}")