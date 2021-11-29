import matplotlib.pyplot as plt
import numpy as np

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

def parkour(image):
    k = 1

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j] == -1):
                if(image[i - 1, j] != 0):
                    image[i, j] = image[i - 1, j]
                elif( image[i , j - 1] != 0):
                    image[i, j] = image[i , j - 1]
                else:
                    image[i, j] = k
                    k += 1
    return(image)
                
image = parkour(image)

plt.figure()
plt.imshow(image)
