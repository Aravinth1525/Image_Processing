import matplotlib.pyplot as plt
import cv2
from skimage import filters
camera = cv2.imread('Camera.jpeg',2)
edge_roberts = filters.roberts(camera)
plt.subplot(121),plt.imshow(camera),plt.title("Input Image")
plt.subplot(122),plt.imshow(edge_roberts),plt.title("Roberts")

