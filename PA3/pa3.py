# g(x)=cos(pi/6 *x) 0<x<3 \dx = =0.05
import math
import numpy as np
import matplotlib as plt

dx = 0.05
N = (3 - 0) / dx
df = (1 / N) / dx
fs = 1 / dx
# sampling
f = np.linspace(0, 3, 20)
gd = []
for n in range(int(N)):
    temp = math.cos((math.pi / 6) * (n * dx))
    gd.append(temp)
# DFT
gd = np.array(gd)

Gd = np.fft.fft(gd)

# Mapping
G1 = []
f_coord = []
for m in range(int(N)):
    if m <= N / 2:
        f_coord.append(m * df)
        G1.append(Gd[m] * dx)
    else:
        f_coord.append(m * df - fs)
        G1.append(Gd[m] * dx)
# Modulation
G = np.array(G1)
print(G)
