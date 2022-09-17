import matplotlib.pyplot as plt
from skimage import filters
import cv2
image = cv2.imread('Grayscale.tif',2)
edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)
edge_prewitt=filters.prewitt(image)
fig, axes = plt.subplots(ncols=4, sharex=True, sharey=True,figsize=(8, 4))
axes[0].imshow(image, cmap=plt.cm.gray)
axes[0].set_title('Input Image')
axes[1].imshow(edge_roberts, cmap=plt.cm.gray)
axes[1].set_title('Roberts Image')
axes[2].imshow(edge_prewitt, cmap=plt.cm.gray)
axes[2].set_title('Prewitt Edge Detection')
axes[3].imshow(edge_sobel, cmap=plt.cm.gray)
axes[3].set_title('Sobel Edge Detection')
for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()