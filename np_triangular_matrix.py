import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Au = np.triu(A)
print(Au)

Al = np.tril(A)
print(Al)
