import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Salary Prediction App", page_icon="💰")

st.title("💰 Salary Prediction App")
st.write("This app predicts a person's **salary** based on their **years of experience** 📈")

model = joblib.load("salary.pkl")

st.sidebar.header("📋 Enter Details")

sr_no = st.sidebar.number_input("🔢 SrNo (just a placeholder, keep as 0)", min_value=0, max_value=1000, value=0)
years_experience = st.sidebar.slider("💼 Years of Experience", min_value=0.0, max_value=40.0, value=5.0, step=0.1)

input_data = pd.DataFrame({
    "SrNo": [sr_no],
    "YearsExperience": [years_experience]
})

st.subheader("🔍 Your Input Data")
st.write(input_data)


if st.button("🔮 Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"💵 Predicted Salary: **₹{prediction}**")

