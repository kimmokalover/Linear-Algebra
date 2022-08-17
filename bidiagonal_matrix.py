def u_bidiag(A):
    n = len(A)
    p = len(A[0])
    ret = []

    for i in range(n):
        ret.append([])
        for j in range(p):
            if(i == j):
                ret[i].append(A[i][j])
            elif (i + 1 == j):
                ret[i].append(A[i][j])
            else :
                ret[i].append(0)
    return ret

def l_bidiag(A):
    n = len(A)
    p = len(A[0])
    ret = []

    for i in range(n):
        ret.append([])
        for j in range(p):
            if (i == j):
                ret[i].append(A[i][j])
            elif (i -1 == j):
                ret[i].append(A[i][j])
            else :
                ret[i].append(0)
    return ret

A = [[1, 2, 1, 3], [5, 3, 4, 1], [2, 1, 7, 9], [2, 8, 1, 3]]
print(u_bidiag(A))
print(l_bidiag(A))
