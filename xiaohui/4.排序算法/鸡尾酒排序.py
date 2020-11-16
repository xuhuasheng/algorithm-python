import numpy as np

# 鸡尾酒排序
# 时间复杂度：o(n2)
# 空间复杂度：o(1)
class CocktailSort:
    def __init__(self):
        pass
    @staticmethod
    # 鸡尾酒排序：左右双向冒泡
    def cocktailSort(arr):
        # 外层大循环控制所有排序回合数 n/2
        for i in range(len(arr)//2):
            isSorted = True
            # 奇数轮： 从左往右冒泡 [i, n-1-i)
            for j in range(i, len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSorted = False
            if isSorted:
                break

            isSorted = True
            # 偶数轮： 从右往左冒泡 [n-1-i, i)
            for j in range(len(arr)-1-i, i, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    isSorted = False
            if isSorted:
                break

if __name__ == "__main__":
    arr = np.array([2, 3, 4, 5, 6, 7, 8, 1])
    print("before sorted:{}".format(arr))
    CocktailSort.cocktailSort(arr)
    print("after sorted:{}".format(arr))