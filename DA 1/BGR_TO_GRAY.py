import imp
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('Virat.jpeg')
plt.subplot(121), plt.imshow(image), plt.title('BGR IMAGE')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(122), plt.imshow(grayscale), plt.title('GRAYSCALE IMAGE')
