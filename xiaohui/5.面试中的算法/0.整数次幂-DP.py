# 求a^b,要求时间复杂度和空间复杂度尽可能小

# 时间复杂度：o(n)
# 空间复杂度：o(1)
def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    res = a
    for i in range(b):
        res *= a
    return res

# 递归（X）动态规划最忌讳用递归解决!!!
# 时间复杂度o(2^n)
# 有重复计算
def power2(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return power2(a, b//2) * power2(a, b-b//2)

# 动态规划
# 从底向上，一步一个脚印填表
# 时间复杂度o(n)
# 空间复杂度o(n)
def power3(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    arr = [0] * (b+1)
    arr[0] = 1
    arr[1] = a
    for i in range(2. b+1):
        arr[i] = arr[i//2] * arr[i-i//2]
    return arr[b]

