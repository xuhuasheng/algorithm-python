# 题目：最小的k个数（第k小的数）
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

# 基于快排的partition，只分拨不排序
# 时间复杂度o(n)
# 但是会改变原始数组
def getLeastKNums(arr, k):
    if arr is None or len(arr) <= 0 or len(arr) < k or k <= 0:
        return []
    start = 0
    end = len(arr) - 1
    index = partition(arr, start, end)
    while index != k-1:
        if index < k-1:
            start = index + 1
            index = partition(arr, start, end)
        else:
            end = index - 1
            index = partition(arr, start, end)
    return sorted(arr[:k])

def partition(arr, start, end):
    pivot = arr[start]
    mark = start
    for i in range(start+1, end+1):
        if arr[i] < pivot:
            mark += 1
            arr[i], arr[mark] = arr[mark], arr[i]
    arr[start] = arr[mark]
    arr[mark] = pivot
    return mark

if __name__ == "__main__":
    arr = [4, 5, 1, 6, 2, 7, 3, 8]
    print(getLeastKNums(arr, 4))