import matplotlib.pyplot as plt
from matplotlib.axis import Axis
from matplotlib.ticker import MultipleLocator
import numpy as np

    

settings = np.loadtxt("settings_old.txt" , dtype=float, delimiter = '\n')

print(settings[0], settings[1])

V_data = np.loadtxt("data_old.txt" , dtype=float, delimiter = '\n')

time = len(V_data)/settings[0]
T_data = np.arange(0, time, 1/settings[0], dtype=float) 
 
fig, ax = plt.subplots(figsize = (16,10), dpi = 400)

ax.set_xlabel("Время t,с")
ax.set_ylabel("Напряжение V,В") 


ax.grid(which = "major", visible = True)
ax.grid(which = "minor", visible = True)


Axis.set_minor_locator(ax.xaxis, MultipleLocator(2))
Axis.set_minor_locator(ax.yaxis, MultipleLocator(0.1))


plt.xlim(0, 85)
plt.ylim(0, 3.5)

ax.plot(T_data, V_data)
fig.savefig("test.png")
