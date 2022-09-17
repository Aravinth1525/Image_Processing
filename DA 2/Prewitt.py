import matplotlib.pyplot as plt
import cv2
from skimage import filters
camera = cv2.imread('Grayscale.tif')
edge_prewitt = filters.prewitt(camera)
plt.subplot(121),plt.imshow(camera),plt.title("Input Image")
plt.subplot(122),plt.imshow(edge_prewitt),plt.title("Prewitt")