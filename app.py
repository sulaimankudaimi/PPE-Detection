import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="SafeDrill AI Pro", layout="wide")

# --- Sidebar (Your Full Name) ---
with st.sidebar:
    st.title("Developer Information")
    st.write("---")
    st.subheader("Eng. Sulaiman Al-Kudaimi")
    st.info("AI & Computer Vision Developer")
    st.write("---")
    st.success("YOLOv8 Model Active")

# --- Main Interface (English) ---
st.title("SafeDrill AI Pro: Smart Safety Monitoring System")
st.write("Professional Site Inspection & Safety Compliance")

# Load Model
model = YOLO("best.pt")

# Options
option = st.radio("Choose Detection Method:", ("Upload Image", "Use Camera"))

if option == "Upload Image":
    img_file = st.file_uploader("Upload site image for AI scanning", type=['jpg', 'png', 'jpeg'])
    if img_file:
        img = Image.open(img_file)
        results = model(img)
        # Process and draw boxes
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="Detection Analysis Result", use_column_width=True)
        st.success(f"Analysis Complete: {len(results[0].boxes)} elements identified.")

elif option == "Use Camera":
    img_file = st.camera_input("Take a photo for instant inspection")
    if img_file:
        img = Image.open(img_file)
        results = model(img)
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="Camera Stream Inspection")

# --- Footer (Professional Credits) ---
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #888888;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
    }
    </style>
    <div class="footer">
        <p>Developed by Eng. Sulaiman Al-Kudaimi | AI Safety Solutions © 2026</p>
    </div>
    """, unsafe_allow_html=True)
