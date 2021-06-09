import numpy as np
from math import e

n = np.arange(0, 11, 1)
Px1 = 12 / (11 * (n + 1) * (n + 2))
Px2 = ((1 - e ** -0.5) / (1 - e ** -5.5)) * (e ** (-0.5 * n))
H1 = 0
H2 = 0
for i in n:
    H1 += Px1[i] * np.log(Px1[i])
    H2 += Px2[i] * np.log(Px2[i])

H1 = -H1
H2 = -H2
print("H1: ", H1)
print("H2: ", H2)
