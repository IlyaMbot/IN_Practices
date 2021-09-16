#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def func_y(x, a = 1, b = 1, c = 1):    
    return(a + c + b * x)
    
def func_i(x, i = 1):
    return(x ** i)

x = np.arange(-10, 10.2, 0.2)
i = np.arange(1,5)

a = 2
b = 3


fig = plt.figure()
plt.subplot(111)
plt.plot(x, func_y(x, a, b))
plt.show()
