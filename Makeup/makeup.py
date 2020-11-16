import cv2
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils
import imutils
import pylab


class MakeUp(object):
    def __init__(self, path):
        super(MakeUp, self).__init__()
        self.path = path
        self.image = cv2.imread(self.path)

    def ReadAndShowImg(self, path):
        cv2.imshow("x", path)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def LipAndEyes(self):
        resized_image = imutils.resize(self.image, width=500)
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
        # self.ReadAndShowImg(resized_image)
        hog_face_detector = dlib.get_frontal_face_detector()
        cnn_face_detector = dlib.cnn_face_detection_model_v1(
            'mmod_human_face_detector.dat')
        predictor = dlib.shape_predictor(
            'shape_predictor_68_face_landmarks.dat')
        faces = hog_face_detector(gray_image, 1)
        shape = predictor(gray_image, faces[0])
        shape = face_utils.shape_to_np(shape)
        pil_image = Image.fromarray(resized_image)
        draw = ImageDraw.Draw(pil_image, 'RGBA')
        shape = shape.tolist()
        for i, j in enumerate(shape):
            shape[i] = (j[0], j[1])
        indices = [48, 49, 50, 51, 52, 53, 54, 64, 63, 62, 61, 60, 48]
        top_lip = [shape[i] for i in indices]
        indices = [48, 60, 67, 66, 65, 64, 54, 55, 56, 57, 58, 59, 48]
        bottom_lip = [shape[i] for i in indices]
        indices = [36, 37, 38, 39, 40, 41, 36]
        left_eye = [shape[i] for i in indices]
        indices = [42, 43, 44, 45, 46, 47, 42]
        right_eye = [shape[i] for i in indices]

        draw.polygon(top_lip, fill=(128, 0, 120, 90))
        draw.polygon(bottom_lip, fill=(128, 0, 120, 90))
        draw.line(left_eye, fill=(0, 0, 0, 255), width=3)
        draw.line(right_eye, fill=(0, 0, 0, 255), width=3)
        pil_image = np.array(pil_image)
        # self.ReadAndShowImg(pil_image)
        cv2.imshow('MK', pil_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


p = MakeUp('smile.png')
p.LipAndEyes()
