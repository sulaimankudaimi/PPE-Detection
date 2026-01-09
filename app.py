import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="SafeDrill AI Pro", layout="wide")

# --- Sidebar (Your Name on the Side) ---
with st.sidebar:
    st.title("Developer Info")
    st.write("---")
    st.subheader("Eng. Sulaiman")
    st.info("Industrial AI Specialist - SPC")
    st.write("---")
    st.success("YOLOv8 Model Loaded Successfully")

# --- Main Interface (English) ---
st.title("SafeDrill AI Pro: Smart Safety Monitoring System")
st.write("Ensuring a safer environment at the drilling sites.")

# Load Model
model = YOLO("best.pt")

# Options
option = st.radio("Choose Detection Method:", ("Upload Image", "Use Camera"))

if option == "Upload Image":
    img_file = st.file_uploader("Upload site image for AI scanning", type=['jpg', 'png', 'jpeg'])
    if img_file:
        img = Image.open(img_file)
        results = model(img)
        # Draw bounding boxes
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="AI Detection Results", use_column_width=True)
        st.success(f"Detected: {len(results[0].boxes)} safety elements.")

elif option == "Use Camera":
    img_file = st.camera_input("Take a photo for instant inspection")
    if img_file:
        img = Image.open(img_file)
        results = model(img)
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="Real-time Inspection Result")

# --- Footer (Your Name at the Bottom) ---
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p>Developed by: Eng. Sulaiman | SPC Safety Solutions © 2026</p>
    </div>
    """, unsafe_allow_html=True)
