import cv2 as cv
import os
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ref_path = os.getcwd() + '/referenceImages'

query_path = os.getcwd() + '/queryImages'


#read image
def read_image(path):
    # read the image without changing its content
    img = cv.imread(path, cv.IMREAD_UNCHANGED)
    # if there is a mask
    if img.shape[2] == 4:
        # copy the mask
        mask = img[:, :, 3].copy()
        # fill the masked region with white
        img[mask == 0, 0:3] = 255
        return img, mask
    return img, None


#iterate through file names and return descriptors for images using ORB
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html
def create_descriptors(images):
    descriptors = []
    path = ''
    detector = cv.ORB.create()
    for image in tqdm(images):
        img, mask = read_image(ref_path+'/'+image)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kp, des = detector.detectAndCompute(gray, mask)
        descriptors.append([image, des])
    return descriptors


#find descriptors for query image
def nearest_neighbor(image, ref_desc, match_num=0):
    #using Hamming distance 
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    x = []
    #find best matches for each reference image
    for i, desc in enumerate(ref_desc):
        name = desc[0]
        descriptors = desc[1]
        #brute force match
        #https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html#
        matches = bf.match(descriptors, image)
        #keep top 10 matches
        matches = sorted(matches, key = lambda x: x.distance)[:10]
        x.append([matches, name])
    avg_distances = [(np.mean([y.distance for y in match[0]]), match[1]) for match in x]
    avg_distances = sorted(avg_distances, key=lambda x: x[0])
    #return image with lowest distance matches to query image
    return avg_distances[match_num][1]


#function to get descriptors for query image and then run nearest neighbors function
def image_retrieval(image_location, ref_desc, match_num=0):
    img=mpimg.imread(image_location)
    #query_image = cv.imread(image_location)
    query_image, mask = read_image(image_location)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    detector = cv.ORB.create()
    kp, query_image_desc = detector.detectAndCompute(gray, mask)
    #index of closest match
    num = match_num
    x = nearest_neighbor(query_image_desc, ref_desc, match_num=num)
    path = os.getcwd() + '/referenceImages/'
    img=mpimg.imread(path+x)
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()

#function to print images including lines between matches
def draw_matches(image1, image2, n_matches=10):
  detector = cv.ORB.create()
  image1 = cv.imread(image1)
  image2 = cv.imread(image2)
  kp1, des1 = detector.detectAndCompute(image1, None)
  kp2, des2 = detector.detectAndCompute(image2, None)
  bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
  matches = bf.match(des1, des2)
  matches = sorted(matches, key = lambda x: x.distance)
  img_matches = cv.drawMatches(image1, kp1, image2, kp2, matches[:n_matches], image2, flags=2) # Show top 10 matches
  plt.figure(figsize=(8, 8))
  plt.title(type(detector))
  plt.imshow(img_matches); plt.show()
