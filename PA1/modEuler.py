import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint
import itertools

marker = itertools.cycle((",", "+", ".", "o", "*"))
from solver import odeModEuler

# derivative y'=sqrt(y)*exp(-0.1x^2)
def y_prime(y, x):
    return np.sqrt(y) * np.exp(-0.1 * (x ** 2))


# Setting range
x = np.linspace(0, 10, 200)

# Setting init value
y_0 = 1

y_scipy = odeint(y_prime, y_0, x)
y_scipy = np.concatenate(y_scipy)

h = 0.01

legend_lis = []
for cnt in range(10):
    y_mod_euler = odeModEuler(y_prime, y_0, x, h)
    mod_euler_err = np.absolute(100 * (y_mod_euler - y_scipy))
    plt.plot(x, mod_euler_err, marker=next(marker))
    legend_lis.append(str(0.01 * (cnt + 1)))
    h += 0.01

plt.legend(legend_lis)
plt.grid(True)
plt.savefig("modEuler.png")
plt.show()
plt.close()