def mat_add(A, B):
    n = len(A)
    p = len(A[0])
    
    ret = []

    for i in range(n):
        ret.append([])
        for j in range(p):
            ret[i].append(A[i][j] + B[i][j])
    return ret

def mat_sub(A, B):
    n = len(A)
    p = len(A[0])
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(p):
            ret[i].append(A[i][j] - B[i][j])
    return ret

def mat_scalar_mul(a, A):
    n = len(A)
    p = len(A[0])
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(p):
            ret[i].append(a * A[i][j])
    return ret

def mat_ele_product(A, B):
    n = len(A)
    p = len(A[0])
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(p):
            ret[i].append(A[i][j] * B[i][j])
    return ret

def mat_mul(A, B):
    n1 = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    ret = []
    for i in range(n1):
        ret.append([])
        for j in range(p2):
            sum = 0
            for k in range(p1):
                sum += A[i][k]*B[k][j]
            ret[i].append(sum)
    return ret

                
            


A =[[2, 7], [3, 4], [6, 1]]
B = [[1, 4], [4, -1], [2, 5]]


print(mat_add(A, B))
print(mat_sub(A, B))
print(mat_scalar_mul(2, A))

A =[[1, 5], [6, 4], [2, 7]]
B = [[5, -1], [1, 2], [4, 1]]

print(mat_ele_product(A, B))

A =[[2, 7], [3, 4], [5, 2]]
B = [[3, -3, 5], [-1, 2, -1]]

print(mat_mul(A, B))
