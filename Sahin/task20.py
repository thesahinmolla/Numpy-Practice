#Using Flipud
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mp_img

image_a = mp_img.imread('Sahin/Others/image.jpg')

image_b = np.flipud(image_a)
plt.imshow(image_b)

plt.savefig("Sahin/Others/image.jpg", dpi=200)
plt.show()