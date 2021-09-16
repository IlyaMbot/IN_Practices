import numpy as np
import matplotlib.pyplot as plt


image = np.ones(shape = (600, 600))
r = 250

x = np.arange(-300, 300).reshape(1,600)
y = np.arange(-300, 300).reshape(600,1)

mask = ((y) ** 2) + ((x) ** 2) < 125 ** 2

image[mask] = 0

fig = plt.figure()
plt.subplot(111)
plt.imshow(image, cmap = 'hot')
plt.show()