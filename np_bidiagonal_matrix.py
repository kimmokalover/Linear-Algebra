import numpy as np

A = np.array([[1, 2, 1, 3], [5, 3, 4 ,1], [2, 1, 7, 9], [2, 8, 1, 3]])
#print(A)

diag_ele = np.diag(A)
#print(diag_ele)
u_diag_ele = np.diag(A, k = 1)
#print(np.diag(u_diag_ele, 1))
u_diag = np.diag(diag_ele) + np.diag(u_diag_ele, k = 1)
print(u_diag)
