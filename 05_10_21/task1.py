import json
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import time
from scipy.spatial.distance import cdist, pdist, squareform


def station_distance(s1, s2):
    return( (s1['x'] - s2['x'])**2 + (s2['y'] - s2['y'])**2 )
    

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
#file = directory / "stations.json"
file = directory / "2016-02-13.json"


with file.open('r') as f:
    data = json.load(f)


min_dist = 1234567890
name1 = ''
name2 = ''

t = time.time()

arr = np.zeros((len(data), 2))
for i, item in enumerate(data):
    arr[i] = item['x'], item['y']

#distances = cdist(arr, arr)

distances = squareform(pdist(arr))
indexes = np.argwhere(distances  == 0)
print(indexes)

print(np.unravel_index(np.argmin(distances != 0), shape = arr.shape))
pairs = []

   

'''
for i in range(len(data)):
    for j in range(len(data)):
        pair = sorted((i, j))
        if pair not in pairs:
            pairs.append(pair)
        else:
            continue
        if i != j:
            d = station_distance(data[i], data[j])
            if d < min_dist:
                name1 = data[i]['name']
                name2 = data[j]['name']
                min_dist = d
'''

t2 = time.time()
print(f'Elapsed {time.time() - t}')
print(f'dist = {min_dist} between {name1} and {name2}')