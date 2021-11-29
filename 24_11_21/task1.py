import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import signal

def next_imf(t, s):
    
    maxpks = signal.argrelmax(s)[0] 
    minpks = signal.argrelmin(s)[0] 
    
    if t[maxpks[0]] < t[minpks[0]]:
        minpks = np.hstack([[0], minpks])
    else:
        maxpks = np.hstack([[0], maxpks ])

    if t[maxpks[-1]] > t[minpks[-1]]:
        minpks = np.hstack([minpks, [len(s) - 1] ])
    else:
        maxpks = np.hstack([maxpks, [len(s) - 1] ])

    
    fip = sp.interpolate.InterpolatedUnivariateSpline(t[maxpks], s[maxpks], k = 3)
    env_max = fip(t)
    
    fip = sp.interpolate.InterpolatedUnivariateSpline(t[minpks], s[minpks], k = 3)
    env_min = fip(t)

    env_mean = (env_max + env_min)/2
    return( s - env_mean, env_mean , maxpks, minpks)

t = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
s1 = np.sin(2 * t)
s2 = np.sin(t / 2)
s3 = np.cos(t * 4)
s = s1 + s2 + s3

imf1, env1, maxpks, minpks = next_imf(t, s)
imf2, env2, _, _ = next_imf(t, imf1)
imf3, env3, _, _ = next_imf(t, imf2)
imf4, env4, _, _ = next_imf(t, imf3)


plt.subplot(221)
plt.plot(t, s)
plt.plot(t,env1)

plt.subplot(222)
plt.plot(t, imf2)
plt.plot(t,env2)

plt.subplot(223)
plt.plot(t, imf3)
plt.plot(t,env3)

plt.subplot(224)
plt.plot(t, imf4)
plt.plot(t,env4)

plt.show()
