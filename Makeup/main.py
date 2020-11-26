import streamlit as st
from makeup import MakeUp
from PIL import Image
import numpy as np
from vintage import Vintage
IMAGE = []

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
    reset_button = st.sidebar.button('Reset')

    image_to_search = st.file_uploader(
        label='', type=['jpg', 'png', 'jpeg'])
    showfile = st.empty()
    if not image_to_search:
        showfile.info('Please upload image file')
    col1, col2, col3 = st.beta_columns([2, 3, 3])
    
    with col1:
        st.header('Preset')
        PRESET = st.selectbox('', ['#A0511', '#A1506', '#B1812', '#V0504', '#Vintage'])
        if PRESET == '#Vintage':
            grain = st.slider('Grain amount', 0, 100, 40, 1)
        else:
            APPLY = st.button('Apply preset')
        
        if PRESET == '#A0511' and APPLY:
            color = '#aa0511'
            intensity = 60
            color_intensity = 26
            brightness = 5
            contrast = 16
            clarity = -10
        if PRESET == '#A1506' and APPLY:
            color = '#aa1506'
            intensity = 60
            color_intensity = 21
            brightness = 15
            contrast = 15
            clarity = 6
        if PRESET == '#B1812' and APPLY:
            color = '#1b21b8'
            intensity = 45
            color_intensity = 18
            brightness = 12
            contrast = 30
            clarity = 10
        if PRESET == '#V0504' and APPLY:
            color = '#dd0504'
            intensity = 45
            color_intensity = -10
            brightness = 15
            contrast = 19
            clarity = 10

    with col2:
        if image_to_search:
            IMAGE = Image.open(image_to_search)
            IMAGE = IMAGE.convert('RGB')
            IMAGE.save('image/USE_THIS.jpg')
            st.header('Original')
            st.image(IMAGE, use_column_width=True)

    if reset_button:
        color = '#000000'
        intensity = 0
        color_intensity = 0
        brightness = 0
        contrast = 0
        clarity = 0

    with col3:
        if image_to_search:
            Makeup_Object = MakeUp('image/USE_THIS.jpg', color, intensity,
                                brightness, contrast, clarity, color_intensity)
            Result = Makeup_Object.Merge_Makeup()
            if PRESET == '#Vintage':
                Result = Vintage(Result, grain)
            IMG_PLACE = st.empty()
            if int(np.sum(Result)) != 1:
                st.header('Make up')
                IMG_PLACE.image(Result, use_column_width=True)
            else:
                st.header('Make up')
                IMG_PLACE.info('No face detected')


def FaceFilterScreen():
    st.title("Face Filter")
    st.markdown('_**Comming soon**_')


def StickerScreen():
    st.title("Sticker")
    st.markdown('_**Comming soon**_')


def SearchScreen():
    st.title("Search")
    st.markdown('_**Comming soon**_')
    # col1, col2 = st.beta_columns([3, 1])
    # with col1:
    #     image_to_search = st.file_uploader(
    #         label='', type=['jpg', 'png', 'jpeg'], accept_multiple_files=False)
    #     search_button = st.button('Search')
    # with col2:
    #     if search_button and image_to_search:
    #         image = Image.open(image_to_search)
    #         st.image(image, use_column_width=True)

    ################################################################################

    # Image retrival part - List relevant result
    # image_to_search = st.file_uploader(
    #         label='', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    # search_button = st.button('Search')
    # line_dict = {}

    # # col1, col2, col3, col4 = st.beta_columns([1,1,1,1])

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