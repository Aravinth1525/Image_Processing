from matplotlib import pyplot as plt
import cv2
Binary=cv2.imread('Binary.png')
Lion=cv2.imread('Lion.jpeg')
Colour=cv2.imread('Colour.jpeg')
plt.title('SUBPLOT')
plt.subplot(231), plt.imshow(Binary)
plt.subplot(232), plt.imshow(Lion)
plt.subplot(233), plt.imshow(Colour) 