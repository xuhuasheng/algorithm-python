# 统计一个数字在排序数组中出现的次数
# 比如排序数组为{1,2,3,3,3,4,5}，那么数字3出现的次数就是3。

# 重要信息是已经排好序-》二分查找n(logn)
# 分别用二分查找第一个和最后一个k
# 索引相减即为个数
# 时间复杂度:n(logn)
def gerNumOfK(arr, k):
    cnt = 0
    if arr is not None and len(arr)>0:
        firstk = getFirstK(arr, k)
        lastk = getLastK(arr, k, 0, len(arr)-1)
        if firstk > -1 and lastk > -1:
            cnt = lastk - firstk + 1
    return cnt
# 循环法二分查找
def getFirstK(arr, k):
    if arr is None or len(arr) == 0:
        return 0
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == k:
            if (mid > 0 and arr[mid-1] != k) or mid == 0:
                return mid
            else:
                end = mid - 1
        elif arr[mid] < k:
            start = mid +1 
        else:
            end = mid - 1
    return -1
# 递归法二分查找
def getLastK(arr, k, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if arr[mid] == k:
        if (mid < len(arr)-1 and arr[mid+1] != k) or mid == len(arr)-1:
            return mid
        else:
            start = mid + 1
    elif arr[mid] < k:
        start = mid +1 
    else:
        end = mid - 1 
    return getLastK(arr, k, start, end)



if __name__ == "__main__":
    arr= [1,2,3,3,3,3,4,5]
    print(gerNumOfK(arr, k=3))
