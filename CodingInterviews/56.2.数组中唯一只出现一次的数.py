# 题目2：在一个数组中除了一个数字值出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字
# 考察位运算

# 对每个数字按位累加
# 在对结果的每位%3，如果==0，则那个数字该位为0， 否则为1
# 时间复杂度：o(n)
# 空间复杂度：o(1)
def findNumberAppearingOnce(arr):
    bitSum = [0] * 32
    mask = 0x1
    for i in range(32):
        for num in arr:
            bit = (num & mask)
            if bit != 0:
                bitSum[i] += 1
        mask = mask << 1
    res = 0
    weight = 0
    for i in bitSum:
        res += ((i % 3) * 2**weight)
        weight += 1
    return res

if __name__ == "__main__":
    arr=[1, 1, 1, 2, 2, 2, 3]
    print(findNumberAppearingOnce(arr))


