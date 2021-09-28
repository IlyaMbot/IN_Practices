import numpy as np
import matplotlib.pyplot as plt
import pathlib

directory = pathlib.Path("./lessons")
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

fig = plt.figure()
plt.subplot(111)

for i in range(len(signals[0])): 
    plt.plot( time, signals[: , i] )

plt.show()