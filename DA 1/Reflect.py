
import cv2
import matplotlib.pyplot as plt
input = cv2.imread('BGR.jpeg')
plt.subplot(121), plt.imshow(input), plt.title('Original')
# FlipV=cv2.flip(input, 0)
# FlipH=cv2.flip(input,1)
Flip_Both=cv2.flip(input,-1)
# plt.subplot(222), plt.imshow(FlipV), plt.title('Flipped Vertically')
# plt.subplot(223), plt.imshow(FlipH), plt.title('Flipped Horizontally')
plt.subplot(122), plt.imshow(Flip_Both), plt.title('Both')
# -1 To flip at both vertical and horizontal axis