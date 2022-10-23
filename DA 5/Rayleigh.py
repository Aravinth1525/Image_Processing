import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
img = cv2.imread('Leaf.tif', 0)
img = img/25
x, y = img.shape
g = np.zeros((x,y), dtype=np.float32)
plt.subplot(222),plt.imshow(g,cmap='gray'),plt.title("Rayleigh noise"),plt.axis("off")
a = 0.05
b = 1-a
for i in range(x):
    for j in range(y):
        rdn = np.random.random() 
        if rdn >= a:
            g[i][j] = ((2/b)*((rdn-a)*(np.exp(-(rdn-a)**2/b))))
        elif rdn < a:
            g[i][j] = 0
plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title("Input image"),plt.axis("off") 
plt.subplot(223),plt.imshow(g,cmap='gray'),plt.title("Image with Noise "),plt.axis("off")
# cv2.imshow("Rayleigh Noise",g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()