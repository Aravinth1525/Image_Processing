import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("Line.tif")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)
plt.subplot(121),plt.imshow(img),plt.title("Input Image"),plt.axis("off")
plt.subplot(122),plt.imshow(edges,cmap="gray"),plt.title("Line Detection"),plt.axis("off")