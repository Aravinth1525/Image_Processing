import cv2 
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
mask = np.array([[-1,-1,-1 ],[-1,8,-1],[-1,-1,-1]])
thrs = 100
image = cv2.imread("jetplane.tif",0).astype('float64')
final = ndimage.convolve(image,mask)
final[final>thrs] = 1
final[final<thrs] = 0
cv2.imwrite("Point_Output.jpg",final)
plt.imshow(final,cmap='gray'),plt.title("Point Detection")