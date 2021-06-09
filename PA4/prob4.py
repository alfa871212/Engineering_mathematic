import numpy as np

A = np.array([[0.75, 0.15, 0.05], [0.15, 0.75, 0.05], [0.1, 0.1, 0.9]])
x = np.array([400000, 300000, 300000])
x = x.transpose()
print(A)
A2 = np.matmul(A, A)
A4 = np.matmul(A2, A2)
print(np.matmul(A4, x))
