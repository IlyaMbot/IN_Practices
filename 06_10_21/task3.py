import numpy as np
import matplotlib.pyplot as plt
import pathlib
from astropy.io import fits

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")

mag = directory / "magnetogram.fits"

f = fits.open(mag)
f.verify('silentfix')

'''
for key in f[0].header:
    print(f"{key} - {f[0].header[key]}")

for key in f[1].header:
    print(f"{key} - {f[1].header[key]}")
'''

mag = f[1].data[1900:2300, 1500:1900]
print(mag.shape, mag.dtype)

imax = np.unravel_index(np.argmax(mag), shape = mag.shape)
imin = np.unravel_index(np.argmin(mag), shape = mag.shape)

print(f"Absolute magnet flux {np.abs(mag).mean()}")

bpos = mag[mag > 0].mean()
bneg = mag[mag < 0].mean()

print(bpos, bneg)

v = mag[:,imax[1]]
h = mag[ imax[0], :]

plt.subplot(211)
plt.title('v')
plt.plot(v)
plt.subplot(212)
plt.title('h')
plt.plot(h)
plt.tight_layout()
'''
plt.imshow(mag, cmap = 'hot')
plt.scatter(imax[1], imax[0], color = 'r')
plt.scatter(imin[1], imin[0], color = 'b')
plt.colorbar()
plt.clim(-400, 400)
'''
plt.show()

f.close
