import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os

def load_image(img):
    im = Image.open(img)


def main():
    st.title("Aiphotec prototype")
    st.text("Build with Streamlit and OpenCV")

    enhance_type = st.sidebar.radio("Enhance Type", ["Original", "Gray-Scale", "Contrast", "Brightness", "Blurring"])
    image_file = st.file_uploader("Upload Image",type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)

        if enhance_type == 'Gray-Scale':
            new_image = np.array(our_image.convert('RGB'))
            img = cv2.cvtColor(new_image, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            st.text("Gray-Scale Image")
            st.image(gray)

        if enhance_type == 'Contrast':
            c_rate = st.sidebar.slider("Contrast", 0.5,3.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)

        if enhance_type == 'Brightness':
            c_rate = st.sidebar.slider("Brightness", 0.5,3.5)
            enhancer = ImageEnhance.Brightness(our_image)
            img_output = enhancer.enhance(c_rate)
            st.image(img_output)

        if enhance_type == "Blurring":
            new_image = np.array(our_image.convert('RGB'))
            blur_rate = st.sidebar.slider("Blurring", 0.5,3.5)
            img = cv2.cvtColor(new_image, 1)
            blur_img = cv2.GaussianBlur(img, (11,11),blur_rate)
            st.text("Blurred Image")
            st.image(blur_img)
        else: st.image(our_image,width=300)


if __name__ == '__main__':
    main()
