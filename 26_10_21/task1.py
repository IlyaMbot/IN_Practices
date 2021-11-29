import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pathlib

def cros_correlation(s1, s2):
    s1 -= np.mean(s1)
    s2 -= np.mean(s2)
    
    f1 = np.fft.fft(s1)
    f2 = np.ma.conjugate( np.fft.fft(s2) )
    
    corr =  np.abs( np.fft.ifft(f1 * f2))
    c = corr / np.sqrt( (s1 ** 2).sum() * (s2 ** 2).sum() )
    return( c.max() )

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons/notafolder")

file1 = directory / "corr_signal1.npy"
file2 = directory / "corr_signal2.npy"
file3 = str(directory / "corr_shift.npy")

data1 = np.load(str(file1))
data2 = np.load(str(file2))
res = []
for i in range( data1.shape[1] - data2.shape[0]  ): 
    res.append(cros_correlation( data1[1, i : i + data2.shape[0] ] , data2 ))

res = np.array(res)

pos = res.argmax()
amp = res.max()

print(f"position max = { data1[ 0, pos ] }, max = {amp}" )
plt.plot(res)
plt.scatter(pos, amp, color = "red")
plt.show()