import numpy as np 
import math

def gram_schmidt(A):
    n = A.shape[1]
    for j in range(n):
        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
        A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    return A
def modgram_schmidt(A):
    n = A.shape[0]
    for j in range(n):
        for k in range(j):
            A[j, :] -= np.dot(A[k, :], A[j, :]) * A[k, :]
        A[j, :] = A[j, :] / np.linalg.norm(A[j, :])
    return A
def wgram_schmidt(A,w):
    n = A.shape[1]
    for j in range(n):
        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]*w[n]
        A[:, j] = (A[:, j] / np.linalg.norm(A[:, j]))*(1/np.sqrt(w[n]))
    return A
def modwgram_schmidt(A,w):
    n = A.shape[0]
    for j in range(n):
        for k in range(j):
            A[j, :] -= np.dot(A[k, :], A[j, :]) * A[k, k]*w[n]
        A[j, :] = (A[j, :] / np.linalg.norm(A[j, :]))*(1/np.sqrt(w[n]))
    return A

w=[]
for n in range(16):
    w.append(1-n/16)

b=[]
for k in range(6):
    temp=[]
    for n in range(16):
        temp.append(math.cos(k*n))
    b.append(temp)


d = np.array(b)
e = np.array(b)
print("GS:")
print(modgram_schmidt(d))
print("GS with weight:")
print(modwgram_schmidt(e,w))
