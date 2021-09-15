import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y1 = x - (np.arctan(x * np.exp(3)))**2
y2 = x + (np.arctan(x * np.exp(3)))**2

fig = plt.figure()
plt.subplot(111)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
