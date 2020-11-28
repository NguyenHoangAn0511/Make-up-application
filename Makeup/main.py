import streamlit as st
from makeup import MakeUp
from PIL import Image
import cv2
import numpy as np
import Filter
from Filter import Vintage, Posterize, Resize
from HairEyebrow import Hair_and_Eyebrow

IMAGE = []

def main():
    menu = ['Home', 'Make up', 'Search']
    choice = st.sidebar.selectbox('Navigation', menu)

    if choice == 'Home':
        HomeScreen()
    elif choice == 'Make up':
        MakeUpScreen()
    elif choice == 'Face Filter':
        FaceFilterScreen()
    elif choice == 'Sticker':
        StickerScreen()
    elif choice == 'Search':
        SearchScreen()


def HomeScreen():
    st.title('Make up Application')
    st.header('> MemberS: <')
    st.write('> :crown: **Nguyen Huynh Anh (Leader)**' )
    st.write('>> :computer: **Nguyen Hoang An**')
    st.write('>> :pencil2: **Nguyen Ngoc Binh**')
    st.write('>> :moneybag: **Duong Trong Van**')

def MakeUpScreen():
    st.title("_**Purr-fect me!**_")

    color = st.sidebar.color_picker(label='Lip color')
    intensity = st.sidebar.slider('Make up intensity', 0, 100, 50, 1)
    color_intensity = st.sidebar.slider('Color', -100, 100, 0, 1)
    brightness = st.sidebar.slider('Brightness', -100, 100, 0, 1)
    contrast = st.sidebar.slider('Contrast', -100, 100, 0, 1)
    clarity = st.sidebar.slider('Clarity', -100, 100, 0, 1)
    reset_button = st.sidebar.button('Reset')

    UPLOADED_IMAGE = st.file_uploader(
        label='', type=['jpg', 'png', 'jpeg'])
    showfile = st.empty()
    if not UPLOADED_IMAGE:
        showfile.info('Please upload image file')
    col1, col2, col3 = st.beta_columns([2, 3, 3])
    
    with col1:
        st.header('_**Filter**_ me!')
        PRESET = st.selectbox('', 
        ['#Real-me!', '#1977', '#Toaster',
        '#Aden', '#Rise', '#Earlybird', '#Vintage', '#Posterize',
        '#Gotham', '#Brannan', '#Clarendon', '#Gingham',
        '#Kelvin', '#Lark', '#Lofi',
        '#Maven', '#Nashville',
        '#Reyes', '#Stinson',
        '#Walden', '#Willow', '#Xpro2'])
        
        if PRESET == '#Vintage' or PRESET == '#Posterize':
            if PRESET == '#Vintage':
                grain = st.slider('Grain amount', 0, 100, 40, 1)
            if PRESET == '#Posterize':
                level = st.slider('Level', 1, 3, 2, 1)

        st.header('_**Dye**_ me!')
        HAIR = st.selectbox('', ['#Real-me!', '#GOLD', '#RED', '#DEEP-BLUE', '#PURR-PLE', '#MINT', '#GRIIN', '#OCEAN-BLUE'])

    with col2:
        if UPLOADED_IMAGE:
            IMAGE = Image.open(UPLOADED_IMAGE)
            IMAGE = IMAGE.convert('RGB')
            IMAGE = Resize(IMAGE)
            IMAGE.save('image/USE_THIS.jpg')
            st.header('_**Original**_ me!')
            st.image(IMAGE, use_column_width=True)

    if reset_button:
        color = '#000000'
        intensity = 0
        color_intensity = 0
        brightness = 0
        contrast = 0
        clarity = 0

    path = 'image/USE_THIS.jpg'

    with col3:
        if UPLOADED_IMAGE:
            if HAIR == '#GOLD':
                colors = [[15, 75, 150], [15, 75, 150], [15, 75, 125]]
                IMAGE = Hair_and_Eyebrow(path, colors)
            
            elif HAIR == '#RED':
                colors = [[15, 20, 210], [15, 20, 210], [15, 20, 210]]
                IMAGE = Hair_and_Eyebrow(path, colors)
            
            elif HAIR == '#DEEP-BLUE':
                colors = [[150, 25, 15], [150, 25, 15], [150, 25, 15]]
                IMAGE = Hair_and_Eyebrow(path, colors)
            
            elif HAIR == '#PURR-PLE':
                colors = [[150, 25, 125], [150, 25, 125], [150, 25, 125]]
                IMAGE = Hair_and_Eyebrow(path, colors)
            
            elif HAIR == '#MINT':
                colors = [[150, 120, 35], [150, 120, 35], [150, 120, 35]]
                IMAGE = Hair_and_Eyebrow(path, colors)

            elif HAIR == '#GRIIN':
                colors = [[35, 175, 64], [35, 175, 64], [35, 175, 64]]
                IMAGE = Hair_and_Eyebrow(path, colors)

            elif HAIR == '#OCEAN-BLUE':
                colors = [[210, 100, 10], [210, 100, 10], [210, 100, 10]]
                IMAGE = Hair_and_Eyebrow(path, colors)

            Makeup_Object = MakeUp(IMAGE, color, intensity,
                                brightness, contrast, clarity, color_intensity)
            Result = Makeup_Object.Merge_Makeup()
            IMG_PLACE = st.empty()
            
            if PRESET == '#Vintage':
                Result = Vintage(Result, grain)
            elif PRESET == '#Posterize':
                Result = Posterize(Result, level)
            elif PRESET == '#1977':
                Result = Filter._1977(Result)
            elif PRESET == '#Aden':
                Result = Filter.aden(Result)
            elif PRESET == '#Brannan':
                Result = Filter.Brannan(Result)
            elif PRESET == '#Clarendon':
                Result = Filter.Clarendon(Result)
            elif PRESET == '#Earlybird':
                Result = Filter.Earlybird(Result)
            elif PRESET == '#Gingham':
                Result = Filter.Gingham(Result)
            elif PRESET == '#Kelvin':
                Result = Filter.Kelvin(Result)
            elif PRESET == '#Lark':
                Result = Filter.Lark(Result)
            elif PRESET == '#Lofi':
                Result = Filter.Lofi(Result)
            elif PRESET == '#Maven':
                Result = Filter.Maven(Result)
            elif PRESET == '#Nashville':
                Result = Filter.Nasville(Result)
            elif PRESET == '#Reyes':
                Result = Filter.Reyes(Result)
            elif PRESET == '#Rise':
                Result = Filter.Rise(Result)
            elif PRESET == '#Stinson':
                Result = Filter.Stinson(Result)
            elif PRESET == '#Toaster':
                Result = Filter.Toaster(Result)
            elif PRESET == '#Walden':
                Result = Filter.Walden(Result)
            elif PRESET == '#Willow':
                Result = Filter.Willow(Result)
            elif PRESET == '#Xpro2':
                Result = Filter.Xpro2(Result)
            elif PRESET == '#Gotham':
                Result = Filter.Gotham(Result, 0.75, 0.6, 0.75)
            
            
            if int(np.sum(Result)) != 1:
                st.header('_**Purr-fect**_ me!')
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
    # st.title("Search")
    # st.markdown('_**Comming soon**_')
    # col1, col2 = st.beta_columns([3, 1])
    # with col1:
    #     UPLOADED_IMAGE = st.file_uploader(
    #         label='', type=['jpg', 'png', 'gif'], accept_multiple_files=True)
    #     search_button = st.button('Search')
    # with col2:
    #     if search_button and UPLOADED_IMAGE:
    #         image = Image.open(UPLOADED_IMAGE)
    #         st.image(image, use_column_width=True)

    ################################################################################

    #Image retrival part - List relevant result
    UPLOADED_IMAGE = st.file_uploader(
            label='', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    search_button = st.button('Search')
    line_dict = {}

    # col1, col2, col3, col4 = st.beta_columns([1,1,1,1])

    for i in range(len(UPLOADED_IMAGE)):
        line_dict[i] = st.empty()
    if search_button:
        j = 0
        for i in UPLOADED_IMAGE:
            image = Image.open(i)
            line_dict[j].image(image, use_column_width=True)
            j = j + 1
            print(len(UPLOADED_IMAGE))


if __name__ == '__main__':
    main()