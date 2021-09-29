import numpy as np
import matplotlib.pyplot as plt
import pathlib
import struct


directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
file = directory / "signals"

t = []
s1 = []
s2 = []
s3 = []

with file.open('rb') as f:
    bts = b' '
    
    while True:
        bts = f.read(3)
        if(bts == b''):
            break
        
        t.append(struct.unpack(">h", bts[:2]))
        #val = struct.unpack("B", bts[2:])[0]
        s1.append((bts[-1] & 0b00000100) >> 2)
        s2.append((bts[-1] & 0b00010000) >> 4)
        s3.append((bts[-1] & 0b10000000) >> 7)

def diff_freq(s):
    d = np.diff(s)
    t = np.abs(np.argmax(d) - np.argmin(d)) *2
    return(1 / t * 10**3 )
'''
dtype = [("time", ">i2"), ("values", "u1")]
data = np.fromfile(file, dtype)
s1 = (data[values] & mask) >> 2
'''

"""
s1 = 74
s2 = 37
s3 = 24
"""
print(diff_freq(s1))

fig = plt.figure()

plt.subplot(311)
plt.plot(s1)
plt.subplot(312)
plt.plot(s2)
plt.subplot(313)
plt.plot(s3)

plt.show()