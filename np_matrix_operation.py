import numpy as np

def np_mat_add():
    A = np.array([[2, 7], [3, 4], [6, 1]])
    B = np.array([[1, 4], [4, -1], [2, 5]])
    print(A + B)
    print()

def np_mat_sub():
    A = np.array([[2, 7], [3, 4], [6, 1]])
    B = np.array([[1, 4], [4, -1], [2, 5]])
    print(A - B)
    print()

def np_mat_scalar_mul():
    a = 2
    A = np.array([[2, 7], [3, 4], [6, 1]])
    print(a * A)
    print()

def np_mat_ele_product():
    A = [[1, 5], [6, 4], [2, 7]]
    B = [[5, -1], [1, 2], [4, 1]]
    print(np.multiply(A, B))
    print()

def np_mat_mul():
    A = [[2, 7], [3, 4], [5, 2]]
    B = [[3, -3, 5], [-1, 2, -1]]
    print(np.matmul(A, B))
    print()


np_mat_add()
np_mat_sub()
np_mat_scalar_mul()
np_mat_ele_product()
np_mat_mul()
