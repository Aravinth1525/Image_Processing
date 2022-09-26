import cv2
from matplotlib import pyplot as plt
image = cv2.imread('Image.tif',2)
ret, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret1, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret2, thresh2 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret3, thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret4, thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
plt.subplot(331),plt.imshow(image,cmap='gray'),plt.title("GrayScale Image"),plt.axis('off')
plt.subplot(332),plt.imshow(thresh,cmap='gray'),plt.title("Threshold - Binary"),plt.axis('off')
plt.subplot(333),plt.imshow(thresh1,cmap='gray'),plt.title("Threshold - Binary Inverse"),plt.axis('off')
plt.subplot(334),plt.imshow(thresh2,cmap='gray'),plt.title("Threshold - Truncate"),plt.axis('off')
plt.subplot(335),plt.imshow(thresh3,cmap='gray'),plt.title("Threshold - To Zero"),plt.axis('off')
plt.subplot(336),plt.imshow(thresh4,cmap='gray'),plt.title("Threshold - To Zero Inverse"),plt.axis('off')
plt.tight_layout()