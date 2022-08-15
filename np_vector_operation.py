import numpy as np

def np_add():
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    w = u + v
    print(w)
def np_sub():
    u = np.array([7, 3, 9])
    v = np.array([2, 5, 7])
    w = u - v
    print(w)
def np_scalar_mul():
    a = 3
    u = np.array([1, 2, 4])
    w = a * u
    print(w)

def np_mul():
    u = np.array([1, 2, 4])
    v = np.array([7, 3, 2])
    w = u * v
    print(w)
def np_div():
    u = np.array([6, 5, 9])
    v = np.array([2, 2, -3])
    w = u / v
    print(w)

np_add()
np_sub()
np_scalar_mul()
np_mul()
np_div()
