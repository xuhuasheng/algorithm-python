
def moreThanHalfNum(arr):
    if arr is None or len(arr) == 0:
        return None
    mid = len(arr)//2
    start = 0
    end = len(arr)-1
    index = partition(arr, start, end)
    while index != mid:
        if index > mid:
            end = index-1
            index = partition(arr, start, end)
        else:
            start = index+1
            index = partition(arr, start, end)
    res = arr[mid]
    # 验证是否超过一半
    times = 0
    for i in arr:
        if i == res:
            times += 1
    if times *2 <= len(arr):
        return 0

    return res

def partition(arr, start, end):
    pivot = arr[start]
    mark = start
    for i in range(start+1, end+1):
        if arr[i] < pivot:
            mark += 1
            arr[mark], arr[i] = arr[i], arr[mark]
    arr[start] = arr[mark]
    arr[mark] = pivot 
    return mark

def partition2(arr, start, end):
    pivot = arr[start]
    left = start
    right = end
    while left != right:
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] < pivot:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start] = arr[left]
    arr[left] = pivot
    return left

if __name__ == "__main__":
    arr = [1,2,3,2,2,2,5,4,2]
    print(moreThanHalfNum(arr))
