import streamlit as st
from makeup import MakeUp
from PIL import Image
import numpy as np


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

    color = st.sidebar.color_picker(label='Lip color')
    intensity = st.sidebar.slider('Make up intensity', 0, 100, 50, 1)
    color_intensity = st.sidebar.slider('Color', -100, 100, 0, 1)
    brightness = st.sidebar.slider('Brightness', -100, 100, 0, 1)
    contrast = st.sidebar.slider('Contrast', -100, 100, 0, 1)
    clarity = st.sidebar.slider('Clarity', -100, 100, 0, 1)
    reset_button = st.sidebar.button('Auto')

    image_to_search = st.file_uploader(
        label='', type=['jpg', 'png'])
    showfile = st.empty()
    if not image_to_search:
        showfile.info('Please upload image file')
    col1, col2 = st.beta_columns([3, 3])
    with col1:
        if image_to_search:
            image = Image.open(image_to_search)
            image = image.convert('RGB')
            image.save('USE_THIS.jpg')
            st.header('Original')
            st.image(image, use_column_width=True)

    if reset_button:
        color = '#fe1010'
        intensity = 60
        color_intensity = 13
        brightness = 14
        contrast = 17
        clarity = 11

    with col2:
        Makeup_Object = MakeUp('USE_THIS.jpg', color, intensity,
                               brightness, contrast, clarity, color_intensity)
        Result = Makeup_Object.Merge_Makeup()
        IMG_PLACE = st.empty()
        if int(np.sum(Result)) != 1:
            st.header('Make up')
            IMG_PLACE.image(Result, use_column_width=True)
        else:
            st.header('Make up')
            IMG_PLACE.info('No face detected')


def FaceFilterScreen():
    st.title("Face Filter")


def StickerScreen():
    st.title("Sticker")


def SearchScreen():
    st.title("Search")
    col1, col2 = st.beta_columns([3, 1])
    with col1:
        image_to_search = st.file_uploader(
            label='', type=['jpg', 'png'], accept_multiple_files=False)
        search_button = st.button('Search')
    with col2:
        if search_button and image_to_search:
            image = Image.open(image_to_search)
            st.image(image, use_column_width=True)
    # Image retrival part - List relevant result
    # line_dict = {}
    # for i in range(len(image_to_search)):
    #     line_dict[i] = st.empty()
    # if search_button:
    #     j = 0
    #     for i in image_to_search:
    #         image = Image.open(i)
    #         line_dict[j].image(image, use_column_width=True)
    #         j = j + 1
    #         print(len(image_to_search))


if __name__ == '__main__':
    main()
