import json
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import datetime as dt
from scipy.interpolate import interp1d as int1d


directory = pathlib.Path("/home/conpucter/GitHub/try/lessons")
file = directory / "awk.json"

measurements = {}

with file.open('r') as f:
    data = json.load(f)

#------------------------------------------------------------------------------

for i in range(len(data)):
    date = dt.datetime.strptime(data[i]['date'].split(" ")[0], "%Y-%m-%d").date()
    if date not in measurements:
        measurements[date] = []
    measurements[date].append(data[i]['meteo']['T'])

for date in measurements:
    measurements[date] = np.average(measurements[date])

date = np.array([int(i.strftime('%j')) for i in sorted(measurements) ])
temp = np.array([measurements[date] for date in sorted(measurements) ])

#------------------------------------------------------------------------------

env_x_max = [date[0]]
env_y_max = [temp[0]]

env_x_min = [date[0]]
env_y_min = [temp[0]]

for i in range(1, len(date)-1):
    if  temp[i - 1] < temp[i] > temp[i + 1]:
        env_x_max.append(date[i])
        env_y_max.append(temp[i])
        #for i in range(1, len(date)-1):
    if  temp[i - 1] > temp[i] < temp[i + 1]:
        env_x_min.append(date[i])
        env_y_min.append(temp[i])

env_x_min.append(date[-1])
env_y_min.append(temp[-1])

env_x_max.append(date[-1])
env_y_max.append(temp[-1])

#------------------------------------------------------------------------------

fmax = int1d(env_x_max, env_y_max, kind = 'cubic')
fmin = int1d(env_x_min, env_y_min, kind = 'cubic')

env_interp_x = np.linspace(date[0], date[-1], 100)
env_interp_max = fmax(env_interp_x)
env_interp_min = fmin(env_interp_x)

#------------------------------------------------------------------------------

plt.plot(date, temp, label = "data")
plt.scatter(env_x_max, env_y_max, label = "max" )
plt.scatter(env_x_min, env_y_min, label = "max" )
plt.plot(env_interp_x, env_interp_max, label = "interp_max")
plt.plot(env_interp_x, env_interp_min, label = "interp_min")
plt.legend()
#plt.show()