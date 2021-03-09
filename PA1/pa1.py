import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# derivative y'=sqrt(y)*exp(-0.1x^2)
# solution from wolfram -->  1 + 2.8025 erf(0.316228 x) + 1.9635 erf(0.316228 x)^2


def odeEuler(derivative, y0, x):
    y = np.zeros(len(x))
    y[0] = y0
    for n in range(0, len(x) - 1):
        y[n + 1] = y[n] + derivative(y[n], x[n]) * (x[n + 1] - x[n])
    return y


def odeModEuler(derivative, y0, x, h):
    y = np.zeros(len(x))
    y[0] = y0
    for n in range(0, len(x) - 1):
        appro = y[n] + h * derivative(y[n], x[n])
        y[n + 1] = y[n] + h * (
            (derivative(y[n], x[n]) + derivative(appro, x[n + 1])) / 2
        )
    return y


def odeRK4(derivative, y0, x, h):
    y = np.zeros(len(x))
    y[0] = y0
    for n in range(0, len(x) - 1):
        k1 = derivative(y[n], x[n])
        k2 = derivative(y[n] + 0.5 * h * k1, x[n] + 0.5 * h)
        k3 = derivative(y[n] + 0.5 * h * k2, x[n] + 0.5 * h)
        k4 = derivative(y[n] + h * k3, x[n] + h)
        y[n + 1] = y[n] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return y


# solution
t_true = np.linspace(0, 10, 200)
sol = 1 + 2.8025 * erf(0.316228 * t_true) + 1.9635 * (erf(0.316228 * t_true) ** 2)

# Setting range and function
x = np.linspace(0, 10, 200)
y_0 = 1


def y_prime(y, x):
    return np.sqrt(y) * np.exp(-0.1 * (x ** 2))


y_euler = odeEuler(y_prime, y_0, x)
# Tune h for proper value
h = 0.05
y_mod_euler = odeModEuler(y_prime, y_0, x, h)
y_rk4 = odeRK4(y_prime, y_0, x, h)
plt.plot(x, y_euler, "r.-", t_true, sol, x, y_mod_euler, "b.-", x, y_rk4, "g.-")
plt.legend(["Euler", "Sol", "ModEuler", "RK4"])
plt.grid(True)
plt.axis([0, 10, 0, 10])

plt.show()
