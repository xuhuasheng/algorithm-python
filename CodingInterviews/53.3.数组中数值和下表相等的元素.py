# 假设一个单调递增的数组里的每个元素都是整数且是唯一的，
# 请编程实现一个函数，找出数组中任意一个数值等于其下标的元素，
# 例如，在数组{-3，-1,1,3,5}中数字3和它的下标相同。

# 思路：重点是已经排序了，可以用二分查找o(logn)

def getNumSameAsIndex(arr):
    if arr is None or len(arr) == 0:
        return None
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == mid:
            return arr[mid]
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid -1
    return -1

if __name__ == "__main__":
    arr=[-3,-1,1,3,5]
    print(getNumSameAsIndex(arr))
