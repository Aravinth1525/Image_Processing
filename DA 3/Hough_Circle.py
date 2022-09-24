import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
img = cv.imread('Coin.jpeg',0)
img = cv.medianBlur(img,5)
# cv.imshow('Input Image', img)
out = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
param1=50,param2=30,minRadius=0,maxRadius=0) 
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv.circle(out,(i[0],i[1]),i[2],(0,255,0),2) 
    cv.circle(out,(i[0],i[1]),2,(0,0,255),3)
# cv.imshow('Output Image', out)
# cv.waitKey(0) 
# cv.destroyAllWindows()

plt.subplot(121),plt.imshow(img),plt.title("Input Image")
plt.subplot(122),plt.imshow(out,cmap='gray'),plt.title("Output Image")