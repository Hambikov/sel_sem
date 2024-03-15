
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('img.jpg')
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

gray_img = (0.2126 * red + 0.7152 * green + 0.0722 * blue)

plt.imshow(gray_img, cmap=plt.get_cmap("gray"))
plt.axis('off')
plt.savefig('gray.jpg')
plt.show()
