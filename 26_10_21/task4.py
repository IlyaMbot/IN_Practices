import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pathlib
import h5py
import itertools as it
import time

def corr_shift(s1, s2):
    s1, s2 = np.array(s1), np.array(s2)
    s1 -= np.mean(s1)
    s2 -= np.mean(s2)
    
    fft = np.fft.fft
    ifft = np.fft.ifft
    if s1.ndim == 2:
        fft = np.fft.fft2    
        ifft = np.fft.ifft2
    
    f1 = fft(s1)
    f2 = np.ma.conjugate(fft(s2) )
    
    corr =  np.abs(ifft(f1 * f2))
    c = corr / np.sqrt( (s1 ** 2).sum() * (s2 ** 2).sum() )
    
    if s1.ndim == 1:
        xp = c.argmax()
        return(c.max(), xp)
    else:
        yp, xp = np.unravel_index(c.argmax(), c.shape)
        yp -= s1.shape[0]
        xp -= s1.shape[1]
        xp = xp + s1.shape[1] if abs(xp) > s1.shape[1]/ 2 else xp       
        yp = yp + s1.shape[1] if abs(yp) > s1.shape[0]/ 2 else yp       
        return(c.max(), yp,xp )

arr1 = np.zeros((100, 100))
arr1[50, 50] = 1

arr2 = np.zeros((100, 100))
arr2[35, 35] = 1

arr3 = np.zeros((100, 100))
arr3[75, 75] = 1

corr, yp, xp = corr_shift(arr1, arr3)
print(corr, xp, yp)