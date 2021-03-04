import numpy as np
import matplotlib.pyplot as plt

def circle_points(r, n):
    circles = []
    for r, n in zip(r, n):
        t = np.linspace(0, 2*np.pi, n, endpoint=False)
        x = r * np.cos(t)
        y = r * np.sin(t)
        circles.append(np.c_[x, y])
    return circles
n = np.random.randn(100)
r = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
circles = circle_points(r, n)
fig, ax = plt.subplots()
for circle in circles:
    ax.scatter(circle[:, 0], circle[:, 1])
ax.set_aspect('equal')
plt.show()