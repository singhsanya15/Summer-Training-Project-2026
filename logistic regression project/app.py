import streamlit as st
import pandas as pd
import joblib

model = joblib.load("cancer.pkl")


st.title("🩺 Breast Cancer Prediction")
st.write("Enter the cell values below to predict whether the tumor is Benign or Malignant.")


clump = st.number_input("Clump Thickness", min_value=1, max_value=10, value=1)
cell_size = st.number_input("Uniformity of Cell Size", min_value=1, max_value=10, value=1)
cell_shape = st.number_input("Uniformity of Cell Shape", min_value=1, max_value=10, value=1)
adhesion = st.number_input("Marginal Adhesion", min_value=1, max_value=10, value=1)
epithelial = st.number_input("Single Epithelial Cell Size", min_value=1, max_value=10, value=1)
bare = st.number_input("Bare Nuclei", min_value=1, max_value=10, value=1)
chromatin = st.number_input("Bland Chromatin", min_value=1, max_value=10, value=1)
nucleoli = st.number_input("Normal Nucleoli", min_value=1, max_value=10, value=1)
mitoses = st.number_input("Mitoses", min_value=1, max_value=10, value=1)


if st.button("Predict 🔍"):
    input_data = pd.DataFrame({
        "Clump Thickness": [clump],
        "Uniformity of Cell Size": [cell_size],
        "Uniformity of Cell Shape": [cell_shape],
        "Marginal Adhesion": [adhesion],
        "Single Epithelial Cell Size": [epithelial],
        "Bare Nuclei": [bare],
        "Bland Chromatin": [chromatin],
        "Normal Nucleoli": [nucleoli],
        "Mitoses": [mitoses]
    })

   
    prediction = model.predict(input_data)

    
    if prediction[0] == 1:
        st.error("🔴 Prediction: Malignant Tumor")
    else:
        st.success("🟢 Prediction: Benign Tumor")
