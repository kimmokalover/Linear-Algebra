def toeplitz(a, b):
    n1 = len(a)
    n2 = len(b)
    A = []
    for i in range(n1):
        A.append([])
        for j in range(n2):
            if i > j :
                A[i].append(a[i - j])
            else :
                A[i].append(b[j - i])
    return A

a = [1, 0, -2, -4]
b = [1, 3, 5, 7, 9]

print(toeplitz(a,b))
