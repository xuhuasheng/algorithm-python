# 堆排序
# 空间复杂度o(1)
# 时间复杂度o(nLogn)
class HeapSort:
    def __init__(self):
        pass
    
    @staticmethod
    # 升序-构造最大堆
    # 降序-构造最小堆
    def heapSort(arr):
        # 最大堆的下沉
        def downAdjust(arr, parentIndex, length):
            temp = arr[parentIndex]
            childIndex = 2 * parentIndex + 1
            while childIndex < length:
                if childIndex + 1 < length and arr[childIndex+1] > arr[childIndex]:
                    childIndex += 1
                if temp >= arr[childIndex]:
                    break
                arr[parentIndex] = arr[childIndex]
                parentIndex = childIndex
                childIndex = 2 * parentIndex + 1
            arr[parentIndex] = temp
        
        # 1.把无序数字构建最大堆：从最后一个非叶子节点开始，依次做下沉
        for i in range((len(arr)-1-1)//2, -1, -1):
            downAdjust(arr, i, len(arr))
        # 倒序遍历 n-1轮
        for i in range(len(arr)-1, 0, -1):
            # 2.最大堆首尾互换：换至末端的是最大元素-保留
            arr[0], arr[i] = arr[i], arr[0]
            # 3.换至顶端的元素做下沉调整
            downAdjust(arr, 0, i)

if __name__ == "__main__":
    arr = [1,3,2,6,5,7,8,9,10,0]
    print(arr)
    # 升序
    HeapSort.heapSort(arr)
    print(arr)