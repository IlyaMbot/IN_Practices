import numpy as np
import matplotlib.pyplot as plt

st = 25

image = np.kron([[1,0] * 10, [0,1] * 10] * 10, np.ones((25, 25)))

image = np.kron( np.arange(400).reshape(20, 20) , np.ones((25, 25)))

image = np.kron( np.ones((25, 25)), np.arange(400).reshape(20, 20) )


fig = plt.figure()
plt.subplot(111)
plt.imshow(image, cmap = 'hot')
plt.show()