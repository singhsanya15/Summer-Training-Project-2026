import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Smoker Prediction App", page_icon="🚬")

st.title("🚬 Smoker Prediction App")
st.write("This app predicts whether a person is likely a **smoker** based on their **age, BMI, and sex** 🩺")

model = joblib.load("insurance_model.pkl")

st.sidebar.header("📋 Enter Person's Details")

age = st.sidebar.slider("🎂 Age", min_value=18, max_value=100, value=30)
bmi = st.sidebar.slider("⚖️ BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
sex = st.sidebar.radio("🧑 Sex", ["male", "female"])

sex_male = 1 if sex == "male" else 0

input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "sex_male": [sex_male]
})

st.subheader("🔍 Your Input Data")
st.write(input_data)

if st.button("🔮 Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == "yes":
        st.error("🚬 Prediction: This person is likely a **SMOKER**")
    else:
        st.success("✅ Prediction: This person is likely a **NON-SMOKER**")

st.markdown("---")
