import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

# 1. إعداد الصفحة
st.set_page_config(page_title="SafeDrill AI - PPE", page_icon="🏗️", layout="wide")

# 2. تصميم CSS للأناقة الاحترافية
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTitle { color: #1e3a8a; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ SafeDrill AI Pro: نظام مراقبة السلامة الذكي")

# 3. تحميل الموديل (تأكد أن best.pt بجانب هذا الملف في GitHub)
@st.cache_resource
def load_model():
    return YOLO("best.pt")

try:
    model = load_model()
    st.sidebar.success("✅ تم تحميل موديل YOLO بنجاح")
except Exception as e:
    st.sidebar.error(f"❌ خطأ في تحميل الموديل: {e}")

# 4. واجهة رفع الصور والتحليل
uploaded_file = st.file_uploader("ارفع صورة الموقع للفحص الذكي", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="الصورة الأصلية", use_container_width=True)
    
    with col2:
        # تنفيذ التنبؤ
        results = model.predict(source=image, conf=0.45)
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="نتائج الفحص الذكي", use_container_width=True)
        
        # عرض عدد المخالفات/العناصر
        count = len(results[0].boxes)
        st.info(f"تم اكتشاف {count} عناصر في الصورة.")
