import pathlib
import numpy as np
import matplotlib.pyplot as plt
import struct

directory = pathlib.Path("/home/user/mag2021/lessons")

print(list(directory.glob("*.txt")))

file = directory / "twinned.dat"

with file.open("rb") as  f:

    size = struct.unpack("I", f.read(4))[0]
    image = np.zeros((size, size), dtype="uint8")
    while True:
        bts = f.read(10)
        if not bts:
            break
        y, x, val = struct.unpack("IIH", bts)
        image[y, x] = val

extrema = []

# for y in range(image.shape[0] - 2):
#     for x in range(image.shape[1] - 2):
#         sub = image[y:y+3, x:x+3].astype("f4")
#         dsub = sub.copy()
#         dsub[1, 1] = 0
#         avg = np.average(dsub)
#         if sub[1, 1] > avg:
#             print(sub)
#             extrema.append([y, x])
        # if sub[1, 1] == 0:
        #     continue
        # diff = sub - sub[1, 1]
        # diff = diff[diff != 0]
        # if np.all(diff < 0) and diff.size == 7:
        #     print(sub)
        #     extrema.append([y, x])

v = np.average(image, axis=1)
h = np.average(image, axis=0)

vx = []
for i in range(1, len(v)-1):
    if  v[i - 1] < v[i] > v[i + 1]:
        vx.append(i)

hx = []
for i in range(1, len(h)-1):
    if  h[i - 1] < h[i] > h[i + 1]:
        hx.append(i)

if len(vx) == 2:

    for v in vx:
        sl = image[v, :]
        extrema.append([v, np.argmax(sl)])
else:
    for v in hx:
        sl = image[:, v]
        extrema.append([np.argmax(sl), v])

# plt.subplot(121)
# plt.plot(v)
# plt.plot(vx, v[vx], 'o')
# plt.plot()
# plt.subplot(122)
# plt.plot(h)
# plt.plot(hx, h[hx], 'o')
# plt.show()
# print(extrema)

# plt.imshow(image)
# y = [ex[0] for ex in extrema]
# x = [ex[1] for ex in extrema]
# plt.scatter(x, y)

image[image < 10] = 0
image[image > 10] = 1
plt.imshow(image)
plt.show()

