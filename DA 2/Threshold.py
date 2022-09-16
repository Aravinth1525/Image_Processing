import cv2
from skimage import io 
from matplotlib import pyplot as plt
image = cv2.imread('Image.tif',2)
ret, bin_image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret1, bin_image1 = cv2.threshold(image,50,255,cv2.THRESH_BINARY)
ret2, bin_image2 = cv2.threshold(image,100,255,cv2.THRESH_BINARY)
ret3, bin_image3 = cv2.threshold(image,75,200,cv2.THRESH_BINARY)
cv2.imshow('Threshold - 127 & 255',bin_image)
cv2.imshow('Threshold - 50 & 255',bin_image1)
cv2.imshow('Threshold - 100 & 255',bin_image2)
cv2.imshow('Threshold - 75 & 200',bin_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(221),plt.imshow(bin_image),plt.title("Threshold - 127 & 255"),plt.axis('off')
# plt.subplot(222),plt.imshow(bin_image1),plt.title("Threshold - 50 & 255"),plt.axis('off')
# plt.subplot(223),plt.imshow(bin_image2),plt.title("Threshold - 100 & 255"),plt.axis('off')
# plt.subplot(224),plt.imshow(bin_image3),plt.title("Threshold - 75 & 200"),plt.axis('off')