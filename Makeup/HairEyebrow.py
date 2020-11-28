import cv2
import os
import numpy as np
from skimage.filters import gaussian
from parsing import evaluate
from PIL import Image

cp = 'dat/79999_iter.pth'

def sharpen(img):
    img = img * 1.0
    gauss_out = gaussian(img, sigma=3, multichannel=True)

    alpha = 1.2
    img_out = (img - gauss_out) * alpha + img

    img_out = img_out / 255.0

    mask_1 = img_out < 0
    mask_2 = img_out > 1

    img_out = img_out * (1 - mask_1)
    img_out = img_out * (1 - mask_2) + mask_2
    img_out = np.clip(img_out, 0, 1)
    img_out = img_out * 255
    return np.array(img_out, dtype=np.uint8)


def hair(image, parsing, part=17, color=[230, 50, 20]):
    b, g, r = color      #[10, 50, 250]       # [10, 250, 10]
    tar_color = np.zeros_like(image)
    tar_color[:, :, 0] = b
    tar_color[:, :, 1] = g
    tar_color[:, :, 2] = r

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    tar_hsv = cv2.cvtColor(tar_color, cv2.COLOR_BGR2HSV)

    image_hsv[:, :, 0:1] = tar_hsv[:, :, 0:1]

    changed = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    if part == 17 or part == 2 or part == 3:
        changed = sharpen(changed)

    changed[parsing != part] = image[parsing != part]
    return changed

def Hair_and_Eyebrow(image_path, COLOR):
    table = {
        'right eye brow': 2,
        'left eye brow': 3,
        'hair': 17
    }
    cv2image = cv2.imread(image_path)

    ori = cv2image.copy()
    parsing = evaluate(image_path, cp)
    parsing = cv2.resize(parsing, cv2image.shape[0:2], interpolation=cv2.INTER_NEAREST)

    parts = [table['right eye brow'], table['left eye brow'], table['hair']]

    colors = COLOR

    for part, color in zip(parts, colors):
        cv2image = hair(cv2image, parsing, part, color)

    # GOLD: colors = [[15, 75, 150], [15, 75, 150], [15, 75, 125]]
    # RED: colors = [[15, 20, 150], [15, 20, 150], [15, 20, 125]]
    # DEEP BLUE: colors = [[150, 25, 15], [150, 25, 15], [150, 25, 15]]
    # PURPLE: colors = [[150, 25, 125], [150, 25, 125], [150, 25, 125]]
    # MINT: colors = [[150, 120, 35], [150, 120, 35], [150, 120, 35]]
    # GREEN: colors = [[35, 175, 64], [35, 175, 64], [35, 175, 64]]
    # OCEAN BLUE: colors = [[210, 100, 10], [210, 100, 10], [210, 100, 10]]
    pil_image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(pil_image)
    return pil_image    
