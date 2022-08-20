import cv2
from matplotlib import pyplot as plt
steve_image = cv2.imread('BGR.jpeg')
steve_hsv = cv2.cvtColor(steve_image, cv2.COLOR_BGR2HSV)
plt.subplot(121), plt.imshow(steve_image), plt.title('BGR IMAGE')
plt.subplot(122), plt.imshow(steve_hsv), plt.title('HSV IMAGE')
# cv2.imshow('BGR',steve_image)
# cv2.imshow('HSV',steve_hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()