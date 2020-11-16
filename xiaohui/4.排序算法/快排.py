import numpy as np

# 快排：
# 时间复杂度：o(nlogn)：logn轮递归，每一次都是n
# 空间复杂度：o(logn)：快速排序每次递归都会返回一个中间值的位置，必须使用栈。所以空间复杂度就是栈用的空间
class QuickSort:
    def __init__(self):
        pass
    
    @staticmethod
    def quickSort(arr, startIndex, endIndex):
        # 递归结束条件
        if startIndex >= endIndex:
            return
        # 分区并返回基准的索引
        pivotIndex = QuickSort.partition1(arr, startIndex, endIndex)
        # 递归：对基准两边在快排
        QuickSort.quickSort(arr, startIndex, pivotIndex-1)
        QuickSort.quickSort(arr, pivotIndex+1, endIndex)

    @staticmethod
    # 双边循环法
    def partition1(arr, startIndex, endIndex):
        pivot = arr[startIndex] # 选择第一个元素为基准
        left = startIndex       # 右指针
        right = endIndex        # 左指针
        # 只要左右指针不重合
        while left != right:    
            # 向左移动右指针
            while left < right and arr[right] >= pivot:
                right -= 1
            # 向右移动左指针
            while left < right and arr[left] <= pivot:
                left += 1
            # 当左右指针移不动时，交换左右指针
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        # 此时左右指针重合，与基准元素交换
        arr[startIndex], arr[left] = arr[left], arr[startIndex]
        # 返回基准索引
        return left

    @staticmethod
    # 单边循环法
    def partition2(arr, startIndex, endIndex):
        mark = startIndex       # 分界指针
        pivot = arr[startIndex] # 选第一个元素为基准
        # 从第二个元素开始遍历到最后
        for i in range(startIndex+1, endIndex+1):
            if arr[i] < pivot:
                mark += 1
                arr[mark], arr[i] = arr[i], arr[mark]
        arr[startIndex], arr[mark] = arr[mark], arr[startIndex]
        return mark

if __name__ == "__main__":
    arr = np.array([4,4,6,5,3,2,8,1])
    print("before sorted:{}".format(arr))
    QuickSort.quickSort(arr, 0, len(arr)-1)
    print("after sorted:{}".format(arr))