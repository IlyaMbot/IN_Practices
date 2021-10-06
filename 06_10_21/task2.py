import json
import numpy as np
import matplotlib.pyplot as plt
import pathlib

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")

file1 = directory / "eft.json"
file2 = directory / "stations.json"


with file1.open('r') as f1:
    data1 = json.load(f1)
with file2.open('r') as f2:
    data2 = json.load(f2)

#print(data1[1]['location'])

arr1 = np.zeros((len(data1), 2))
arr2 = np.zeros((len(data2), 2))

eft = {}
stat = {}

for i, item in enumerate(data1):
    eft[item['code']] = item['location']['lon'], item['location']['lat']
    
for i, item in enumerate(data2):  
    stat[item['code']] = item['location']['lon'], item['location']['lat']

common = []

set1 = set(list(eft))
set2 = set(list(stat))

common = set1.intersection(set2)
coords = []
for name in common:
    coords.append(eft[name])

eft = np.array(list(eft.values()))
stat = np.array(list(stat.values()))

coords = np.array(coords)
'''
for eft in arr2:
    for station in arr1:
        if( eft[0] == station[0] and eft[1] == station[1] ):
            common.append(eft)

common = np.array(common)
'''

plt.scatter(stat[:,0], stat[:,1], label = 'eft')
plt.scatter(eft[:,0], eft[:,1], label = 'stations')
plt.scatter(coords[:,0], coords[:,1], marker = 'x', color = 'k' , label = 'common')
plt.legend()
plt.show()