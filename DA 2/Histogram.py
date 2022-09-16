import cv2
from skimage import io 
from matplotlib import pyplot as plt
img = cv2.imread('Image.jpeg',2)
ret, bin_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(bin_img)
hist1 = cv2.calcHist([img],[0],None,[10],[0,256])
hist2 = cv2.calcHist([bin_img],[0],None,[10],[0,256])
plt.subplot(121),plt.imshow(hist1),plt.title("Histogram - Colour Image")
plt.subplot(122),plt.imshow(hist2),plt.title("Histogram - Binary Image")








