# 无序数组里有99个重复的数，范围1——100，缺失一个1-100的整数

def findLostNum(arr):
    sum = 0
    for i in range(1, 101):
        sum += i
    arrSum = 0
    for i in arr:
        arrSum += i
    return sum - arrSum

# 扩展1：一个无序数组里有若干个正整数，范围是1-100，其中99各个整数都是出现了偶数次
# 只有1个整数出现了奇数次，找到这个数
# 解法
# 异或：偶数次的数异或必为0
#       奇数次的数异或为自身

# 扩展2：一个无序数组里有若干个正整数，范围是1-100，其中98各个整数都是出现了偶数次
# 有2个整数出现了奇数次，找到这个2个数

def findNum(arr):
    xorRes = 0
    for i in arr:
        xorRes ^= i
    if xorRes == 0:
        return None, None
    separator = 1
    while xorRes & separator == 0:
        separator <<= 1
    resA = 0
    resB = 0
    for i in arr:
        if i & separator == 0:
            resA ^= i
        else:
            resB ^= i
    return resA, resB

def fibo(x):
    f0 = 0
    f1 = 1
    if x == 0:
        return f0
    if x == 1:
        return f1
    res = 0
    if x >= 2:
        for i in range(x-1):
            res = f0 + f1
            f0 = f1
            f1 = res
    return res

def printFibo(n):
    f1 = 1
    f2 = 1
    fiboList = []
    for i in range(n):
        fiboList.append(f1)
        res = f1+f2
        f1 = f2
        f2 = res
    return fiboList



if __name__ == "__main__":
    arr = [4,1,2,2,5,1,4,3]
    a, b = findNum(arr)
    print(a, b)
    print(fibo(3))
    print(fibo(4))
    print(fibo(5))
    print(printFibo(5))

