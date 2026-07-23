import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CropVision AI",
    page_icon="🌱",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#06160d 0%, #081d12 40%, #0b2416 100%);
    color:#E8F5E9;
}
.main .block-container{
    background: transparent;
    padding-top:2rem;
    padding-left:2.5rem;
    padding-right:2.5rem;
}
section[data-testid="stSidebar"]{
    background:#07160d;
    border-right:1px solid #174c2d;
}
section[data-testid="stSidebar"] *{
    color:white;
}
.title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#57F287;
}
.subtitle{
    text-align:center;
    color:#9BC7A5;
    font-size:22px;
}
.card{
    background:linear-gradient(
        135deg,
        #12321d,
        #174826,
        #11331c
    );
    border:1px solid #246d3b;
    border-radius:18px;
    padding:22px;
    height:200px;
    color:white;
    transition:0.3s;
    box-shadow:
        0px 6px 20px rgba(0,0,0,.35);
}
.card:hover{
    transform:translateY(-6px);
    border-color:#43d17d;
    box-shadow:
        0px 10px 25px rgba(67,209,125,.20);
}
.card h3{
    font-size:20px;
    line-height:1.3;
    min-height:60px;
    margin-bottom:12px;
}
.card p{
    font-size:16px;
    line-height:1.5;
    min-height:50px;
}
div[data-testid="stMetric"]{
    background:#10281a;
    border:1px solid #246d3b;
    padding:15px;
    border-radius:15px;
}
.stButton>button{
    background:#2EB872;
    color:white;
    border:none;
    border-radius:10px;
}
.stButton>button:hover{
    background:#45D483;
}
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"]{
    background:#10281a;
    color:white;
}
header{
    visibility:hidden;
}
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🌱 CropVision AI")

page = st.sidebar.radio(
    "Select Module",
    (
        "🏠 Home",
        "🌱 Soil Fertility",
        "🍂 Crop Disease",
        "🌿 Fertilizer",
        "🐛 Pesticide",
        "📈 Yield Prediction",
        "ℹ About"
    )
)

# ================= HOME ================= #

if page=="🏠 Home":

    st.markdown("<div class='title'>CropVision AI</div>",
                unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Smart Agriculture using Machine Learning</div>",
                unsafe_allow_html=True)

    

    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
        <div class='card'>
        <h3>🌱 Soil Fertility</h3>
        Predict soil fertility using nutrient values.
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
        <h3>🍂 Disease Detection</h3>
        Predict crop diseases using ML.
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='card'>
        <h3>🌿 Fertilizer Recommendation</h3>
        Recommend the best fertilizer.
        </div>
        """,unsafe_allow_html=True)

    c4,c5=st.columns(2)

    with c4:
        st.markdown("""
        <div class='card'>
        <h3>🐛 Pesticide Recommendation</h3>
        Suggest the suitable pesticide.
        </div>
        """,unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class='card'>
        <h3>📈 Yield Prediction</h3>
        Predict crop yield accurately.
        </div>
        """,unsafe_allow_html=True)

    st.divider()

    col1,col2,col3,col4=st.columns(4)

    col1.metric("Modules","5")
    col2.metric("Models","5")
    col3.metric("Language","Python")
    col4.metric("Framework","Streamlit")

# ================= SOIL ================= #

elif page=="🌱 Soil Fertility":

    exec(open("pages/soil.py", encoding="utf-8").read())

# ================= DISEASE ================= #

elif page=="🍂 Crop Disease":

    exec(open("pages/disease.py", encoding="utf-8").read())

# ================= FERTILIZER ================= #

elif page=="🌿 Fertilizer":

    exec(open("pages/fertilizer.py",encoding="utf-8").read())

# ================= PESTICIDE ================= #

elif page=="🐛 Pesticide":

    exec(open("pages/pesticide.py",encoding="utf-8").read())

# ================= YIELD ================= #

elif page=="📈 Yield Prediction":

    exec(open("pages/yield.py",encoding="utf-8").read())

# ================= ABOUT ================= #

elif page=="ℹ About":

    st.title("About CropVision AI")

    st.write("""
CropVision AI is an intelligent agriculture application developed using
Machine Learning algorithms.

### Modules Included

✅ Soil Fertility Prediction

✅ Crop Disease Detection

✅ Fertilizer Recommendation

✅ Pesticide Recommendation

✅ Yield Prediction

### Technologies

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Joblib
    """)