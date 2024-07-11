from easywaves import *
import matplotlib.pyplot as plt
from numpy import arange

t = []
y = []
for i in range (0,101):
    t.append(i)
    y.append(ease_map(i, 0, 100, -10, 10, circIn))

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, y)
plt.xlabel('Time/Distance')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()

t = []
y = []
for i in arange (0,10,0.01):
    t.append(i)
    y.append(decayDamped(i, 100, 10))

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, y)
plt.xlabel('Time/Distance')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
