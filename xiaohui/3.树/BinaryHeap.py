# 二叉堆
class BinaryHeap:
    def __init__(self, heaptype):
        self.heaptype = heaptype
    
    # 上浮
    def upAdjust(self, arr):
        childIndex = len(arr)-1
        parentIndex = (childIndex-1) // 2
        temp = arr[childIndex]
        # 最大堆上浮
        if self.heaptype == "max":
            while childIndex > 0 and temp > arr[parentIndex]:
                arr[childIndex] = arr[parentIndex]
                childIndex = parentIndex
                parentIndex = (childIndex-1) // 2
        # 最小堆上浮
        elif self.heaptype == "min":
            while childIndex > 0 and temp < arr[parentIndex]:
                arr[childIndex] = arr[parentIndex]
                childIndex = parentIndex
                parentIndex = (childIndex-1) // 2
        arr[childIndex] = temp

    # 下沉
    def downAdjust(self, arr, parentIndex):
        temp = arr[parentIndex]
        childIndex = parentIndex*2 + 1
        # 最大堆下沉
        if self.heaptype == "max":
            while (childIndex < len(arr)):
                if childIndex+1 < len(arr) and arr[childIndex+1] > arr[childIndex]:
                    childIndex += 1
                if temp >= arr[childIndex]:
                    break
                arr[parentIndex] = arr[childIndex]
                parentIndex = childIndex
                childIndex = parentIndex*2 + 1
        # 最小堆下沉
        elif self.heaptype == "min":
            while (childIndex < len(arr)):
                if childIndex+1 < len(arr) and arr[childIndex+1] < arr[childIndex]:
                    childIndex += 1
                if temp <= arr[childIndex]:
                    break
                arr[parentIndex] = arr[childIndex]
                parentIndex = childIndex
                childIndex = parentIndex*2 + 1
        arr[parentIndex] = temp

    # 构建最大/最小二叉堆
    def buildBinaryHeap(self, arr):
        # 从最后一个非叶子节点开始，依次做下沉
        for i in range((len(arr)-1-1)//2, -1, -1):
            self.downAdjust(arr, i)

if __name__ == "__main__":
    arr = [1,3,2,6,5,7,8,9,10,0]
    print(arr)
    binHeap = BinaryHeap("min")
    binHeap.upAdjust(arr)
    print(arr)

    arr1 = [7,1,3,10,5,2,8,9,6]
    print(arr1)
    binHeap.buildBinaryHeap(arr1)
    print(arr1)


