import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
I = np.identity(3)
print(A)
print(I)
print(np.matmul(A, I))
print(np.matmul(I, A))
