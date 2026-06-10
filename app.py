import streamlit as st

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Data Science Boot Camp",
    page_icon="🚀",
    layout="wide"
)

# =========================
# Theme
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #050816 0%,
        #0a192f 50%,
        #102a43 100%
    );
}

.main-header {
    text-align: center;
    padding: 20px;
}

.main-title {
    color: #4FC3F7;
    font-size: 3rem;
    font-weight: 700;
}

.sub-title {
    color: white;
    font-size: 1.2rem;
}

.card {
    background-color: rgba(17,34,64,0.85);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #1e3a5f;
    min-height: 320px;
}

.section-title {
    color: #64FFDA;
    font-size: 1.3rem;
    font-weight: bold;
    margin-bottom: 15px;
}

div[data-testid="stPageLink"] a {
    width: 100%;
    background: linear-gradient(90deg,#1565C0,#42A5F5);
    color: white !important;
    padding: 12px;
    border-radius: 10px;
    text-decoration: none;
    display: block;
    margin-bottom: 10px;
    text-align: center;
    font-weight: bold;
}

div[data-testid="stPageLink"] a:hover {
    background: linear-gradient(90deg,#1E88E5,#64B5F6);
}

.footer {
    text-align:center;
    color:#90CAF9;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div class="main-header">
    <div class="main-title">
        🚀 DATA SCIENCE & MACHINE LEARNING
    </div>
    <div class="sub-title">
        7 Day Intensive Hands-on Workshop
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# Menu Cards
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">💰 Business Analytics</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/app1_discount_calc.py",
        label="ระบบคำนวณส่วนลด"
    )

    st.page_link(
        "pages/sale_predict.py",
        label="พยากรณ์ยอดขาย"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">🧹 Data Preparation</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/clean_By_B2_app.py",
        label="Clean Data By B"
    )

    st.page_link(
        "pages/clean_app.py",
        label="Data Cleaning"
    )

    st.page_link(
        "pages/transform_app.py",
        label="Data Transformation"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">🤖 Machine Learning</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/EDA_app.py",
        label="EDA Dashboard"
    )

    st.page_link(
        "pages/truck_predict.py",
        label="Transportation Prediction"
    )

    st.page_link(
        "pages/classify_redbull_sale.py",
        label="Sales Opportunity"
    )

    st.page_link(
        "pages/clustering_segment.py",
        label="K-Means Clustering"
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="footer">
    🧠 Python • Data Science • Machine Learning • AI
</div>
""", unsafe_allow_html=True)
