import streamlit as st

st.set_page_config(
    page_title="อย่าบอกใคร999",
    page_icon="🚀",
    layout="wide"
)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #050816 0%,
        #081229 40%,
        #0d1b3d 100%
    );
    color: white;
}

/* Rainbow Logo */
.logo {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    background: linear-gradient(
        90deg,
        #ff0000,
        #ff7f00,
        #ffff00,
        #00ff00,
        #00ffff,
        #0000ff,
        #8b00ff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s infinite alternate;
}

@keyframes glow {
    from {
        filter: drop-shadow(0 0 10px #00ffff);
    }
    to {
        filter: drop-shadow(0 0 30px #8b00ff);
    }
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #9dd9ff;
    font-size: 24px;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: rgba(0,0,0,0.35);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #00c3ff;
    box-shadow: 0 0 25px rgba(0,195,255,0.3);
    margin-bottom: 25px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 15px;
    border: 1px solid #00d9ff;
    background: linear-gradient(
        90deg,
        #0f172a,
        #1e3a8a
    );
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px #00d9ff;
}

/* Section Header */
.section-title {
    color: #00e5ff;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown(
    '<div class="logo">🌈 อย่าบอกใคร999 🌈</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
<h3>🚀 Boot Camp: Data Science and Machine Learning</h3>
<p>
7 Day Intensive Hands-on Workshop<br>
เรียนรู้ Data Analytics, Machine Learning และ AI
แบบลงมือทำจริง
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# Menu
# =========================
st.markdown(
    '<div class="section-title">📊 Data Processing</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc.py")

    if st.button("🧹 การทำความสะอาดข้อมูล"):
        st.switch_page("pages/clean_app.py")

    if st.button("🧹 การทำความสะอาดข้อมูล By B"):
        st.switch_page("pages/clean_By_B2_app.py")

    if st.button("🪥 การแปลงข้อมูล"):
        st.switch_page("pages/transform_app.py")

with col2:
    if st.button("📈 EDA Dashboard"):
        st.switch_page("pages/EDA_app.py")

    if st.button("💰 พยากรณ์ยอดขาย"):
        st.switch_page("pages/sale_predict.py")

    if st.button("🚛 การขนส่ง"):
        st.switch_page("pages/truck_predict.py")

    if st.button("🐂 ทำนายโอกาสขาย"):
        st.switch_page("pages/classify_redbull_sale.py")

st.markdown(
    '<div class="section-title">🤖 Machine Learning</div>',
    unsafe_allow_html=True
)

col3, col4 = st.columns(2)

with col3:
    if st.button("⭕ การทำกลุ่ม K-Means"):
        st.switch_page("pages/clustering_segment.py")

with col4:
    if st.button("🛒 การทำแนะนำสินค้า"):
        st.switch_page("pages/association_items.py")

    if st.button("🏷️ สินค้าที่แนะนำ"):
        st.switch_page("pages/association_recommend.py")

st.markdown("---")
st.caption("© 2026 อย่าบอกใคร999 | AI Analytics Platform")
