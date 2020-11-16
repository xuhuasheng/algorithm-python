# 在一个长度为n+1的数组里所有数字都在1~n的范围内，
# 所以数组中至少有一个数字是重复的
# 请找出数组中任意一个重复的数字。但不能修改输入的数组

# 时间复杂度o(n)
# 空间复杂度o(n)
def getDuplicateNum1(arr):
    arr2 = [0] * len(arr)
    for i in arr:
        if arr2[i] == i:
            return i
        else:
            arr2[i] = i

# 分治
# 时间复杂度o(nlogn)
# 空间复杂度o(1)
def getDuplicateNum2(arr):
    start = 1
    end = len(arr) - 1
    while end >= start:
        mid = (end-start)//2+start
        count = countRange(arr, start, mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > mid-start+1:
            end = mid
        else:
            start = mid +1
    return -1

def countRange(arr, start, end):
    count = 0
    for i in arr:
        if i >= start and i <= end:
            count += 1
    return count
