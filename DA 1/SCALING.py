import cv2
from matplotlib import pyplot as plt
image = cv2.imread('VK.jpeg') 
height, width = image.shape[:2]
center = (width/2, height/2)
image1 = cv2.getRotationMatrix2D(center=center, angle=90, scale=0.5)
downscale = cv2.warpAffine(src=image, M=image1, dsize=(width, height))
image2 = cv2.getRotationMatrix2D(center=center, angle=90, scale=2.5)
upscale = cv2.warpAffine(src=image, M=image2, dsize=(width, height))
plt.subplot(121), plt.imshow(downscale), plt.title('DOWNSCALE')
plt.subplot(122), plt.imshow(upscale), plt.title('UPSCALE')