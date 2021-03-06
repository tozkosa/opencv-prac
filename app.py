import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os

# CSS style --->
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
# <--- CSS style

def load_image(img):
    im = Image.open(img)



def main():
    st.title("Aiphotec prototype :sunglasses: :bow:")
    st.text("Build with Streamlit and OpenCV")

    enhance_type = st.sidebar.radio("Enhance Type", ["Original", "Gray-Scale", "Color-Balance", "Contrast", "Brightness", "Blurring"])
    image_file = st.file_uploader("Upload Image",type=['jpg', 'png', 'jpeg'])
    col1, col2 = st.beta_columns(2)

    if image_file is not None:
        with col1:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image, width=300)

        with col2:
            if enhance_type == 'Gray-Scale':
                new_image = np.array(our_image.convert('RGB'))
                img = cv2.cvtColor(new_image, 1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                st.text("Gray-Scale Image")
                st.image(gray, width=300)

            if enhance_type == 'Color-Balance':
                c_balance = st.sidebar.slider("Color-Balance", 0.0,1.0)
                enhancer = ImageEnhance.Color(our_image)
                img_output = enhancer.enhance(c_balance)
                st.text("Color-Balance: " + str(c_balance))
                st.image(img_output, width=300)

            if enhance_type == 'Contrast':
                c_rate = st.sidebar.slider("Contrast", 0.5,3.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.text("Contrast: " + str(c_rate))
                st.image(img_output, width=300)

            if enhance_type == 'Brightness':
                c_rate = st.sidebar.slider("Brightness", 0.5,3.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.text("Brightness: " + str(c_rate))
                st.image(img_output, width=300)

            if enhance_type == "Blurring":
                new_image = np.array(our_image.convert('RGB'))
                blur_rate = st.sidebar.slider("Blurring", 0.5,3.5)
                img = cv2.cvtColor(new_image, 1)
                blur_img = cv2.GaussianBlur(img, (11,11),blur_rate)
                st.text("Blurred Image: " + str(blur_rate))
                st.image(blur_img, width=300)
        # else: 
        #     st.text("Original Image")
        #     st.image(our_image,width=300)


if __name__ == '__main__':
    main()
