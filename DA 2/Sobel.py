import matplotlib.pyplot as plt
import cv2
from skimage import filters
camera = cv2.imread('Camera.jpeg')
edge_sobel = filters.sobel(camera)
plt.subplot(121),plt.imshow(camera),plt.title("Input Image")
plt.subplot(122),plt.imshow(edge_sobel),plt.title("Sobel")

