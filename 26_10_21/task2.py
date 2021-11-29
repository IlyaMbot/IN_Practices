import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pathlib
import time

def shift(s1, s2):
    s1, s2 = np.array(s1, dtype = 'float64'), np.array(s2, dtype = 'float64')
    s1 -= np.mean(s1)
    s2 -= np.mean(s2)
    
    f1 = np.fft.fft(s1)
    f2 = np.ma.conjugate( np.fft.fft(s2) )
    
    corr =  np.abs( np.fft.ifft(f1 * f2))
    c = corr / np.sqrt( (s1 ** 2).sum() * (s2 ** 2).sum() )
    
    shift = c.argmax()
    return(shift )

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons/notafolder")

file = str(directory / "corr_shift.npy")

t1 = time.time()

image = np.load(str(file))

result = [image[0,:]]

for stroke in image[1:]:
    result.append( np.roll(stroke, shift(image[0, :], stroke) ) )

result = np.array(result)

print(time.time() - t1)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(result)