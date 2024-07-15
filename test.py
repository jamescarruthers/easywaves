# from easywaves import ease_map
from easywaves import ease, ease_map, ease_xy, wave, Curves, npCurves
from numpy import arange
import matplotlib.pyplot as plt



xy = ease_xy([0,0], [10,100])

x, y = xy[:, 0], xy[:, 1]

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(x, y, '-x')
plt.xlabel('Time/Distance')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()


t = []
y = []
for i in range (0, 101):
    t.append(i)
    y.append(ease_map(i, 0, 100, 10, -10, Curves.circIn))

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
for i in arange (0, 2, 0.01):
    t.append(i)
    y.append(wave(i, Curves.sineInOut) * 100)

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
for i in arange (0, 10, 0.01):
    t.append(i)
    y.append(Curves.decayDamped(i, 100, 10))

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, y)
plt.xlabel('Time/Distance')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
