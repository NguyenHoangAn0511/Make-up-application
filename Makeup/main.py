import streamlit as st
from streamlit_cropper import st_cropper
from makeup import MakeUp
from PIL import Image
import dlib
import numpy as np
from imutils import face_utils
import imutils
import cv2


def main():
    menu = ['Home', 'Face Make up', 'Face Filter', 'Sticker', 'Search']
    choice = st.sidebar.selectbox('Navigation', menu)

    if choice == 'Home':
        HomeScreen()
    elif choice == 'Face Make up':
        MakeUpScreen()
    elif choice == 'Face Filter':
        FaceFilterScreen()
    elif choice == 'Sticker':
        StickerScreen()
    elif choice == 'Search':
        SearchScreen()


def HomeScreen():
    st.title("Home")

def MakeUpScreen():
    st.title("Face Make up")
    image_to_search = st.file_uploader(
        label='Upload your image', type=['jpg', 'png'])
    showfile = st.empty()
    if not image_to_search:
        showfile.info('Please upload image file')
    col1, col2, col3, col4 = st.beta_columns([3,1,1,3])
    with col1:
        if image_to_search:
            image = Image.open(image_to_search)
            image = image.convert('RGB')
            image.save('USE_THIS.jpg')
            st.header('Original')
            st.image(image, use_column_width=True)
    with col2:
    	#st.header('Magical button')
    	makeup_button = st.button('MakeUp')
    with col3:
    	color = st.color_picker(label='')
    with col4:
        if image_to_search:
            if makeup_button:
                Result = MakeUp('USE_THIS.jpg', color)
                Result = Result.LipAndEyes()
                if int(np.sum(Result)) != 1:
                    #Result = Image.open('result.jpg')
                    st.header('Make up')
                    st.image(Result, use_column_width=True)
                else:
                    st.header('Make up')
                    st.info('No face detected')


def FaceFilterScreen():
    st.title("Face Filter")


def StickerScreen():
    st.title("Sticker")


def SearchScreen():
    st.title("Search")
    col1, col2 = st.beta_columns([3, 1])
    with col1:
        image_to_search = st.file_uploader(
            label='', type=['jpg', 'png'])
        st.button('Search')
        showfile = st.empty()
        if not image_to_search:
            showfile.info('Please upload image file')
        if image_to_search:
            image = Image.open(image_to_search)
            showfile.image(image, use_column_width=True)


if __name__ == '__main__':
    main()
