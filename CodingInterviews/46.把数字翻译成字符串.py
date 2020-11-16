# 给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”…25翻译成“z”。
# 一个数字有多种翻译可能，例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。
# 实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 递归地思考问题，自底向上地解决问题
# f(n)表示从右边数第n位的结果
# f(0) = 1
# f(1) = 1
# f(n) = f(n-1) + g(n, n-1)f(n-2)
# 当str(n)x10+str(n-1)在10-25时，g=1，否则=0



# 动态规划：实质是自底向上地计算并储存复用结果
# 时间复杂度:o(n)
# 空间复杂度:o(n)
def getTranslationCount(num):
    if num < 0:
        return 0
    numstr = str(num)
    if len(numstr) == 1:
        return 1
    restmp = [0] * (len(numstr)+1)
    restmp[0] = 1
    restmp[1] = 1
    g = 0
    n = 0
    for i in range(len(numstr)-2, -1, -1):
        dd = int(numstr[i])*10+int(numstr[i+1])
        if dd >= 10 and dd <=25:
            g = 1
        else:
            g = 0
        n = len(numstr)-i
        restmp[n] = restmp[n-1] + g*restmp[n-2]
    return restmp[n]

if __name__ == "__main__":
    print(getTranslationCount(12258))