def transpose(A):
    n = len(A)
    p = len(A[0])
    At = []
    for i in range(p):
        At.append([])
        for j in range(n):
            At[i].append(A[j][i])
    return At

def matmul(A, B):
    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(p2):
            sum = 0
            for k in range(p1):
                sum += A[i][k]*B[k][j]
            ret[i].append(sum)
    return ret

A = [[1, 0, 2], [0, 2, 1], [2, 1, 1]]

At = transpose(A)
print(At)
print(At == A)

AA = A
for i in range(0, 9):
    AA = matmul(AA, A)
    print("행렬 A의", i + 2, "제곱은", AA)

A = [[1, 0, 3], [2, 1, 4], [0, 1, 1]]
At = transpose(A)
print(A)

print(matmul(A, At))
print(matmul(At, A))
