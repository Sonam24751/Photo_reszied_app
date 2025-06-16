import streamlit as st
from PIL import Image  
import numpy as np
import cv2 
import io

# Hide Streamlit Cloud elements
hide_streamlit_cloud_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    a[title="View source"] {display: none !important;}
    button[kind="icon"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_cloud_elements, unsafe_allow_html=True)

# Set page title and layout
st.set_page_config(page_title="Photo Resizer", layout="centered")

# App Title
st.title("📷 Photo Resizer App")

# Image Upload
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    arr_image = np.array(image)
    st.image(arr_image, caption="🖼️ Original Image", width=100)

    # Input for new dimensions
    width = st.number_input('Enter Width', min_value=1, value=arr_image.shape[1])
    height = st.number_input('Enter Height', min_value=1, value=arr_image.shape[0])

    # Flip options
    flip_value = st.selectbox("Flip Direction", ["None", "Vertical", "Horizontal"])
    if flip_value == 'Vertical':
        arr_image = cv2.flip(arr_image, 0)
    elif flip_value == "Horizontal":
        arr_image = cv2.flip(arr_image, 1)
    st.image(arr_image, caption="🔄 Flipped Image", width=100)

    # Resize and Download Button
    if st.button('Resize'):
        resized_image = cv2.resize(arr_image, (int(width), int(height)))
        st.image(resized_image, caption="✅ Resized Image", width=100)

        buff = io.BytesIO()
        image_pil = Image.fromarray(resized_image)
        image_pil.save(buff, format="JPEG")
        st.download_button(
            "📥 Download Resized Image",
            data=buff.getvalue(),
            mime='image/jpeg',
            file_name="image_resize_from_photo_resizer_app.jpeg"
        )
