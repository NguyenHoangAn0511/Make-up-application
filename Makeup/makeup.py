import cv2
from PIL import Image, ImageDraw, ImageColor
import numpy as np
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils
import imutils
import streamlit as st

hog_face_detector = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1(
    'mmod_human_face_detector.dat')
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


class MakeUp():
    def __init__(self, path, color):
        super(MakeUp, self).__init__()
        self.path = path
        self.image = cv2.imread(self.path)
        self.color = color

    def HEX2RGBA(self, hex, op):
        h = hex.lstrip('#')
        h = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        h = list(h)
        h.append(op)
        return tuple(h)
    @st.cache
    def LipAndEyes(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        # self.ReadAndShowImg(resized_image)
        faces = hog_face_detector(gray_image, 1)
        if len(faces) == 0:
            return 1
        shape = predictor(gray_image, faces[0])
        shape = face_utils.shape_to_np(shape)

        imageRGB = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        pil_image = Image.fromarray(imageRGB)
        draw = ImageDraw.Draw(pil_image, 'RGBA')
        shape = shape.tolist()
        for i, j in enumerate(shape):
            shape[i] = (j[0], j[1])
        indices = [48, 49, 50, 51, 52, 53, 54, 64, 63, 62, 61, 60, 48]
        top_lip = [shape[i] for i in indices]
        indices = [48, 60, 67, 66, 65, 64, 54, 55, 56, 57, 58, 59, 48]
        bottom_lip = [shape[i] for i in indices]
        indices = [36, 37, 38, 39]
        left_eye = [shape[i] for i in indices]
        indices = [42, 43, 44, 45]
        right_eye = [shape[i] for i in indices]
        #self.color = ImageColor.getrgb(self.color)
        if self.color[0] == '#':
            self.color = self.HEX2RGBA(self.color, 95)
        draw.polygon(top_lip, fill=self.color)
        draw.polygon(bottom_lip, fill=self.color)
        print(self.color)
        draw.line(left_eye, fill=(0, 0, 0, 255), width=3)
        draw.line(right_eye, fill=(0, 0, 0, 255), width=3)
        pil_image = np.array(pil_image)
        # self.ReadAndShowImg(pil_image)
        cv2.imwrite('result.jpg', cv2.cvtColor(pil_image, cv2.COLOR_RGB2BGR))
        return pil_image
