from matplotlib import pyplot as plt
from skimage import io 
import cv2
Colour=io.imread('Colour.jpeg') 
Colour_CV2 = cv2.imread('Colour.jpeg') 
plt.subplot(121), plt.imshow(Colour), plt.title('COLOUR - SCIKIT') 
plt.subplot(122), plt.imshow(Colour_CV2), plt.title('COLOUR - OPENCV')
print(Colour.shape)
print(Colour_CV2.shape)


