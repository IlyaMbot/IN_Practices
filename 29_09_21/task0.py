import numpy as np
import matplotlib.pyplot as plt

def signal(t, amp = 1, freq = 1, offset = 0, func = np.sin):
    phase = 2 *  np.pi * freq * t + offset
    return(amp * func( phase))

def unbias(s):
    return(s - s.mean())

dt = 0.001
time = np.arange(0, 2, dt)
signal = signal(time, freq = 10) + signal(time, freq = 2, amp = 0.5) + signal(time, amp = 0.5, freq = 50, func = np.cos) + 50

ft = np.fft.rfft(signal)
freqs = np.fft.rfftfreq(len(time), dt)


ft2 = np.fft.rfft(unbias(signal))


fig = plt.figure()

plt.subplot(211)
plt.title("1")
plt.plot( time, signal )

plt.subplot(212)
plt.title("2")
plt.plot( freqs, np.abs(ft) )

plt.subplot(223)
plt.title("3")
plt.plot( freqs, np.abs(ft2) )
plt.show()
