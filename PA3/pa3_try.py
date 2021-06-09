import numpy as np


def cft(g, f):
    """Numerically evaluate the Fourier Transform of g for the given frequencies"""
    result = np.zeros(len(f), dtype=complex)

    # Loop over all frequencies and calculate integral value
    for i, ff in enumerate(f):
        # Evaluate the Fourier Integral for a single frequency ff,
        # assuming the function is time-limited to abs(t)<5
        result[i] = complex_quad(lambda t: g(t) * np.exp(-2j * np.pi * ff * t), -5, 5)
    return result


def complex_quad(g, a, b):
    """Return definite integral of complex-valued g from a to b,
    using Simpson's rule"""
    # 2501: Amount of used samples for the trapezoidal rule
    t = np.linspace(a, b, 2501)
    x = g(t)
    return np.integrate.simps(y=x, x=t)
