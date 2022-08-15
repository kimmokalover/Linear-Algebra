def v_add(u, v):
    n = len(u)
    w = []
    for i in range(n):
        w.append(u[i] + v[i])
    return w

def v_sub(u, v):
    n = len(u)
    w = []
    for i in range(n):
        w.append(u[i] - v[i])
    return w

def scalar_v_mul(a, u):
    n = len(u)
    w = []
    for i in range(n):
        w.append(a*u[i])
    return w

def v_mul(u, v):
    n = len(u)
    w = []
    for i in range(n):
        w.append(u[i]*v[i])
    return w

def v_div(u, v):
    n = len(u)
    w = []
    for i in range(n):
        w.append(u[i]/v[i])
    return w

u = [6, 5, 9]
v = [2, 2, -3]

w = v_div(u, v)
print(w)
