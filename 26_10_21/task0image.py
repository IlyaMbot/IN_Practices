import numpy as np
import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pathlib

#------------------------------------------------------------------------------

def int_finder(image_input, roof):
    image = np.sum( image_input, axis = 2 )/3
    
    position = np.argwhere(image >= roof)
    return(position)

#------------------------------------------------------------------------------


directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")

file = directory / "W40_CAM.bmp"

#(117)


#image = mpimg.imread(file)

img = cv.imread(str(file))

#positions  = int_finder(image, 164)

_, threshold = cv.threshold(img, 164, 255, cv.THRESH_BINARY)

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(threshold)


""" z index"""

'''
*****
***0*
*000*
*0*0*
*****
'''