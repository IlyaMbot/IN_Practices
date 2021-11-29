import matplotlib.pyplot as plt
import numpy as np

def neighbours4(x,y):    
    return( (x, y-1), (x-1, y), (x+1, y), (x, y+1) )

def label(b):
    nb = b
    label = 0
    for y in range(nb.shape[0]):
        for x in range(nb.shape[1]):
            if nb[y,x] == -1:
                label += 1
                search(nb, label, y, x)
    return(nb)


def search(nb, label, y, x):
    nb[y,x] = label
    for ny, nx, in neighbours4(y,x):
        if nb[ny, nx] == -1:
            search(nb, label, ny, nx)
    



#image------------------------------------------------------------------------
image = np.zeros((20, 20), dtype='int32')

image[1:-1, -2] = -1

image[1, 1:5] = -1
image[1, 7:12] = -1
image[2, 1:3] = -1
image[2, 6:8] = -1
image[3:4, 1:7] = -1

image[7:11, 11] = -1
image[7:11, 14] = -1
image[10:15, 10:15] = -1

image[5:10, 5] = -1
image[5:10, 6] = -1

image[13 : 18, 2 : 9] = -1
image[12 : 19 , 3 : 8] = -1

image = np.array(image)
#-------------------------------------------------------------------------

result = label(image)

plt.figure()
plt.imshow(result)
plt.show()
