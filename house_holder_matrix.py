def outer_product(a, b):
    n1 = len(a)
    n2 = len(b)
    ret = []

    for i in range(n1):
        ret.append([])
        for j in range(n2):
            ret[i].append(a[i]*b[j])
    return ret

def inner_product(a, b):
    n1 = len(a)
    ret = 0
    for i in range(n1):
        ret += a[i]*b[i]
    return ret

def subtract(a, b):
    n = len(a)
    p = len(a[0])
    ret = []

    for i in range(n):
        ret.append([])
        for j in range(n):
            ret[i].append(a[i][j] - b[i][j])
    return ret

def identity(n):
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(n):
            if i == j:
                ret[i].append(1)
            else:
                ret[i].append(0)
    return ret

def householder(v):
    n = len(v)
    outer_mat = outer_product(v, v)
    inner_val = inner_product(v, v)
    V = []
    for i in range(n):
        V.append([])
        for j in range(n):
            V[i].append((outer_mat[i][j] * 2)/inner_val)
    H = subtract(identity(n), V)
    return H

V = [1, 0, 2, 3]
H = householder(V)

for i in range(len(H)):
    print(H[i])
