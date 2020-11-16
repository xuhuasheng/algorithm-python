# 输入一个正数, 打印出和为s的连续正数序列(至少含有两个数). 
# 例如, 输入15, 由于1+2+3+4+5=4+5+6=7+8=15, 所以打印出3个连续序列1~5, 4~6, 7~8

# 双指针 滑动窗口

def findContinueSeq(sum):
    if sum < 3:
        return
    left = 1
    right = 2
    mid = (sum+1)//2
    # 循环条件：左区间 小于 中间位置
    while left < mid:
        cur = (left + right) * (right - left + 1) // 2
        if cur == sum:
            print(list(range(left, right+1)))
            # 增大右区间，重新驱动滑动窗口
            right += 1
        elif cur < sum:
            right += 1
        else:
            left += 1
    return

def findContinueSeq2(sum):
    if sum < 3:
        return
    left = 1
    right = 2
    # 循环条件：左区间小于右区间，不越界
    while left < right:
        cur = (left + right) * (right - left + 1) // 2
        if cur == sum:
            print(list(range(left, right+1)))
            # 增大左区间， 重新驱动滑动窗口
            left += 1
        elif cur < sum:
            right += 1
        else:
            left += 1
    return

    

if __name__ == "__main__":
    findContinueSeq(15)
    findContinueSeq2(15)
