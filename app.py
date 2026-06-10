import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown(''':rainbow[อย่าบอกใคร999] ''')
st.write("##### การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("🧹 การทำความสะอาดข้อมูล By B"):
    st.switch_page("pages/clean_By_B2_app.py")
elif st.button("🧹 การทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_app.py")
elif st.button("🪥 การแปลงข้อมูล"):
    st.switch_page("pages/transform_app.py")
elif st.button("🦆 กราฟฟฟฟ"):
    st.switch_page("pages/EDA_app.py")
elif st.button("💰 พยากรณ์ยอดขาย"):
    st.switch_page("pages/sale_predict.py")
elif st.button("🚛 การขนส่ง"):
    st.switch_page("pages/truck_predict.py")
elif st.button("🐂 ทำนายโอกาสขาย"):
    st.switch_page("pages/classify_redbull_sale.py")
elif st.button("⭕ การทำกลุ่ม Kmeans"):
    st.switch_page("pages/clustering_segment.py")
elif st.button("🛒 การทำแนะนำสินค้า"):
    st.switch_page("pages/association_items.py")
