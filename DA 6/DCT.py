from scipy.fftpack import dct, idct
import cv2

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')    

from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

im = imread('Image.tif')
imF = dct2(im)
im1 = idct2(imF)

np.allclose(im, im1)

cv2.imshow("DCT",imF)
cv2.waitKey(0)
cv2.imshow("IDCT",im1)

plt.gray()
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Input', size=20)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('Output', size=20)
plt.show()
cv2.imshow("INPUT IMAGE",im)
cv2.imshow("DCT APPLIED IMAGE",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Compressed.png",im1)