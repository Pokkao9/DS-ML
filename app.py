import streamlit as st

st.set_page_config(
    page_title="Boot Camp DS & ML",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CSS Theme
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #050816 0%, #0A192F 100%);
}

.main-title {
    text-align: center;
    color: #4FC3F7;
    font-size: 3rem;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: white;
    font-size: 1.2rem;
}

.card {
    background-color: #112240;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #233554;
    box-shadow: 0 0 15px rgba(79,195,247,0.15);
}

.section-title {
    color: #64FFDA;
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.stButton button {
    width: 100%;
    height: 60px;
    border-radius: 12px;
    background: linear-gradient(90deg,#1565C0,#42A5F5);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg,#42A5F5,#64B5F6);
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown(
    "<div class='main-title'>🚀 DATA SCIENCE & MACHINE LEARNING BOOT CAMP</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>7 Day Intensive Hands-on Workshop</div>",
    unsafe_allow_html=True
)

st.divider()

# =========================
# Menu
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>💰 Business Analytics</div>", unsafe_allow_html=True)

    if st.button("ระบบคำนวณส่วนลด"):
        st.switch_page("pages/app1_discount_calc.py")

    if st.button("พยากรณ์ยอดขาย"):
        st.switch_page("pages/sale_predict.py")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🧹 Data Preparation</div>", unsafe_allow_html=True)

    if st.button("Clean Data By B"):
        st.switch_page("pages/clean_By_B2_app.py")

    if st.button("Data Cleaning"):
        st.switch_page("pages/clean_app.py")

    if st.button("Data Transformation"):
        st.switch_page("pages/transform_app.py")

    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🤖 Machine Learning</div>", unsafe_allow_html=True)

    if st.button("EDA Dashboard"):
        st.switch_page("pages/EDA_app.py")

    if st.button("Transportation Prediction"):
        st.switch_page("pages/truck_predict.py")

    if st.button("Sales Opportunity"):
        st.switch_page("pages/classify_redbull_sale.py")

    if st.button("K-Means Clustering"):
        st.switch_page("pages/clustering_segment.py")

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Footer
st.markdown(
    """
    <center>
        <h4 style='color:#64FFDA'>
        🧠 Python • Data Science • Machine Learning • AI
        </h4>
    </center>
    """,
    unsafe_allow_html=True
