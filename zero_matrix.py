def zero_mat(n, p):
    Z = []
    for i in range(n):
        Z.append([])
        for j in range(p):
            Z[i].append(0)
    return Z

print(zero_mat(3, 2))
