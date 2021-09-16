import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face 


def desc(arr, xbloks = 1000, ybloks = 12 ):
    
    if xbloks == 0 or ybloks == 0:
        return(arr)
        
    arr = arr.copy()
    xsize = int(arr.shape[1] / xbloks) 
    ysize = int(arr.shape[0] / ybloks)
    
    for i in range(0, arr.shape[1], xsize):
        for j in range(0, arr.shape[0], ysize):
            avg = np.average(arr[j : j + ysize , i : i + xsize])
            arr[j : j + ysize , i : i + xsize] = avg
    
    return(arr)
        
image = face(gray = True)

result = desc(image)

fig = plt.figure()
plt.subplot(121)
plt.imshow(result, cmap = 'Greys_r')
plt.subplot(122)
plt.imshow(image, cmap = 'Greys_r')

plt.show()
