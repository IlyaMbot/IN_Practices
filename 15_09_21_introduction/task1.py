import numpy as np
import matplotlib.pyplot as plt

def func_i(x, i = 1):
    return(x ** i)

x = np.arange(-10, 10.2, 0.2)
pwr = np.arange(1, 6)

fig = plt.figure()
plt.subplot(111)
plt.yscale('symlog')

for i in pwr:    
    plt.plot(x, func_i(x, i))

plt.show()