import streamlit as st
from PIL import Image
# from ultralytics import YOLO

st.set_page_config(page_title="🍎 Predict Fruit Quality", layout="centered")
st.title("🧠 AI Fruit Quality Prediction")

st.markdown("Upload a fruit image to see its predicted condition:")
st.markdown("Works locally on Jetson's GPUs")

# # Load YOLO model
# model = YOLO('././best.pt')

# uploaded_file = st.file_uploader("Upload a fruit image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded Image', use_container_width=True)

#     results = model(image)
#     st.image(results[0].plot(), caption="Prediction", use_container_width=True)
