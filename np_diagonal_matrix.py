import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = np.diag([1, 3, 4])

print(np.matmul(A, D))
print()
print(np.matmul(D, A))
