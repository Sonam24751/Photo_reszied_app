import streamlit as st
from PIL import Image  
import numpy as np
import cv2 
import io

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



st.set_page_config(page_title="Photo Resizer", layout="centered")

st.title("Photo Resizer App")
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image =Image.open(uploaded_image)
    arr_image=np.array(image)
    st.image(arr_image, caption="Original Image",width=100)

    width=st.number_input('enter width',min_value=1,value=arr_image.shape[1])
    height=st.number_input('enter height',min_value=1,value=arr_image.shape[0])

    filp_value= st.selectbox("Direction",["None","Vertical","Horizontal"])
    if filp_value=='Vertical':
        filp_image=cv2.flip(arr_image,0)
        arr_image=filp_image
    elif filp_value=="Horizontal":
        filp_image=cv2.flip(arr_image,1)
        arr_image=filp_image
    st.image(arr_image,caption="filped image",width=100)
    
    if st.button('Resize'):
        resized_image=cv2.resize(arr_image,(int(width),int(height)))
        st.image(resized_image,caption="Resized",width=100)

        buff=io.BytesIO()
        image_pil=Image.fromarray(resized_image)
        image_pil.save(buff,format="jpeg")
        st.download_button("Download here", data=buff.getvalue(), mime='image/jpeg', file_name=("image resize from photo resizer app.jpeg"))
                                
