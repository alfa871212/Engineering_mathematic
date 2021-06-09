# g(x)=cos(pi/6 *x) 0<x<3 \dx = =0.05
import math
from math import e
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("tkagg")
dx = 0.05
N = (3 - 0) / dx
df = (1 / N) / dx
fs = 1 / dx
# sampling
f = np.linspace(0, 3, N + 1)
print(len(f))
f1 = np.cos((math.pi / 6) * f)


Gd = np.fft.fft(f1)
m = np.linspace(0, 61, 61)

# Mapping
G1 = []
f_coord = []
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

# G = math.exp(fp) * G1
# G = np.array(G1)
G = np.array(G)
plt.plot(f_coord, G.real, "ro")

plt.show()
