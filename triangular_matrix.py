def u_tri(A):
    n = len(A)
    p = len(A[0])
    utri = []

    for i in range(n):
        utri.append([])
        for j in range(p):
            if i > j :
                utri[i].append(0)
            else:
                utri[i].append(A[i][j])
    return utri

def l_tri(A):
    n = len(A)
    p = len(A[0])
    ltri = []

    for i in range(n):
        ltri.append([])
        for j in range(p):
            if i < j:
                ltri[i].append(0)
            else:
                ltri[i].append(A[i][j])
    return ltri


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(u_tri(A))
print(l_tri(A))
