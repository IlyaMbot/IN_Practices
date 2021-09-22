import numpy as np
import matplotlib.pyplot as plt
import pathlib
import datetime as dt


directory = pathlib.Path("./lessons")
file = directory / "dtvar.txt"

coeffs = []

measures = {}

with file.open('r') as f:
    print("opened", file)
    
    for line in f:
        d, _, val = line.split(' ')
        if d not in measures.keys():
            measures[d] = []
        measures[d].append(float(val))

for day in measures:
    measures[day] = np.average(measures[day])

x = [dt.datetime.strptime(d, "%Y-%m-%d") for d in measures.keys()]
y = list(measures.values())

fig = plt.figure()
plt.subplot(111)
plt.plot(x , y)
plt.show()