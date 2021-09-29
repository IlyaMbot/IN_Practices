import numpy as np
import matplotlib.pyplot as plt
import pathlib

def unbias(s):
    return(s - s.mean())

def local_max(arr):
    res = []
    for i in range(1, len(arr)-1):
        if  arr[i - 1] < arr[i] > arr[i + 1] and arr[i] > 300 :
            res.append(i)
    return(res)


directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
file = directory / "freqs.txt"

time = []
signals = []

with file.open('r') as f:
    data = f.readlines()
    
    for i in range(0, len(data), 6):
        
        time.append(float(data[i]))
        
        signals.append( [ float( data[i + 1] ) , float( data[i + 2] ), float( data[i + 3] ) , float( data[i + 4] ), float( data[i + 5] ) ] )

signals = np.array(signals)
time = np.array(time)
time = time - time[0]
dt = time[1]


ft = []

for i in range(len(signals[0])):
    ft.append( np.abs( np.fft.rfft( unbias( signals[ :, i] ) ) ) )

freqs = np.fft.rfftfreq( len(time), dt)
for i in range(len(ft)):
    print( freqs[local_max(ft[i])] )

fig = plt.figure()
plt.subplot(211)

for i in range(len(signals[0])): 
    plt.plot( time, signals[: , i] )

plt.subplot(212)

for i in range(len(ft)): 
    plt.plot( freqs, ft[i] )

plt.show()
