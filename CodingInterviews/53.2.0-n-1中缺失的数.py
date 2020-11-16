# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
# 在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

# 方案一：时间复杂度为O(n)
# 先用公式n(n-1)/2求出数组0~n-1的和，记为s1；
# 再求出数组元素的和，记为s2；
# 用s1减去s2就可以求得缺失的数字。
def getLostNum0(arr):
    n = len(arr)+1
    s1 = n*(n-1)//2
    s2 = 0
    for i in arr:
        s2 += i
    return s1-s2

# 方案二：时间复杂度为o(logn)
#  在已序数列中查找，首选二分查找算法。由题意得：在缺失得数字前面，数组元素与数组下标相等。
# 如果中间元素与下标相等，则从中间值的右侧查找；
# 如果中间元素与下标不相等：如果此时下标等于0，或者前一个元素等于下标，则此时的下标就是缺失的数字；否则从左侧查找。

def getLostNum1(arr):
    if arr is None or len(arr) == 0:
        return None
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] != mid:
            if mid > 0 and arr[mid-1] == mid-1 or mid == 0:
                return mid
            else:
                end = mid-1
        else:
            start = mid + 1
    return -1

def getLostNum2(arr, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] != mid:
        if mid > 0 and arr[mid-1] == mid-1 or mid == 0:
            return mid
        else:
            end = mid-1
    else:
        start = mid + 1
    return getLostNum2(arr, start, end)

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,7,8,9,10]
    print(getLostNum0(arr))
    print(getLostNum1(arr))
    print(getLostNum2(arr, 0, len(arr)-1))

