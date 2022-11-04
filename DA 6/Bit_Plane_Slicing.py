
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Lena.tif', 0)
# cv2.imshow('Input image', img)
# cv2.waitKey(0)

list = []   
for i in range(img.shape[0]):   
    for j in range(img.shape[1]):
        list.append(np.binary_repr(img[i][j], width=8))
        
a = np.array(list)
print(len(a))

print(list[25000])  
        
eight_bit_plane = (np.array([int(i[0]) for i in list], dtype = np.uint8) * 128).reshape(img.shape[0], img.shape[1]) 

seven_bit_plane = (np.array([int(i[1]) for i in list], dtype = np.uint8) * 64).reshape(img.shape[0], img.shape[1]) 
six_bit_plane = (np.array([int(i[2]) for i in list], dtype = np.uint8) * 32).reshape(img.shape[0], img.shape[1]) 
five_bit_plane = (np.array([int(i[3]) for i in list], dtype = np.uint8) * 16).reshape(img.shape[0], img.shape[1]) 
four_bit_plane = (np.array([int(i[4]) for i in list], dtype = np.uint8) * 8).reshape(img.shape[0], img.shape[1])
three_bit_plane = (np.array([int(i[5]) for i in list], dtype = np.uint8) * 4).reshape(img.shape[0], img.shape[1]) 
two_bit_plane = (np.array([int(i[6]) for i in list], dtype = np.uint8) * 2).reshape(img.shape[0], img.shape[1]) 
one_bit_plane = (np.array([int(i[7]) for i in list], dtype = np.uint8) * 1).reshape(img.shape[0], img.shape[1])  
     
plt.subplot(241), plt.imshow(eight_bit_plane), plt.axis('off'), plt.title('Bit plane 7')
plt.subplot(242), plt.imshow(seven_bit_plane), plt.axis('off'), plt.title('Bit plane 6')
plt.subplot(243), plt.imshow(six_bit_plane), plt.axis('off'), plt.title('Bit plane 5')
plt.subplot(244), plt.imshow(five_bit_plane), plt.axis('off'), plt.title('Bit plane 4')
plt.subplot(245), plt.imshow(four_bit_plane), plt.axis('off'), plt.title('Bit plane 3')
plt.subplot(246), plt.imshow(three_bit_plane), plt.axis('off'), plt.title('Bit plane 2')
plt.subplot(247), plt.imshow(two_bit_plane), plt.axis('off'), plt.title('Bit plane 1')
plt.subplot(248), plt.imshow(one_bit_plane), plt.axis('off'), plt.title('Bit plane 0')

new_img = eight_bit_plane + seven_bit_plane + six_bit_plane

plt.subplot(121), plt.imshow(img), plt.axis('off'), plt.title('Input Image')
plt.subplot(122), plt.imshow(new_img), plt.axis('off'), plt.title('Output Image')


# cv2.imshow('Input image', img)
# cv2.waitKey(0)
# cv2.imshow('Bit Plane 8,7,6', new_img)
# cv2.waitKey(0)
 