# import skimage
# from matplotlib import pyplot as plt
# from skimage import io 
# img=io.imread('BGR.jpeg') 
# print(img.shape)
# plt.imshow(img)

import cv2
from matplotlib import pyplot as plt
originalImage = cv2.imread('BGR.jpeg') 
plt.imshow(originalImage)
print(originalImage.shape)

