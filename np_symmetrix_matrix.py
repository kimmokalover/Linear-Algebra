import numpy as np

A = np.array([[1, 0, 2], [0, 2, 1], [2, 1, 1]])
print(A)
At = np.transpose(A)
print(At)
print(A == At)

AA = A

for i in range(9):
    AA = np.matmul(AA, A)
    print("행렬 A의", i + 2, "제곱은")
    print(AA)
    print("==========================")

A = np.array([[1, 0, 3], [2, 1, 4], [0, 1, 1]])
print(np.matmul(A, np.transpose(A)))
print(np.matmul( np.transpose(A), A))
