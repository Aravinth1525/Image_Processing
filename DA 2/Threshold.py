import cv2
from skimage import io 
from matplotlib import pyplot as plt
image = cv2.imread('Image.tif',2)
ret, bin_image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret1, bin_image1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret2, bin_image2 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret3, bin_image3 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret4, bin_image4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
# cv2.imshow('Threshold - Binary',bin_image)
# cv2.imshow('Threshold - Binary Inverse',bin_image1)
# cv2.imshow('Threshold - Truncate',bin_image2)
# cv2.imshow('Threshold - To Zero',bin_image3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.subplot(331),plt.imshow(image,cmap='gray'),plt.title("GrayScale Image"),plt.axis('off')
plt.subplot(332),plt.imshow(bin_image,cmap='gray'),plt.title("Threshold - Binary"),plt.axis('off')
plt.subplot(333),plt.imshow(bin_image1,cmap='gray'),plt.title("Threshold - Binary Inverse"),plt.axis('off')
plt.subplot(334),plt.imshow(bin_image2,cmap='gray'),plt.title("Threshold - Truncate"),plt.axis('off')
plt.subplot(335),plt.imshow(bin_image3,cmap='gray'),plt.title("Threshold - To Zero"),plt.axis('off')
plt.subplot(336),plt.imshow(bin_image4,cmap='gray'),plt.title("Threshold - To Zero Inverse"),plt.axis('off')
plt.tight_layout()