import matplotlib.pyplot as plt
import cv2
from skimage import filters
camera = cv2.imread('Camera.jpeg')
camera1=cv2.imread('Camera.jpeg',2)
edge_sobel = filters.sobel(camera)
edge_roberts = filters.roberts(camera)
edge_prewitt = filters.prewitt(camera)
plt.subplot(221),plt.imshow(edge_roberts),plt.title("Roberts"),plt.axis('off')
plt.subplot(222),plt.imshow(edge_sobel),plt.title("Sobel"),plt.axis('off')
plt.subplot(223),plt.imshow(edge_prewitt),plt.title("Prewitt"),plt.axis('off')