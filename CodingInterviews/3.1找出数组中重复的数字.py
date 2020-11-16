# 在一个长度为n的数字里的所有数字都在0~n-1的范围内，
# 数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道重复了几次，找出数组中任意的一个重复的数字。

# 先排序o(nlogn),后遍历o(n)
# 时间复杂度o(nlogn)
# 空间复杂度o(1)
def getDuplicateNum1(arr):
    list.sort(arr)
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False

# 创建集合set或字典dict记录
# 时间复杂度o(n):遍历o(n),查表o(1)
# 空间复杂度o(n)
def getDuplicateNum2(arr):
    s = set()
    for i in arr:
        if i in s:
            return True
        else:
            s.add(i)
    return False
def getDuplicateNum3(arr):
    d = dict()
    for i in arr:
        if i in d.keys():
            d[i] += 1
            print(d)
            return True
        else:
            d[i] = 1
    return False

# 遍历数组，让每一个数字回归其对应下标的位置，若在回归中有重复则有重复数字
# 时间复杂度：o(n)
# 空间复杂度：o(1)
def getDuplicateNum4(arr):
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[arr[i]] == arr[i]:
                return True, arr[i]
            else:
                arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
    return False



if __name__ == "__main__":
    arr = [2,3,1,0,2,5,3]
    print(getDuplicateNum3(arr))