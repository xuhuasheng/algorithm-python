# 用自上而下的递归思想解决动态规划是不明智之选
# 时间复杂度o(2^n)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibo(n-1) + fibo(n-2)

# 自底向上的循环才是解决动态规划的正确道路
# 时间复杂度o(n)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    num1 = 0
    num2 = 1
    fibo = 0
    for i in range(2, n+1):
        fibo = num2 + num1
        num1 = num2
        num2 = fibo
    return fibo
