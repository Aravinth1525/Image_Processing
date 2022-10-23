import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt 
img=cv2.imread('Leaf.tif', 0)
img= img/255
plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title("Original Image"),plt.axis("off")
x, y=img.shape
mean =0
var=0.05  
sigma = np.sqrt(var)
n=np.random.normal(loc=mean, scale=sigma, size=(x,y))
plt.subplot(222),plt.imshow(n,cmap='gray'),plt.title("Gaussian Noise"),plt.axis("off")
g=img+n
plt.subplot(223),plt.imshow(g,cmap='gray'),plt.title("Image with Noise"),plt.axis("off")
# cv2.imshow("Noise Image",g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
kde = gaussian_kde(n.reshape(int(x*y)))  
dist_space=np.linspace(np.min(n), np.max(n), 100) 
plt.plot(dist_space, kde(dist_space))  
plt.xlabel('Noise pixel value')
plt.ylabel('Frequency')
plt.show()


