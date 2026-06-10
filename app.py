import streamlit as st

st.set_page_config(
    page_title="Boot Camp DSML",
    page_icon="🚀",
    layout="wide"
)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #050816 0%, #0f172a 50%, #081126 100%);
}

/* ซ่อน Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hero */
.hero {
    text-align:center;
    padding:40px;
    border-radius:20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    border:1px solid rgba(0,170,255,0.2);
    box-shadow: 0 0 30px rgba(0,170,255,0.25);
    margin-bottom:30px;
}

.hero-title {
    font-size:52px;
    font-weight:800;
    color:white;
}

.hero-sub {
    font-size:22px;
    color:#7dd3fc;
}

.hero-desc {
    color:#cbd5e1;
    font-size:18px;
}

/* ปุ่ม */
.stButton > button {
    width:100%;
    height:120px;
    border-radius:20px;
    border:1px solid #0ea5e9;
    background: rgba(15,23,42,0.9);
    color:white;
    font-size:20px;
    font-weight:bold;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-5px);
    box-shadow: 0px 0px 25px #38bdf8;
    border:1px solid #38bdf8;
}

/* Card */
.card {
    background: rgba(255,255,255,0.04);
    padding:15px;
    border-radius:15px;
    border:1px solid rgba(56,189,248,0.15);
    text-align:center;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 DATA SCIENCE & MACHINE LEARNING</div>
    <div class="hero-sub">7 Day Intensive Hands-on Workshop</div>
    <br>
    <div class="hero-desc">
        Python • Data Cleaning • EDA • Machine Learning • Forecasting
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# Menu
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💰\nระบบคำนวณส่วนลด"):
        st.switch_page("pages/app1_discount_calc.py")

with col2:
    if st.button("🧹\nData Cleaning By B"):
        st.switch_page("pages/clean_By_B2_app.py")

with col3:
    if st.button("🧹\nData Cleaning"):
        st.switch_page("pages/clean_app.py")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("🪥\nData Transform"):
        st.switch_page("pages/transform_app.py")

with col5:
    if st.button("📊\nEDA Dashboard"):
        st.switch_page("pages/EDA_app.py")

with col6:
    if st.button("💰\nSales Forecast"):
        st.switch_page("pages/sale_predict.py")

col7, col8, col9 = st.columns(3)

with col7:
    if st.button("🚛\nTransport Prediction"):
        st.switch_page("pages/truck_predict.py")

with col8:
    if st.button("🐂\nSale Classification"):
        st.switch_page("pages/classify_redbull_sale.py")

with col9:
    if st.button("⭕\nKMeans Clustering"):
        st.switch_page("pages/clustering_segment.py")

# =========================
# Footer
# =========================
st.markdown("""
<br><br>
<center>
    <span style='color:#38bdf8;font-size:16px'>
        ⚡ Boot Camp Data Science & Machine Learning
    </span>
</center>
""", unsafe_allow_html=True)
