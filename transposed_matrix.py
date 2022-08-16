import numpy as np

def mat_transpose(A):
    n = len(A)
    p = len(A[0])
    At = []
    for i in range(p):
        At.append([])
        for j in range(n):
            At[i].append(A[j][i])
    return At

def np_mat_transpose(A):
    At = np.transpose(A)
    return At

A = [[1, 5], [3, 4], [6, 2]]
ret = mat_transpose(A)
print(ret)
print()
A = np.array([[1, 5], [3, 4], [6, 2]])
ret = np_mat_transpose(A)
print(ret)
