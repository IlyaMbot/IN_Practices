import numpy as np
import matplotlib.pyplot as plt
import pathlib

def parabola(x, a, b, c):
    return(a * x**2 + b * x + c)


directory = pathlib.Path("./lessons")
file = directory / "coeffs.txt"

coeffs = []

with file.open('r') as f:
    print("opened", file)
    for line in f:
        parts = line.split(' ')
        if len(parts) != 3:
            continue
        try:
            coeffs.append([int(val) for val in parts])
        except ValueError as e:
            print(f"Skip row '{e}'.")

coeffs = np.array(coeffs)

result = np.sum(coeffs, axis = 1)

x = np.linspace(-100, 100, 1000)

fig = plt.figure()
plt.subplot(111)
plt.plot(result)
plt.show()