import cv2
from matplotlib import pyplot as plt
apple_image = cv2.imread("Apple.jpeg")
plt.subplot(121), plt.imshow(apple_image), plt.title('BGR IMAGE')
apple_image_rgb = cv2.cvtColor(apple_image, cv2.COLOR_BGR2RGB)
plt.subplot(122), plt.imshow(apple_image_rgb), plt.title('RGB IMAGE')



