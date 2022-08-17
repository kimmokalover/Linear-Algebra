from scipy.linalg import toeplitz

A = toeplitz([1, 0, -2, -4], [1, 3, 5, 7, 9])
print(A)
