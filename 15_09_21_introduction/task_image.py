import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face 

def desc(arr, nvals = 3):
    arr = arr.copy()
    mn = arr.min()
    mx = arr.max()
    lvls = np.linspace(mn, mx, nvals, endpoint = True)
    for i in range(len(lvls) - 1):
        lvl = lvls[i], lvls[i + 1]
        avg = np.average(lvl)
        #pos = np.where(np.logical_and(arr >= lvl[0], arr < lvl[1]))
        arr[np.logical_and(arr >= lvl[0], arr <= avg)] = lvl[0]
        arr[np.logical_and(arr < lvl[1], arr >= avg)] = lvl[1]
    return(arr)
        
image = face(gray = True)

result = desc(image)

fig = plt.figure()
plt.subplot(121)
plt.imshow(result, cmap = 'Greys_r')
plt.subplot(122)
plt.imshow(image, cmap = 'Greys_r')

plt.show()
