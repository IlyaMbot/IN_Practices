import numpy as np
import matplotlib.pyplot as plt

st = 25
image = np.zeros(shape = (500, 500))

for i in range(0, 500, st):
    for j in range(0, 500, st):
        image[j : j + st, i : i + st] =  (j + i) /25 


fig = plt.figure()
plt.subplot(111)
plt.imshow(image, cmap = 'hot')
plt.show()