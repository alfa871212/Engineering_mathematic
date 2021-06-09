# g(x) = 1 – 2|x| for -2< x <2, g(x) = 0 otherwise, dx = 0.1.
import math
from math import e
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("tkagg")
dx = 0.1
N = (2 - (-2)) / dx
df = (1 / N) / dx

fs = 1 / dx
# sampling
f = []
for i in range(int(N) + 1):
    f.append(i * dx)
f = np.array(f)

g1 = 1 - 2 * np.abs(f - 2)

Gd = np.fft.fft(g1)


m = np.linspace(0, N + 1, N + 1)

# Mapping
G1 = []
f_coord = []
f_coord_plt = []
for m in range(int(N) + 1):
    if m <= N / 2:
        f_coord.append(m * df)
        G1.append(Gd[m] * dx)
    else:
        f_coord.append(m * df - fs)
        G1.append(Gd[m] * dx)
# Modulation
f_coord = np.array(f_coord)

G = []
for i in range(len(f_coord)):
    fp = 1j * 2 * math.pi * f_coord[i]
    t = e ** fp
    G.append(t * G1[i])


pts = []
for i in range(len(G)):
    temp = []
    temp = tuple([f_coord[i], G[i]])

    pts.append(temp)


G = np.array(G)
print(G)
G_plot = G.real

plt.plot(f_coord, G.real, "ro")

plt.show()
