import numpy as np
# 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
def numberOf1(n):
    cnt = 0
    flag = np.int32(1)
    while flag:
        if n & flag:
            cnt += 1
        flag <<= 1
    return cnt

if __name__ == "__main__":
    print(numberOf1(9))