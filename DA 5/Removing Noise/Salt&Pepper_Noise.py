import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
img = cv2.imread('Salt_n_Pepper.png') 
imag1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
kernel=np.ones((5,5), np.float32)/25
out_img=cv2.filter2D(img, -1, kernel) 
blur=cv2.blur(img, (5,5)) 
blur1=cv2.blur(imag1, (5,5))
gblur=cv2.GaussianBlur(img, (5,5), 0)
median =cv2.medianBlur(img, 5)
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75) 
mean = cv2.cvtColor(blur1, cv2.COLOR_HSV2RGB)
titles = ['Image', '2D Convolution', 'Average Filter', 'Median Filter', 'Bilateral Filter','Mean Filter']
images=[img, out_img, blur, median, bilateralfilter,mean]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap='gray'),plt.axis("off") 
    plt.title(titles[i])
