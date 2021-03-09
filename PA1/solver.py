import numpy as np


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
