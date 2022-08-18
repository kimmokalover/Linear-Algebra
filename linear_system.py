from copy import deepcopy


def solve(A, B):
    X = deepcopy(A)
    sol = deepcopy(B)
    n = len(X)
    
    for i in range(n):
        print('------i번째 실행 시작------')
        x_row = X[i]
        y_val = sol[i]
        
        if x_row[i] != 0:
            tmp = 1/x_row[i]
        else :
            tmp = 0
        
        x_row = [element * tmp for element in x_row]
        y_val *= tmp

        X[i] = x_row
        sol[i] = y_val
        print(x_row)
        print(y_val)
        print('------행 나누기 완료------')

        for j in range(n):
            if i == j:
                continue
            print('------j 번째 실행 시작------' )
            x_next = X[j]
            y_next = sol[j]
            x_tmp = [element * -x_next[i] for element in x_row]
            y_tmp = -x_next[i] * y_val

            for k in range(len(x_row)):
                x_next[k] += x_tmp[k]
            y_next += y_tmp

            X[j] = x_next
            sol[j] = y_next

            print(X)
            print(sol)
            print('------j 번째 실행 종료------')
        print('------i 번째 완료------')
    return sol

X = [[3, 1, 2], [2, 6, 1], [4, 0, -1]]
y = [5, 1, 3]

ret = solve(X, y)
print(ret)
