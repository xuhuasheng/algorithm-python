# 输入数字，嗯，按顺序打印出从一到最大的n位数十进制数。
# 比如输入3，则打印出1231直到最大的三位数999。

# 掉入陷阱：当位数n大于64位时，long都会溢出
# 解决大数问题：C++可以用字符串或者数组存储大数
            # python java只能用数组，因为字符串是不可更改的
def print1ToMaxOfNDigits_1(n):
    i = 0
    limit = 1
    while i < n:
        limit *= 10
        i += 1
    for i in range(limit):
        print(i)

# 正确解法：
def print1ToMaxOfNDigits_2(n):
    numStr = [0] * (n+1)
    while numStr[0] == 0:
        increase(numStr)
        printNum(numStr)
        print()


def increase(numStr):
    numStr[-1] += 1
    # 如果个位有进位
    if numStr[-1] > 9:
        numStr[-1] -= 10 
        for i in range(len(numStr)-2, -1, -1):
            numStr[i] += 1
            if numStr[i] > 9:
                numStr[i] -= 10
            else:
                break

def printNum(numStr):
    isZeroStart = True
    for i in range(len(numStr)):
        if isZeroStart and numStr[i] == 0:
            continue
        else:
            isZeroStart = False
        print(str(numStr[i]), end='')

if __name__ == "__main__":
    print1ToMaxOfNDigits_2(2)



