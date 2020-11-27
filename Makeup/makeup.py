import cv2
from PIL import Image, ImageDraw, ImageEnhance, ImageOps
import numpy as np
# import matplotlib.pyplot as plt
import dlib
from imutils import face_utils
# import imutils
import streamlit as st

hog_face_detector = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1(
    'dat/mmod_human_face_detector.dat')
predictor = dlib.shape_predictor('dat/shape_predictor_68_face_landmarks.dat')


class MakeUp():
    def __init__(
            self, image, color, intensity,
            brightness, contrast, clarity, color_intensity):
        super(MakeUp, self).__init__()
        self.image = image
        # self.image = cv2.imread(self.path)
        # self.Resize()
        self.color = color
        self.intensity = intensity
        self.brightness = brightness
        self.contrast = contrast
        self.clarity = clarity
        self.color_intensity = color_intensity


    @st.cache(suppress_st_warning=False)
    def HEX2RGBA(self, hex, op):
        h = hex.lstrip('#')
        h = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        h = list(h)
        h.append(op)
        return tuple(h)

    @st.cache(suppress_st_warning=False)
    def Brightness(self, image):
        enhancer = ImageEnhance.Brightness(image)
        im_output = enhancer.enhance((self.brightness / 100) + 1)
        # im_output.save('result.jpg')
        return im_output

    @st.cache(suppress_st_warning=False)
    def Contrast(self, image):
        enhancer = ImageEnhance.Contrast(image)
        im_output = enhancer.enhance((self.contrast / 100) + 1)
        # im_output.save('result.jpg')
        return im_output

    @st.cache(suppress_st_warning=False)
    def Clarity(self, image):
        enhancer = ImageEnhance.Sharpness(image)
        im_output = enhancer.enhance(((self.clarity * 5) / 100))# + (0.5 + (self.clarity * 5) / 100))
        # im_output.save('result.jpg')
        return im_output

    @st.cache(suppress_st_warning=False)
    def Color(self, image):
        enhancer = ImageEnhance.Color(image)
        im_output = enhancer.enhance((self.color_intensity / 100) + 1)
        # im_output.save('result.jpg')
        return im_output

    @st.cache(suppress_st_warning=False)
    def Eyes_Lip(self):

        np_image = np.array(self.image)
        cv2_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
        
        gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_RGB2GRAY)

        faces = hog_face_detector(gray_image, 1)

        if len(faces) == 0:
            return self.image

        shape = predictor(gray_image, faces[0])
        shape = face_utils.shape_to_np(shape)

        imageRGB = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

        pil_image = Image.fromarray(imageRGB)
        draw = ImageDraw.Draw(pil_image, 'RGBA')
        shape = shape.tolist()
        for i, j in enumerate(shape):
            shape[i] = (j[0], j[1])

        indices = [48, 49, 50, 51, 52, 53, 54, 64, 63, 62, 61, 60, 48]
        top_lip = [shape[i] for i in indices]
        indices = [48, 60, 67, 66, 65, 64, 54, 55, 56, 57, 58, 59, 48]
        bottom_lip = [shape[i] for i in indices]
        indices = [17, 18, 19, 20, 21]
        right_eyebrow = [shape[i] for i in indices]
        indices = [22, 23, 24, 25, 26]
        left_eyebrow = [shape[i] for i in indices]
        indices = [36, 37, 38, 39]
        left_eye = [shape[i] for i in indices]
        indices = [42, 43, 44, 45]
        right_eye = [shape[i] for i in indices]

        if self.color[0] == '#':
            self.color = self.HEX2RGBA(
                self.color, int((self.intensity / 100) * 150))

        draw.polygon(top_lip, fill=self.color)
        draw.polygon(bottom_lip, fill=self.color)
        # draw.polygon(right_eyebrow, fill=(0, 0, 0, 150))
        # draw.polygon(left_eyebrow, fill=(0, 0, 0, 150))
        draw.line(left_eye, fill=(0, 0, 0, 200), width=3)
        draw.line(right_eye, fill=(0, 0, 0, 200), width=3)

        # out_image = self.Brightness(pil_image)
        # out_image = self.Contrast(out_image)
        # out_image = self.Clarity(out_image)
        # out_image = self.Color(out_image)

        # out_image.save('result.jpg')
        # Out_image = np.array(pil_image)
        # cv2.imwrite('result.jpg', cv2.cvtColor(pil_image, cv2.COLOR_RGB2BGR))
        return pil_image

    def Merge_Makeup(self):
        out_image = self.Eyes_Lip()
        out_image = self.Brightness(out_image)
        out_image = self.Contrast(out_image)
        out_image = self.Clarity(out_image)
        out_image = self.Color(out_image)
        out_image.save('image/final_result.jpg')
        return out_image