import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("tkagg")
x = np.arange(10)
plt.plot(x, x)
plt.savefig("test.png")
plt.show()