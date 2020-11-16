# 求最大公约数：最大的公共除数：[1, min(a,b)]

# 辗转相除法（欧几里得算法）：
# 定理：两个正整数a和b（a > b），它们的最大公约数等于a除以b的余数c（a%b）和较小数b的最大公约数
# 时间复杂度：o(log(max(a,b)))
# 局限性：当两个a，b较大时，%取模运算的性能会比较差
def getGreatestCommomDivisor1(a, b):
    max = a if a>b else b
    min = a if a<b else b
    c = max % min
    if c == 0:
        return min  #直到能被整除，此时最大公约数为除数
    else:
        return getGreatestCommomDivisor1(c, min)


# 更相减损术
# 定理：两个正整数a和b（a > b），它们的最大公约数等于a-b的差值c和较小数b的最大公约数
# 时间复杂度：o(max(a,b))
# 局限性：当两数相差悬殊时，如10000和1的最大公约数，要递归9999次
def getGreatestCommomDivisor2(a, b):
    if a == b:
        return a    #直到两数相等，最大公约数为本身
    max = a if a>b else b
    min = a if a<b else b
    c = max - min
    return getGreatestCommomDivisor2(c, min)


# 辗转相除法和更相减损术结合
# 时间复杂度：o(log(max(a,b)))
def getGreatestCommomDivisor3(a, b):
    if a == b:
        return a
    if (a&1) == 0 and (b&1) == 0:   # a偶 b偶
        return getGreatestCommomDivisor3(a>>1, b>>1)<<1
    elif (a&1) == 0 and (b&1) != 0: # a偶 b奇
        return getGreatestCommomDivisor3(a>>1, b)
    elif (a&1) != 0 and (b&1) == 0: # a奇 b偶
        return getGreatestCommomDivisor3(a, b>>1)
    else: # a奇 b奇
        max = a if a>b else b
        min = a if a<b else b
        c = max - min # 两个奇数相减 差为偶
        return getGreatestCommomDivisor2(c, min)