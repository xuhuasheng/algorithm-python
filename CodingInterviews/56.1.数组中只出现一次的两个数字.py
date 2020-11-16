# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

# XOR异或^: 相同的数偶数次会抵消，偶数个相同的数异或等于0
# 异或定位特征，根据特征分拨数组，再对子数组求异或

# 时间复杂度o(n)
# 空间复杂度o(1)
def findNumsAppearOnce(arr):
    # 全部异或，得到的结果是那两个只出现一次的数的异或结果
    xor = 0
    for i in arr:
        xor = xor ^ i
    # 这个结果的二进制中至少有一个1，找到其第一个1的位置
    bit_index = 0
    pulse = 0x1
    while (xor & pulse) == 0:
        bit_index += 1
        pulse = pulse << 1
    # 以第一个1的位置为分类标准，把原数组划分为2个子数组，实现了这两个数的分拨
    # 在对这2个子数组分别求异或，其结果就是这两个数
    a = 0
    b = 0
    for i in arr:
        ii = i >> bit_index
        if ii & 0x1 == 0:
            a = a ^ i
        else:
            b = b ^ i
    return a, b

if __name__ == "__main__":
    arr = [2,4,3,6,3,2,5,5]
    print(findNumsAppearOnce(arr))