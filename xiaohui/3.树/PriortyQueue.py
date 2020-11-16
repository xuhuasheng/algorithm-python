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
        if self.heaptype == "maxHeap":
            while childIndex > 0 and temp > arr[parentIndex]:
                arr[childIndex] = arr[parentIndex]
                childIndex = parentIndex
                parentIndex = (childIndex-1) // 2
        # 最小堆上浮
        elif self.heaptype == "minHeap":
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
        if self.heaptype == "maxHeap":
            while (childIndex < len(arr)):
                if childIndex+1 < len(arr) and arr[childIndex+1] > arr[childIndex]:
                    childIndex += 1
                if temp >= arr[childIndex]:
                    break
                arr[parentIndex] = arr[childIndex]
                parentIndex = childIndex
                childIndex = parentIndex*2 + 1
        # 最小堆下沉
        elif self.heaptype == "minHeap":
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

class PriortyQueue:
    def __init__(self, queueType):
        self.arr = []
        self.size = 0
        self.queueType = queueType
        if self.queueType == "max":
            self.heap = BinaryHeap("maxHeap")
        elif self.queueType == "min":
            self.heap = BinaryHeap("minHeap")

    def enQueue(self, data):
        self.arr.append(data)
        self.size += 1
        self.heap.upAdjust(self.arr)

    def deQueue(self):
        if self.size <= 0:
            raise Exception("the queue is empty")
        head = self.arr.pop(0)
        self.arr.insert(0, self.arr[-1])
        self.size -= 1
        self.heap.downAdjust(self.arr, 0)
        return head

if __name__ == "__main__":
    priortyQueue = PriortyQueue("max")
    priortyQueue.enQueue(3)
    priortyQueue.enQueue(10)
    priortyQueue.enQueue(5)
    priortyQueue.enQueue(2)
    priortyQueue.enQueue(7)
    print("出队元素：{}".format(priortyQueue.deQueue()))
    print("出队元素：{}".format(priortyQueue.deQueue()))




