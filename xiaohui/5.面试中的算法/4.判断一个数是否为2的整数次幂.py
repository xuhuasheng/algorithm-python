# 判断一个正整数是否是2的整数次幂

# 时间复杂度o(logn)
def isPowerOf2_1(n):
    temp = 1
    while temp <= n:
        if temp == n:
            return True
        # temp = temp*2
        temp = temp<<1  #左移一位比乘2快
    return False

# 规律;
# 十进制    n二进制     n-1二进制
# 2         10b         1b
# 4         100b        11b
# 8         1000b       111b
# 时间复杂度o(1)
def isPowerOf2_2(n):
    return n & (n-1) == 0
    