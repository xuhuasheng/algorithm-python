# 归并排序：
# 时间复杂度：o(nlogn)
# 空间复杂度：o(n)
class MergeSort:
    @staticmethod
    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        return MergeSort.merge(MergeSort.mergeSort(leftArr), MergeSort.mergeSort(rightArr)) 

    @staticmethod
    def merge(left, right): 
        res = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        res += left
        res += right
        return res

def mergeSort(arr):
    # 递归的终点条件 只有一个元素 start==end
    if len(arr) == 1:
        return arr
    # 归：递归分治排序
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    # 并：合并排序好的两部分
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res

if __name__ == "__main__":
    arr = [4,4,6,5,3,2,8,1]
    arr2 = MergeSort.mergeSort(arr)
    arr3 = mergeSort(arr2)
    print(arr2)
    print(arr3)