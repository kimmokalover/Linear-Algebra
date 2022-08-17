def identitiy(n):
    I = []
    for i in range(n):
        I.append([])
        for j in range(n):
            if(i == j):
                I[i].append(1)
            else :
                I[i].append(0)
    return I

def matmul(A, B):
    n1 = len(A)
    p = len(A[0])
    n2 = len(B[0])
    AB = []
    for i in range(n1):
        AB.append([])
        for j in range(n2):
            sum = 0
            for k in range(p):
                sum += A[i][k]*B[k][j]
            AB[i].append(sum)
    return AB


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

I = identitiy(3)
print(matmul(A,I))
print(matmul(I, A))
