import streamlit as st

st.set_page_config(
    page_title="Boot Camp AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================
st.markdown("""
<style>

/* พื้นหลังหลัก */
.stApp {
    background: linear-gradient(
        135deg,
        #050816 0%,
        #07152d 40%,
        #0a1f44 100%
    );
    color: white;
}

/* ซ่อนเมนู Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* หัวข้อ */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: #6ad5ff;
    text-shadow:
        0 0 10px #00bfff,
        0 0 20px #00bfff,
        0 0 40px #00bfff;
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:#d7e7ff;
    font-size:1.2rem;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,191,255,0.4);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(12px);
    box-shadow:
        0 0 20px rgba(0,191,255,0.25),
        inset 0 0 20px rgba(255,255,255,0.03);
    margin-bottom:20px;
}

/* ปุ่ม */
.stButton>button {
    width: 100%;
    height: 70px;
    border-radius: 18px;

    border: 1px solid #00bfff;
    background: linear-gradient(
        90deg,
        #0b1835,
        #112b5c
    );

    color: white;
    font-size: 18px;
    font-weight: 700;

    box-shadow:
        0 0 10px #00bfff,
        0 0 20px rgba(0,191,255,0.5);

    transition: all 0.3s ease;
}

/* Hover */
.stButton>button:hover {
    transform: translateY(-5px);
    background: linear-gradient(
        90deg,
        #00bfff,
        #005eff
    );

    box-shadow:
        0 0 20px #00bfff,
        0 0 40px #00bfff,
        0 0 60px #00bfff;
}

/* Animation Glow */
.glow {
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {
        text-shadow:
            0 0 10px #00bfff,
            0 0 20px #00bfff;
    }
    to {
        text-shadow:
            0 0 20px #00bfff,
            0 0 40px #00bfff,
            0 0 60px #00bfff;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================
st.markdown(
    """
    <h1 class="main-title glow">
        🚀 AI & Data Science Boot Camp
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        7 Day Intensive Hands-on Workshop
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# Info Card
# ==========================
st.markdown("""
<div class="card">
<h3>📊 Data Science & Machine Learning Platform</h3>
<p>
เรียนรู้การจัดการข้อมูล การวิเคราะห์ข้อมูล
Machine Learning และการสร้างโมเดลทำนาย
ผ่าน Workshop แบบลงมือทำจริง
</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# Menu
# ==========================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💰 ระบบคำนวณส่วนลด"):
        st.switch_page("pages/app1_discount_calc.py")

    if st.button("🧹 Data Cleaning"):
        st.switch_page("pages/clean_app.py")

    if st.button("🪥 Data Transform"):
        st.switch_page("pages/transform_app.py")

with col2:
    if st.button("📈 EDA Dashboard"):
        st.switch_page("pages/EDA_app.py")

    if st.button("💰 Sales Forecast"):
        st.switch_page("pages/sale_predict.py")

    if st.button("🚛 Logistics Forecast"):
        st.switch_page("pages/truck_predict.py")

with col3:
    if st.button("🐂 Sale Classification"):
        st.switch_page("pages/classify_redbull_sale.py")

    if st.button("⭕ K-Means Clustering"):
        st.switch_page("pages/clustering_segment.py")

    if st.button("🧹 Cleaning By B"):
        st.switch_page("pages/clean_By_B2_app.py")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <center>
        <span style='color:#6ad5ff'>
            ⚡ Powered by Python • Streamlit • Machine Learning
        </span>
    </center>
    """,
    unsafe_allow_html=True
)
