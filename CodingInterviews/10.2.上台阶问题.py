# f(1) = 1
# f(2) = 2
# f(n) = f(n-1) + f(n-2)

def upstair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    f1 = 1
    f2 = 2
    res = 0
    for i in range(3, n+1):
        res = f1 + f2
        f1 = f2
        f2 = res
    return res
