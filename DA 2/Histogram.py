import cv2
from skimage import io 
from matplotlib import pyplot as plt
img = cv2.imread('Virat.jpeg')
col=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bin_img = cv2.imread('Leaf.tif',2)
plt.subplot(121),plt.imshow(col),plt.title("Colour Image")
plt.subplot(122),plt.imshow(bin_img,cmap='gray'),plt.title("Binary Image")
hist1 = cv2.calcHist([col],[0],None,[10],[0,256])
hist2 = cv2.calcHist([bin_img],[0],None,[10],[0,256])
plt.subplot(121),plt.imshow(hist1),plt.title("Histogram - Colour Image")
plt.subplot(122),plt.imshow(hist2),plt.title("Histogram - Binary Image")








