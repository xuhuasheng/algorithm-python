# 二分法的时间复杂度o(logn)
# 二分法 递归
def binarySearch1(arr, num, start, end):
    # 递归终止条件
    if start > end:
        return -1
    mid = start + (end - start)//2
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binarySearch1(arr, num, start, mid-1)
    elif arr[mid] < num:
        return binarySearch1(arr, num, mid+1, end)


# 二分法 非递归
def binarySearch2(arr, num):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end - start)//2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    lis = [99, 222, 444, 544, 555, 567, 777, 786, 787, 991, 998, 5555, 8877]
    print(binarySearch1(lis, 477, 0, len(lis)-1))
    print(binarySearch2(lis, 477))

        