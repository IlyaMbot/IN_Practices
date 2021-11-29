import numpy as np
import matplotlib.pyplot as plt
import pathlib
import h5py
from sdppy.emd import emd
import time
from multiprocessing import Process, Pool, Queue
from concurrent.futures import ProcessPoolExecutor as ppe

def get_trend(image, start, stop):

    trend = np.zeros((stop - start, image.shape[1] ))

    for i in range(start, stop):
        trend[i - start] = emd(image[i])[-1]

    return(trend)

def proc(image, start, stop, q):
    q.put(get_trend(image, start, stop))

directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
file = directory / "pco.h5"

t1 = time.time()

f = h5py.File(file, 'r')

image = f['image'][()]

with ppe(4) as p:
    future1 = p.submit(get_trend, image, 200, 205)
    future1 = p.submit(get_trend, image, 205, 210)
    
    trend = np.vstack([future1.result(), future2.result()])
print(f"{time.time() - t1}")

'''
plt.figure()
# plt.imshow(trend, cmap = 'hot', aspect = 'auto')
plt.figure()
plt.show()
'''