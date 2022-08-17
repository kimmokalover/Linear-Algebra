def diag(A):
    n = len(A)
    D = []
    for i in range(n):
        D.append([])
        for j in range(n):
            if(i == j):
                D[i].append(A[i][j])
            else:
                D[i].append(0)
    return D

def diag_ele(A):
    n = len(A)
    D = []
    for i in range(n):
        D.append(A[i][i])
    return D

def ele2diag(a):
    n = len(a)
    D = []
    for i in range(n):
        D.append([])
        for j in range(n):
            if i == j :
                D[i].append(a[i])
            else:
                D[i].append(0)
    return D

def matmul(A, D):
    n1 = len(A)
    p1 = len(A[0])
    n2 = len(D[0])
    AD = []
    for i in range(n1):
        AD.append([])
        for j in range(n2):
            sum = 0
            for k in range(p1):
                sum += A[i][k]*D[k][j]
            AD[i].append(sum)
    return AD



A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
D = ele2diag([1, 3, 1])

AD = matmul(A, D)
print(AD)
DA = matmul(D, A)
print(DA)
