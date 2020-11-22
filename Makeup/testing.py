from PIL import Image, ImageEnhance

im = Image.open("leonardo.jpg")

enhancer = ImageEnhance.Color(im)

factor = 1
im_s_1 = enhancer.enhance(factor)
im_s_1.save('original-image-1.png');

factor = 0
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred-image.png');

factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened-image.png');