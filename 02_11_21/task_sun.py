from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage import draw
import pathlib


directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
file = directory / "hmi.Ic_720s.20140215_190000_TAI.1.continuum.fits"

f = fits.open(file)
f.verify("silentfix")

sun_image = f[1].data[1250:2750, 400:3500]


trend = np.average(sun_image[:400], 0)
detrended = sun_image / trend

threshold = 0.9

binary = np.copy(detrended)

binary[binary > threshold] = 0
binary[binary > 0] = 1

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(binary)
plt.subplot(122)
plt.imshow(binary[1000:1200, 1000:1400])
plt.tight_layout()

'''
plt.figure(figsize=(10, 5))
plt.imshow(detrended, cmap="gray")
plt.colorbar()
'''