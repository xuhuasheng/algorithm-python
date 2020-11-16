import numpy as np

# // 计数排序：基于数组下标和频数统计（线性时间复杂度）
# // 原始数组规模为n，极值差为m
# // 时间复杂度：o(3n+m) => o(n+m)
# // 空间复杂度：o(m+1) => o(m)
# // 局限性：1.不适合极值差m过大的
# //        2.待排序列是存在小数的，无法建立统计数组
class CountSort:
    def __init__(self):
        pass

    @staticmethod
    def countSort(arr):
        # 1.遍历原始数组o(n)，求最大值和最小值，计算差值
        # max = np.max(arr)
        # min = np.min(arr)
        max = arr[0]
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
            if arr[i] < min:
                min = arr[i]
        d = max-min
        # 2.建立统计数组o(m+1)，遍历原始数组o(n)，统计元素频数
        countArray = [0] * (d+1) # list
        # countArray = np.zeros((d+1), dtype=np.int) # array
        for i in range(len(arr)):
            countArray[arr[i]-min] += 1
        # 3.对统计数组做变形，从第二个元素开始遍历o(m)，累加前面的频数
        for i in range(1, len(countArray)):
            countArray[i] += countArray[i-1]
        # 4.倒序遍历原始数组o(n)，从变形后的统计数组中找到排位，填入结果数组(索引=排位-1), 统计数组对应的频数自减一
        sortedArray = [0] * len(arr)
        for i in range(len(arr)-1, 0, -1):
            sortedArray[countArray[arr[i]-min] - 1] = arr[i]
            countArray[arr[i]-min] -= 1
        return sortedArray

if __name__ == "__main__":
    arr = [95,84,91,98,99,90,99,93,91,92]
    print(arr)
    arr1 = CountSort.countSort(arr)
    print(arr1)
