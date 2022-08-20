from matplotlib import pyplot as plt
from skimage import io 
import cv2
Lion=io.imread('Lion.jpeg') 
Lion_CV2 = cv2.imread('Lion.jpeg') 
plt.subplot(121), plt.imshow(Lion), plt.title('GREY - SCIKIT') 
plt.subplot(122), plt.imshow(Lion_CV2), plt.title('GREY - OPENCV')
print(Lion_CV2.shape)
print(Lion.shape)
