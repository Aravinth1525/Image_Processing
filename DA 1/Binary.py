import cv2
from matplotlib import pyplot as plt
from skimage import io 

img=io.imread('Binary.png') 
print(img.shape)
plt.subplot(121), plt.imshow(img), plt.title('BINARY - SCIKIT')
input = cv2.imread('Binary.png') 
plt.subplot(122), plt.imshow(input), plt.title('BINARY - OPENCV')
print(input.shape)

