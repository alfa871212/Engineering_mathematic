import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import erf
from scipy.integrate import odeint
from solver import odeEuler, odeModEuler, odeRK4

# derivative y'=sqrt(y)*exp(-0.1x^2)
def y_prime(y, x):
    return np.sqrt(y) * np.exp(-0.1 * (x ** 2))


# Setting range
x = np.linspace(0, 10, 200)

# Setting init value
y_0 = 1

# Approximation solution from Wolfram
sol = 1 + 2.8025 * erf(0.316228 * x) + 1.9635 * (erf(0.316228 * x) ** 2)

# Tune h for proper value
h = 0.05

# Solve
y_euler = odeEuler(y_prime, y_0, x)
y_mod_euler = odeModEuler(y_prime, y_0, x, h)
y_rk4 = odeRK4(y_prime, y_0, x, h)
y_scipy = odeint(y_prime, y_0, x)
y_scipy = np.concatenate(y_scipy)

# Error calculation
wolfram_err = np.absolute(100 * (sol - y_scipy))
euler_err = np.absolute(100 * (y_euler - y_scipy))
mod_euler_err = np.absolute(100 * (y_mod_euler - y_scipy))
rk4_err = np.absolute(100 * (y_rk4 - y_scipy))

# plot
plt.plot(
    x,
    y_euler,
    "r.-",
    x,
    sol,
    "k.-",
    x,
    y_mod_euler,
    "b.-",
    x,
    y_rk4,
    "g.-",
    x,
    y_scipy,
    "y.-",
)
plt.legend(["Euler", "Wolfram_appro", "ModEuler", "RK4", "Scipy"])
plt.grid(True)
plt.axis([0, 10, 0, 10])
plt.savefig("plot.png")
plt.close()

# plot error
plt.plot(
    x,
    euler_err,
    "r.-",
    x,
    wolfram_err,
    "k.-",
    x,
    mod_euler_err,
    "b.-",
    x,
    rk4_err,
    "g.-",
)
plt.legend(["Euler", "Wolfram_appro", "ModEuler", "RK4"])
plt.grid(True)
plt.savefig("err.png")
plt.close()

# DataFrame creation
df = pd.DataFrame()
df["x"] = pd.Series(x)
df["Scipy"] = pd.Series(y_scipy)
df["Wolfram_appro"] = pd.Series(sol)
df["Euler"] = pd.Series(y_euler)
df["modEuler"] = pd.Series(y_mod_euler)
df["RK4"] = pd.Series(y_rk4)
df["Err_Wolfram"] = pd.Series(wolfram_err)
df["Err_Euler"] = pd.Series(euler_err)
df["Err_modEuler"] = pd.Series(mod_euler_err)
df["Err_RK4"] = pd.Series(rk4_err)
df.to_csv("stat.csv")


plt.plot(x, y_euler, "r.-", x, y_scipy, "b.-")
plt.legend(["Euler", "Scipy"])
plt.grid(True)
plt.savefig("Euler_res.png")
plt.close()

plt.plot(x, y_mod_euler, "r.-", x, y_scipy, "b.-")
plt.legend(["modEuler", "Scipy"])
plt.grid(True)
plt.savefig("modEuler_res.png")
plt.close()

plt.plot(x, y_rk4, "r.-", x, y_scipy, "b.-")
plt.legend(["rk4", "Scipy"])
plt.grid(True)
plt.savefig("rk4_res.png")
plt.close()