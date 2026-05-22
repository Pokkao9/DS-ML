import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats.mstats import winsorize
import io
import warnings
warnings.filterwarnings('ignore')

# Custom CSS for a more beautiful title and overall look
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3em;
        color: #CD113B; /* Red Bull Red */
        text-align: center;
        text-shadow: 2px 2px 4px #aaa;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-bottom: 1em;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        font-size: 1.1em;
        margin: 0 auto;
        display: block;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stWarning, .stInfo, .stSuccess, .stError {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set Streamlit page config
st.set_page_config(layout="wide", page_title="Enhanced Data Cleaning App 🐂")

# --- Streamlit App Title and Header ---
st.markdown('<h1 class="main-title">🐂 Enhanced Data Cleaning Workshop App</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">ยินดีต้อนรับสู่แอปพลิเคชัน Data Cleaning ที่สวยงามยิ่งขึ้น!</p>', unsafe_allow_html=True)
st.markdown("""
--- 
ท่านสามารถอัปโหลดไฟล์ CSV และเลือกขั้นตอนการทำความสะอาดข้อมูลได้ 
<br>
""", unsafe_allow_html=True)
st.error("**🚨 ข้อควรระวัง:** แอปพลิเคชันนี้ออกแบบมาสำหรับชุดข้อมูลที่มีโครงสร้างเหมือน `redbull_workshop_dirty.csv` เท่านั้น")

# --- File Uploader ---
uploaded_file = st.file_uploader("อัปโหลดไฟล์ CSV ของคุณที่นี่", type=["csv"], help="เลือกไฟล์ CSV ที่คุณต้องการทำความสะอาด")

if uploaded_file is not None:
    df_raw = pd.read_csv(uploaded_file)
    df = df_raw.copy()
    st.success("✅ อัปโหลดไฟล์สำเร็จแล้ว! เตรียมพร้อมสำหรับการทำความสะอาดข้อมูล")

    st.markdown("### ข้อมูลดิบ (5 แถวแรก)")
    st.dataframe(df_raw.head())

    # --- Data Cleaning Steps (as functions) ---

    def perform_data_exploration(data):
        st.subheader("📊 1. การสำรวจข้อมูลเบื้องต้น (Data Exploration)")
        with st.expander("ดูรายละเอียดการสำรวจข้อมูล"): # Use expander for cleaner UI
            st.write("#### ขนาดข้อมูล (Data Shape):")
            st.write(f"จำนวนแถว: {data.shape[0]:,}, จำนวนคอลัมน์: {data.shape[1]}")
            st.write("#### ข้อมูลทั่วไป (Data Info):")
            buffer = io.StringIO()
            data.info(buf=buffer)
            st.text(buffer.getvalue())
            st.write("#### สถิติเชิงพรรณนา (Descriptive Statistics):")
            st.dataframe(data.describe(include='all'))
        return data

    def handle_duplicate_data(data):
        st.subheader("👥 2. การจัดการข้อมูลซ้ำ (Duplicate Data)")
        with st.expander("ดูรายละเอียดการจัดการข้อมูลซ้ำ"): # Use expander
            exact_dups = data.duplicated()
            exact_dup_count = exact_dups.sum()
            if exact_dup_count > 0:
                st.warning(f"พบข้อมูลซ้ำ 100% จำนวน **{exact_dup_count:,} แถว**")
                st.dataframe(data[exact_dups])
                data = data.drop_duplicates()
                st.success(f"✅ ลบข้อมูลซ้ำแล้ว: เหลือ **{len(data):,} แถว**")
            else:
                st.info("ℹ️ ไม่พบ Exact Duplicate ในข้อมูลนี้")
        return data

    def handle_inconsistent_data(data):
        st.subheader("🔄 3. การจัดการข้อมูลไม่สอดคล้องกัน (Inconsistent Data)")
        with st.expander("ดูรายละเอียดการจัดการข้อมูลไม่สอดคล้องกัน"): # Use expander
            st.write("##### ค่าที่ไม่สอดคล้องกัน (ก่อนแก้ไข):")
            cat_cols = ['Region', 'Product_Variant', 'Channel']
            for col in cat_cols:
                unique_vals = data[col].unique()
                st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**")
                st.json(unique_vals.tolist()) # Display as JSON for readability

            st.info("กำลังดำเนินการแก้ไขค่าที่ไม่สอดคล้องกัน...")

            data['Region'] = data['Region'].str.strip().str.lower()
            region_mapping = {
                'th-central': 'TH-Central', 'th central': 'TH-Central',
                'thailand central': 'TH-Central', 'thailand-central': 'TH-Central',
                'thailand': 'TH-Central',
                'usa-east': 'USA-East', 'us east': 'USA-East',
                'united states east': 'USA-East', 'u.s.a.': 'USA-East',
                'europe-eu': 'Europe-EU', 'eu': 'Europe-EU',
                'europe': 'Europe-EU', 'european union': 'Europe-EU',
                'asia-pacific': 'Asia-Pacific', 'asia-pac': 'Asia-Pacific',
                'apac': 'Asia-Pacific', 'asia pacific': 'Asia-Pacific'
            }
            data['Region'] = data['Region'].replace(region_mapping)
            data['Region'] = data['Region'].str.upper()

            data['Product_Variant'] = data['Product_Variant'].str.strip().str.lower()
            product_variant_mapping = {
                'original blue': 'Original Blue', 'original  blue': 'Original Blue',
                'krating daeng 250': 'Krating Daeng 250',
                'red edition': 'Red Edition',
                'sugarfree': 'Sugarfree', 'sugar free': 'Sugarfree',
                'sugarfree ': 'Sugarfree', 'sugar-free': 'Sugarfree',
                'tropical edition': 'Tropical Edition', 'tropical  edition': 'Tropical Edition',
                'tropical': 'Tropical Edition',
            }
            data['Product_Variant'] = data['Product_Variant'].replace(product_variant_mapping)

            data['Channel'] = data['Channel'].str.strip().str.lower()
            channel_mapping = {
                'social media': 'Social Media', 'social_media': 'Social Media',
                'tv ad': 'TV Ad', 'tv ads': 'TV Ad',
                'tv advertisement': 'TV Ad', 'television ad': 'TV Ad',
                'in-store promo': 'In-store Promo',
                'f1 sponsorship': 'F1 Sponsorship',
                'extreme sports': 'Extreme Sports'
            }
            data['Channel'] = data['Channel'].replace(channel_mapping)
            data['Channel'] = data['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x)

            data['Date'] = pd.to_datetime(data['Date'], format='mixed')

            st.success("✅ แก้ไข Inconsistent Values สำเร็จแล้ว!")
            st.write("##### ค่าที่ไม่สอดคล้องกัน (หลังแก้ไข):")
            for col in cat_cols:
                unique_vals = data[col].unique()
                st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**")
                st.json(unique_vals.tolist())
        return data

    def handle_missing_data(data):
        st.subheader("📭 4. การจัดการข้อมูลที่หายไป (Missing Data)")
        with st.expander("ดูรายละเอียดการจัดการข้อมูลที่หายไป"): # Use expander
            missing_count = data.isnull().sum()
            st.write("##### จำนวน Missing Values ก่อนแก้ไข:")
            if missing_count.sum() > 0:
                st.dataframe(missing_count[missing_count > 0])

                median_marketing = data['Marketing_Spend'].median()
                data['Marketing_Spend'] = data['Marketing_Spend'].fillna(median_marketing)
                st.info(f'**✅ Marketing_Spend:** เติมด้วย Median = **{median_marketing:,.2f}**')

                median_score = data['Customer_Score'].median()
                data['Customer_Score'] = data['Customer_Score'].fillna(median_score)
                st.info(f'**✅ Customer_Score:** เติมด้วย Median = **{median_score}**')

                st.success("✅ แก้ไข Missing Values สำเร็จแล้ว!")
                st.write(f"##### จำนวน Missing Values หลังแก้ไข: **{data.isnull().sum().sum()} ค่า** (ควรเป็น 0)")
            else:
                st.info("ℹ️ ไม่พบ Missing Data ในข้อมูลนี้")
        return data

    def handle_noisy_data(data):
        st.subheader("📢 5. การจัดการข้อมูลผิดพลาด (Noisy Data)")
        with st.expander("ดูรายละเอียดการจัดการข้อมูลผิดพลาด"): # Use expander
            st.write("##### ตรวจสอบ Business Logic ก่อนแก้ไข:")
            neg_price = data[data['Unit_Price'] <= 0]
            neg_units = data[data['Units_Sold'] <= 0]
            neg_mkt = data[data['Marketing_Spend'] < 0]
            bad_score = data[(data['Customer_Score'] < 1) | (data['Customer_Score'] > 10)]

            found_noisy = False
            if len(neg_price) > 0:
                st.warning(f"❌ **Unit_Price ≤ 0 :** พบ **{len(neg_price):,} แถว** (ราคาต้องเป็นบวก!)")
                found_noisy = True
            if len(neg_units) > 0:
                st.warning(f"❌ **Units_Sold ≤ 0 :** พบ **{len(neg_units):,} แถว** (จำนวนที่ขายต้องเป็นบวก!)")
                found_noisy = True
            if len(neg_mkt) > 0:
                st.warning(f"❌ **Marketing_Spend < 0 :** พบ **{len(neg_mkt):,} แถว** (งบการตลาดต้องไม่ติดลบ!)")
                found_noisy = True
            if len(bad_score) > 0:
                st.warning(f"❌ **Customer_Score ไม่ใช่ 1-10 :** พบ **{len(bad_score):,} แถว** (คะแนนต้องอยู่ระหว่าง 1-10!)")
                found_noisy = True

            if found_noisy:
                initial_rows = len(data)
                data = data[data['Unit_Price'] > 0]
                data = data[data['Units_Sold'] > 0]
                data = data[data['Marketing_Spend'] >= 0]
                data = data[(data['Customer_Score'] >= 1) & (data['Customer_Score'] <= 10)]
                st.success(f"✅ แก้ไข Noisy Data สำเร็จแล้ว: ลบไป **{initial_rows - len(data):,} แถว**")
            else:
                st.info("ℹ️ ไม่พบ Noisy Data ที่ขัดแย้งกับ Business Logic")
        return data

    def perform_outlier_analysis(data):
        st.subheader("📐 6. การตรวจจับและจัดการ Outlier (Outlier Detection & Treatment)")
        with st.expander("ดูรายละเอียดการตรวจจับและจัดการ Outlier"): # Use expander
            st.markdown("##### ตรวจสอบ Outliers ด้วย Boxplot")

            numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if 'Customer_Score' in numeric_cols:
                numeric_cols.remove('Customer_Score')

            if numeric_cols:
                for col in numeric_cols:
                    fig, ax = plt.subplots(figsize=(8, 2))
                    sns.boxplot(x=data[col], ax=ax)
                    ax.set_title(f'Boxplot ของ {col}')
                    st.pyplot(fig)
                    plt.close(fig)

                st.markdown("""
                **⚠️ หมายเหตุเกี่ยวกับการจัดการ Outliers:**
                ใน Workshop นี้ เราได้สังเกตว่าการใช้ `winsorize` อาจจะทำให้ Business Logic ของข้อมูลเปลี่ยนไป (เช่น `Units_Sold` ที่ถูกปรับค่าอาจไม่สะท้อนยอดขายจริง)
                ดังนั้น ในกรณีนี้ เราจะเลือก **ไม่ปรับ Outliers** ในขั้นตอนนี้ เพื่อรักษาความถูกต้องของข้อมูลตามบริบททางธุรกิจ อย่างไรก็ตาม ในสถานการณ์จริง การจัดการ Outlier ต้องพิจารณาจากบริบทและเป้าหมายการวิเคราะห์อย่างรอบคอบ.
                """)
            else:
                st.info("ℹ️ ไม่พบคอลัมน์ตัวเลขสำหรับวิเคราะห์ Outliers")
        return data

    # --- Sidebar for Cleaning Options ---
    st.sidebar.header("⚙️ เลือกขั้นตอน Data Cleaning")
    do_explore = st.sidebar.checkbox("1. Data Exploration", value=True)
    do_duplicates = st.sidebar.checkbox("2. Handle Duplicate Data", value=True)
    do_inconsistent = st.sidebar.checkbox("3. Handle Inconsistent Data", value=True)
    do_missing = st.sidebar.checkbox("4. Handle Missing Data", value=True)
    do_noisy = st.sidebar.checkbox("5. Handle Noisy Data", value=True)
    do_outlier = st.sidebar.checkbox("6. Outlier Detection", value=True)

    st.markdown("---  ")

    if st.button("🚀 เริ่มทำความสะอาดข้อมูล"): # Styled button
        st.markdown("### กำลังดำเนินการ Data Cleaning...")
        with st.spinner('กำลังวิเคราะห์และทำความสะอาดข้อมูล...'):
            if do_explore:
                df = perform_data_exploration(df)
            if do_duplicates:
                df = handle_duplicate_data(df)
            if do_inconsistent:
                df = handle_inconsistent_data(df)
            if do_missing:
                df = handle_missing_data(df)
            if do_noisy:
                df = handle_noisy_data(df)
            if do_outlier:
                df = perform_outlier_analysis(df)
        
        st.markdown("---  ")
        st.subheader("✅ 7. สรุปผลข้อมูลที่ทำความสะอาดแล้ว (Cleaned Data Summary)")
        st.write(f"#### **ก่อนทำความสะอาด:** {df_raw.shape[0]:,} แถว, {df_raw.shape[1]} คอลัมน์")
        st.write(f"#### **หลังทำความสะอาด:** {df.shape[0]:,} แถว, {df.shape[1]} คอลัมน์")

        st.markdown("### ข้อมูลที่ทำความสะอาดแล้ว (5 แถวแรก)")
        st.dataframe(df.head())

        # --- Download Cleaned Data ---
        csv_buffer = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ ดาวน์โหลดข้อมูลที่ทำความสะอาดแล้วเป็น CSV",
            data=csv_buffer,
            file_name="redbull_clean_beautiful.csv",
            mime="text/csv",
            help="คลิกเพื่อดาวน์โหลดชุดข้อมูลที่ทำความสะอาดเรียบร้อยแล้ว"
        )
else:
    st.info("👆 โปรดอัปโหลดไฟล์ CSV เพื่อเริ่มต้นกระบวนการทำความสะอาดข้อมูล")

st.markdown("---  ")
if st.button("🏠 กลับหน้าหลัก", help="กลับไปยังหน้าหลักของแอปพลิเคชัน"): # Styled button
    st.switch_page("app.py")
