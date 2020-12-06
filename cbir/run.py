from orb import *
from google.colab.patches import cv2_imshow
import cv2

ref_path = os.getcwd() + '/referenceImages'
query_path = os.getcwd() + '/queryImages'

#list of file names in reference image folder
ref_images = os.listdir(ref_path)

#creating descriptors for reference images
ref_desc = create_descriptors(ref_images)

query_images = []
#creating list of query image locations
for x in os.listdir(query_path):
    query_images.append(query_path + '/' + x)

print('Querry Image')
query = cv2.imread(query_images[12])
cv2_imshow(query)

for i in range (10):
  image_retrieval(query_images[12], ref_desc=ref_desc, match_num=i)