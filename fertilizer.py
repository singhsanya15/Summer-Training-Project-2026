import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/fertilizer.pkl")

st.title(" Fertilizer Recommendation🌱 ")
st.write("Enter the crop and soil details to get the recommended fertilizer.")

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

soil = st.selectbox(
    "🌍 Soil Type",
    [
        "Sandy",
        "Loamy",
        "Clay",
        "Black",
        "Red"
    ]
)

N = st.number_input("Nitrogen (N)", 0, 200, 60)

P = st.number_input("Phosphorus (P)", 0, 200, 40)

K = st.number_input("Potassium (K)", 0, 200, 50)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🌱 Recommend Fertilizer"):

    input_df = pd.DataFrame({
        "crop":[crop],
        "soil":[soil],
        "N":[N],
        "P":[P],
        "K":[K]
    })

    # Same preprocessing used during training
    input_df = pd.get_dummies(input_df)

    # Training columns
    train_columns = model.feature_names_in_

    # Add missing columns
    input_df = input_df.reindex(columns=train_columns, fill_value=0)

    prediction = model.predict(input_df)

    # Convert prediction to fertilizer name
    fertilizers = [
        "DAP (Di-Ammonium Phosphate)",
        "MOP (Muriate of Potash)",
        "NPK 20-20-20",
        "Urea",
        "Vermicompost / Organic Manure"
    ]

    result = fertilizers[prediction.argmax()]

    st.success(f"✅ Recommended Fertilizer: **{result}**")
    st.balloons()