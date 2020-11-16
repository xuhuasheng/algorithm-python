import numpy as np

# 冒泡排序
# 时间复杂度：o(n2)
# 空间复杂度：o(1)
class BubbleSort:
    def __init__(self):
        pass
    # 基本
    @staticmethod
    def bubbleSort_v1(arr):
        # 外层循环 i= 0 : n-1 控制回合轮数n-1 
        for i in range(len(arr)-1):
            # 内层循环 j= 0 : n-1-i 控制冒泡轮数n-1-i
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    # 优化1 针对剩下序列已经是有序 则提前结束排序
    @staticmethod
    def bubbleSort_v2(arr):
        for i in range(len(arr)-1):
            isSorted = True
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  
                    isSorted = False
            if isSorted:
                break  

    @staticmethod   
    # 优化2 针对序列右侧已为有序时 减少不必要的冒泡操作         
    def bubbleSort_v3(arr):
        # 每一轮冒泡排序的边界 也是前一轮最后一次交换的位置
        sortBorder = len(arr) - 1
        for i in range(len(arr)-1):
            # 有序标记 每一轮的初始值都是true
            isSorted = True
            for j in range(sortBorder):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  
                    # 若有交换操作 则说明这一轮排序前是无序的
                    isSorted = False
                    # 更新最后一次交换的位置
                    sortBorder = j
            if isSorted:
                #  说明这一轮没有交换操作 即这一轮排序之前已经是有序的
                #  提前结束大循环 不再下一轮冒泡排序
                break         


if __name__ == "__main__":
    arr = np.array([3, 4, 2, 1, 5, 6, 7, 8])
    print("before sorted:{}".format(arr))
    BubbleSort.bubbleSort_v3(arr)
    print("after sorted:{}".format(arr))