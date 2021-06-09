import numpy as np


# prob:
# y=[5,3,3,4,2,2,1,2,3]
# b0=[1,1,1,1,1,1,1,1,1]
# bm=[-4^m,-3^m,-2^m,-1^m,0,1^m,2^m,3^m,4^m]
# (a) find c0,c1,c2 to minimize |y-c0b0-c1b1-c2b2|
# (b) find c0,c1,c2,c3,c4 to minimize |y-c0b0-c1b1-c2b2-c3b3-c4b4|


def create_b(m):
    return np.array([-4 ^ m, -3 ^ m, -2 ^ m, -1 ^ m, 0, 1 ^ m, 2 ^ m, 3 ^ m, 4 ^ m])


def solve(vec):
    A = np.array(vec).transpose()
    A_T = A.transpose()
    A_T_A = np.matmul(A_T, A)
    A_T_A_inv = np.linalg.inv(A_T_A)
    tmp = np.matmul(A_T_A_inv, A_T)
    res = np.matmul(tmp, y)
    return res


y = np.array([5, 3, 3, 4, 2, 2, 1, 2, 3])
b0 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
b1 = create_b(1)
b2 = create_b(2)
b3 = create_b(3)
b4 = create_b(4)
res_a = solve([b0, b1, b2])
res_b = solve([b0, b1, b2, b3, b4])

print("(a): ", res_a)
print("(b): ", res_b)
