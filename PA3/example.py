# g(x)=cos(pi/6 *x) 0<x<3 \dx = =0.05
import math
from math import e
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("tkagg")
dx = 0.1
N = (1 - (-1)) / dx
df = (1 / N) / dx

fs = 1 / dx
# sampling
f = []
for i in range(int(N)):
    f.append(i * dx)
f = np.array(f)

g1 = (1 - np.abs(f - 1)) ** 2

Gd = np.fft.fft(g1)


m = np.linspace(0, N, N)

# markerline, stemlines, baseline = plt.stem(m, Gd.real, "-.")
# plt.setp(baseline, "color", "r", "linewidth", 2)

# plt.show()

# Mapping
G1 = []
f_coord = []
f_coord_plt = []
for m in range(int(N)):
    if m <= N / 2:
        f_coord.append(m * df)
        G1.append(Gd[m] * dx)
    else:
        f_coord.append(m * df - fs)
        G1.append(Gd[m] * dx)
# Modulation
f_coord = np.array(f_coord)

# print(f_coord[0])
# G1 = np.array(G1)
# print(G1)
G = []
for i in range(len(f_coord)):
    fp = 1j * 2 * math.pi * f_coord[i]
    t = e ** fp
    G.append(t * G1[i])

# G = math.exp(fp) * G1
# G = np.array(G1)
pts = []
for i in range(len(G)):
    temp = []
    temp = tuple([f_coord[i], G[i]])

    pts.append(temp)


"""
G_plot = sorted(pts, key=lambda x: x[1].real)

f_coord = []
G_plot_real = []
for i in range(len(G_plot)):
    f_coord.append(G_plot[i][0])
    G_plot_real.append(G_plot[i][1])
print(f_coord)
print(G_plot_real)
plt.plot(f_coord, G_plot_real, "ro")
plt.show()
"""
G = np.array(G)
print(G)
G_plot = G.real

plt.plot(f_coord, G.real, "ro")

plt.show()
