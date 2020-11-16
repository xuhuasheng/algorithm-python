# 选择排序
# 时间复杂度：o(n2)
# 空间复杂度：o(1)
class SelectSort:
    @staticmethod
    def selectSort(arr):
        # 外层 i [0, n-1)
        for i in range(len(arr) - 1):
            # 内层 j [i+1, n)
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [3, 4, 2, 1, 5, 6, 7, 8]
    print(arr)
    SelectSort.selectSort(arr)
    print(arr)