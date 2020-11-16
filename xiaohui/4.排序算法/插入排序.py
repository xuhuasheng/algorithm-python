# 插入排序法
# 时间复杂度o(n^2)
# 空间复杂度o(1)
class InsertSort:
    @staticmethod
    def insertSort(arr):
        # 从第二个元素开始遍历 n-1 轮
        for i in range(1, len(arr)):
            key = arr[i] # 当前排序的元素（待插入）
            j = i-1      # 指向要比较的元素指针
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]   # 单向覆盖
                j -= 1
            arr[j+1] = key

        
if __name__ == "__main__":
    # arr = [3, 4, 2, 1, 5, 6, 7, 8]
    arr = [4,4,6,5,3,2,8,1]
    print(arr)
    InsertSort.insertSort(arr)
    print(arr)