import cv2 
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
mask_h = np.array([[-1,-1,-1 ],[2,2,2],[-1,-1,1]])
mask_45 = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
mask_v = np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
mask_n45 = np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
image = cv2.imread("Line.tif",0).astype('float64')
image/=255.0
horizontal = ndimage.convolve( image, mask_h )
horizontal*=255
plt.subplot(221),plt.imshow(horizontal,cmap='gray'),plt.title("Horizontal"),plt.axis('off') 
Degree45= ndimage.convolve( image, mask_45 )
Degree45*=255
plt.subplot(222),plt.imshow(Degree45,cmap='gray'),plt.title("45 Degree"),plt.axis('off') 
vertical = ndimage.convolve( image, mask_v )
vertical*=255
plt.subplot(223),plt.imshow(vertical,cmap='gray'),plt.title("Vertical"),plt.axis('off') 
Neg_Degree45 = ndimage.convolve( image, mask_n45)
Neg_Degree45*=255
plt.subplot(224),plt.imshow(Neg_Degree45,cmap='gray'),plt.title("Negative 45 Degree"),plt.axis('off') 
plt.tight_layout()
