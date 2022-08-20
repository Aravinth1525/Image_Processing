from matplotlib import pyplot as plt
from skimage import io
img = io.imread('Virat.jpg', as_gray=True)
plt.imshow(img)