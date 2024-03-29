import random
from PIL import Image, ImageOps, ImageEnhance
import pilgram
from skimage import filters
import numpy as np
import skimage


VINTAGE_COLOR_LEVELS = {
    'r': [0, 0, 0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 47, 48, 49, 52, 54, 55, 57, 59, 60, 62, 65, 67, 69, 70, 72, 74, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 99, 101, 103, 107, 109, 111, 112, 116, 118, 120, 124, 126, 127, 129, 133, 135, 136, 140, 142, 143, 145, 149, 150, 152, 155, 157, 159, 162, 163, 165, 167, 170, 171, 173, 176, 177, 178, 180, 183, 184, 185, 188, 189, 190, 192, 194, 195, 196, 198, 200, 201, 202, 203, 204, 206, 207, 208, 209, 211, 212, 213, 214, 215, 216, 218, 219, 219, 220, 221, 222, 223, 224, 225, 226, 227, 227, 228, 229, 229, 230, 231, 232, 232, 233, 234, 234, 235, 236, 236, 237, 238, 238, 239, 239, 240, 241, 241, 242, 242, 243, 244, 244, 245, 245, 245, 246, 247, 247, 248, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    'g' : [0, 0, 1, 2, 2, 3, 5, 5, 6, 7, 8, 8, 10, 11, 11, 12, 13, 15, 15, 16, 17, 18, 18, 19, 21, 22, 22, 23, 24, 26, 26, 27, 28, 29, 31, 31, 32, 33, 34, 35, 35, 37, 38, 39, 40, 41, 43, 44, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 88, 89, 90, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 105, 106, 107, 108, 109, 111, 113, 114, 115, 117, 118, 119, 120, 122, 123, 124, 126, 127, 128, 129, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 144, 145, 146, 148, 149, 150, 151, 153, 154, 155, 157, 158, 159, 160, 162, 163, 164, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 181, 182, 183, 184, 186, 186, 187, 188, 189, 190, 192, 193, 194, 195, 195, 196, 197, 199, 200, 201, 202, 202, 203, 204, 205, 206, 207, 208, 208, 209, 210, 211, 212, 213, 214, 214, 215, 216, 217, 218, 219, 219, 220, 221, 222, 223, 223, 224, 225, 226, 226, 227, 228, 228, 229, 230, 231, 232, 232, 232, 233, 234, 235, 235, 236, 236, 237, 238, 238, 239, 239, 240, 240, 241, 242, 242, 242, 243, 244, 245, 245, 246, 246, 247, 247, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 255],
    'b' : [53, 53, 53, 54, 54, 54, 55, 55, 55, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 60, 61, 61, 61, 62, 62, 63, 63, 63, 64, 65, 65, 65, 66, 66, 67, 67, 67, 68, 69, 69, 69, 70, 70, 71, 71, 72, 73, 73, 73, 74, 74, 75, 75, 76, 77, 77, 78, 78, 79, 79, 80, 81, 81, 82, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 89, 89, 90, 90, 91, 91, 93, 93, 94, 94, 95, 95, 96, 97, 98, 98, 99, 99, 100, 101, 102, 102, 103, 104, 105, 105, 106, 106, 107, 108, 109, 109, 110, 111, 111, 112, 113, 114, 114, 115, 116, 117, 117, 118, 119, 119, 121, 121, 122, 122, 123, 124, 125, 126, 126, 127, 128, 129, 129, 130, 131, 132, 132, 133, 134, 134, 135, 136, 137, 137, 138, 139, 140, 140, 141, 142, 142, 143, 144, 145, 145, 146, 146, 148, 148, 149, 149, 150, 151, 152, 152, 153, 153, 154, 155, 156, 156, 157, 157, 158, 159, 160, 160, 161, 161, 162, 162, 163, 164, 164, 165, 165, 166, 166, 167, 168, 168, 169, 169, 170, 170, 171, 172, 172, 173, 173, 174, 174, 175, 176, 176, 177, 177, 177, 178, 178, 179, 180, 180, 181, 181, 181, 182, 182, 183, 184, 184, 184, 185, 185, 186, 186, 186, 187, 188, 188, 188, 189, 189, 189, 190, 190, 191, 191, 192, 192, 193, 193, 193, 194, 194, 194, 195, 196, 196, 196, 197, 197, 197, 198, 199]
    }


def _1977(image):
    return pilgram._1977(image)


def aden(image):
    return pilgram.aden(image)


def Brannan(image):
    return pilgram.brannan(image)


def Clarendon(image):
    return pilgram.clarendon(image)


def Earlybird(image):
    return pilgram.earlybird(image)


def Gingham(image):
    return pilgram.gingham(image)


def Kelvin(image):
    return pilgram.kelvin(image)


def Lark(image):
    return pilgram.lark(image)


def Lofi(image):
    return pilgram.lofi(image)


def Maven(image):
    return pilgram.maven(image)


def Nasville(image):
    return pilgram.nashville(image)


def Reyes(image):
    return pilgram.reyes(image)


def Rise(image):
    return pilgram.rise(image)


def Stinson(image):
    return pilgram.stinson(image)


def Toaster(image):
    return pilgram.toaster(image)


def Walden(image):
    return pilgram.walden(image)


def Willow(image):
    return pilgram.willow(image)


def Xpro2(image):
    return pilgram.xpro2(image)


def Posterize(image, level):
    image = ImageOps.posterize(image, level)
    enhancer = ImageEnhance.Brightness(image)
    if level == 2:
        image = enhancer.enhance(1.4)
    if level == 1:
        image = enhancer.enhance(2)
    if level == 3:
        image = enhancer.enhance(1.4)
    image.save('image/Posterize.jpg')
    return image


def Vintage(image, noise):
  if image.mode != 'RBG':
    image = image.convert('RGB')
  vintage_colors(image)
  add_noise(image, noise)
  image.save('image/Vintage.jpg')
  return image


def Gotham(image, r_boost, g_boost, b_boost):
    original_image = skimage.img_as_float(image)
    r = original_image[:, :, 0]
    g = original_image[:, :, 1]
    b = original_image[:, :, 2]
    k = np.array([0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0])
    r_boost_lower = channel_adjust(r, (r_boost * k).tolist())
    g_boost_lower = channel_adjust(g, (g_boost * k).tolist())
    b_boost_lower = channel_adjust(b, (b_boost * k).tolist())
    merged = np.stack([r_boost_lower, g_boost_lower, b_boost_lower], axis=2)
    blurred = filters.gaussian(merged, sigma=10, multichannel=True)
    image = np.clip(merged * 1.3 - blurred * 0.3, 0, 1.0)
    return image


def Resize(image):
        desired_size = 1024
        old_size = image.size  # old_size[0] is in (width, height) format

        ratio = float(desired_size)/max(old_size)
        new_size = tuple([int(x*ratio) for x in old_size])
        # use thumbnail() or resize() method to resize the input image

        # thumbnail is a in-place operation

        # im.thumbnail(new_size, Image.ANTIALIAS)

        image = image.resize(new_size, Image.ANTIALIAS)
        # create a new image and paste the resized on it

        pad_image = Image.new("RGB", (desired_size, desired_size), '#ffffff')
        pad_image.paste(image, ((desired_size-new_size[0])//2,
                            (desired_size-new_size[1])//2))
        return pad_image



def channel_adjust(channel, values):
    orig_size = channel.shape
    flat_channel = channel.flatten()
    adjusted = np.interp(flat_channel, np.linspace(0, 1, len(values)), values)
    return adjusted.reshape(orig_size)


def modify_all_pixels(im, pixel_callback):
    width, height = im.size
    pxls = im.load()
    for x in range(width):
        for y in range(height):
            pxls[x,y] = pixel_callback(x, y, *pxls[x, y])


def vintage_colors(im, color_map=VINTAGE_COLOR_LEVELS):
    r_map = color_map['r']
    g_map = color_map['g']
    b_map = color_map['b']
    def adjust_levels(x, y, r, g, b):  # expect rgb; rgba will blow up
        return r_map[r], g_map[g], b_map[b]
    modify_all_pixels(im, adjust_levels)
    return im

def add_noise(im, noise_level=40):
    def pixel_noise(x, y, r, g, b):  # expect rgb; rgba will blow up
        noise = random.randint(0, noise_level) - noise_level / 2
        return max(0, int(min(r + noise, 255))), max(0, int(min(g + noise, 255))), max(0, int(min(b + noise, 255)))
    modify_all_pixels(im, pixel_noise)
    return im



#image là 1 link ảnh
# def Vintage(image_link):
#   image = Image.open(image_link)
#   if image.mode != 'RGB':
#       image = image.convert('RGB')
#   vintage_colors(image)
#   add_noise(image)
#   return image
