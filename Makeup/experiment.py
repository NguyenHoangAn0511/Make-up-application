import matplotlib.pyplot as plt
from pychubby.detect import LandmarkFace
from pychubby.actions import Chubbify, AbsoluteMove
import cv2

img = plt.imread("image/USE_THIS.jpg")
lf = LandmarkFace.estimate(img)
# lf.plot()
a = AbsoluteMove(y_shifts={30: 20, 29: 20})
new_lfs, df = a.perform(lf)
# cv2.imshow('m', new_lfs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(new_lfs)
new_lfs.plot(show_landmarks=False)