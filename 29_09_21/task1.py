import numpy as np
import matplotlib.pyplot as plt
import pathlib
import struct

directory = pathlib.Path("./lessons")
file = directory / "twinned.dat"

def intensity_searcher(image):
    pixel_position = np.argwhere(image  == image.max())
    pixel_position = pixel_position[0]
    return(pixel_position)

coords = []


with file.open('rb') as f:

    size = struct.unpack("I", f.read(4))[0]
    

    while True:
        bts = f.read(10)
        if(bts == b''):
            break
        
        coords.append(struct.unpack('IIH', bts[:10]))

coords = np.array(coords)

image = np.zeros(shape = (size, size), dtype = 'uint8')

image[coords[:,0], coords[:,1]] = coords[:,2]

maxs = intensity_searcher(image)

'''
image = np.ones(shape = (size, size))
r = 

x = np.arange(-300, 300).reshape(1,600)
y = np.arange(-300, 300).reshape(600,1)

mask = ((y - maxis[1]) ** 2) + ((x -maxis[2]) ** 2) < 125 ** 2

image[mask] = 0
'''


#find distance between centres

plt.imshow(image, cmap = 'hot')
plt.plot(maxs[1], maxs[0], 'o',ms = 10)
plt.show()

