import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt 
img = cv2.imread('Leaf.tif', 0)
img = img/255
plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title("Image"),plt.axis("off")
x, y = img.shape
g = np.zeros((x,y), dtype=np.float32)  
plt.subplot(222),plt.imshow(g,cmap='gray'),plt.title("Salt & Pepper Noise"),plt.axis("off")
pepper = 0.05
salt = 1-pepper
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
plt.subplot(223),plt.imshow(g,cmap='gray'),plt.title("Image with Noise"),plt.axis("off")
# cv2.imshow("Salt & Pepper Noise",g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


