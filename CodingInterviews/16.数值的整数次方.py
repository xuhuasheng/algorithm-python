# 实现a的b次幂，b为整数

# 基础方法
# 时间复杂度o(n)
def power(a, b):
    if b == 0:
        return 1
    res = a
    if b > 0:
        for i in range(b):
            res *= a
    if b < 0:
        if a != 0:
            for i in range(-b):
                res *= a
        else:
            raise Exception("invalid")

# 递归 极其不推荐
# 看似牛逼 其实有很多重复计算
# 时间复杂度o(2^n)
def power2(a, b):
    if a == 0 and b < 0:
        raise Exception("invalid")
    if b == 0:
        return 1
    if b == 1:
        return a
    return power2(a, b//2) * power2(a, b-b//2)

# 动态规划 从底向上 一步步填表
# 时间复杂度o(n)
def power3(base, exponent):
    if exponent < 0 and base == 0:
        raise Exception("invalid")
    if exponent == 0:
            return 1
    if exponent == 1:
        return base
    n = exponent if exponent > 0 else -exponent
    resArr = [0] * (n+1)
    resArr[0] = 1
    resArr[1] = base
    for i in range(2, n+1):
        resArr[i] = resArr[i//2] * resArr[i-i//2]
    if exponent > 0:
        return resArr[n]
    if exponent < 0:
        return 1/resArr[n]

            

if __name__ == "__main__":
    print(power3(2, -3))

    
