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
    
    f1 = np.fft.fft(s1)
    f2 = np.ma.conjugate( np.fft.fft(s2) )
    
    corr =  np.abs( np.fft.ifft(f1 * f2))
    c = corr / np.sqrt( (s1 ** 2).sum() * (s2 ** 2).sum() )
    
    shift = c.argmax()
    return(c.max(), shift )



def max_corr(group):
    mc = 0
    result_key = ''
    for key in group:
        c = group[key]
        if c > mc:
            mc = c
            result_key = key
    return(result_key)
        

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons/notafolder")

file = str(directory / "curves.h5")

t1 = time.time()
#-----------------------------------------------------------------------------

f = h5py.File(file, 'r')

combs = list(it.combinations( sorted(list(f)), 2 ))

result = {}

for i, (key1, key2) in enumerate(combs):
    c, _ = corr_shift(f[key1], f[key2])
    if key1 not in result:
        result[key1] = {}
    result[key1][key2] = c

pairs = []

for key in result:
    key2 = max_corr(result[key1])
    pairs.append((key1, key2))
    for group in result.values():
        if key2 in group:
            del group[key2]
        


#-----------------------------------------------------------------------------
print(f'time = {time.time() - t1}')

plt.plot(f[pairs[0][0]])
plt.plot(f[pairs[0][1]])
plt.show()
