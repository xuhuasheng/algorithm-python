# 无序数组排序后的最大相邻差
# 一般方法：先排序o(nlogn)，再遍历再差值最大o(n)

# 基于计数排序的思想 线性时间复杂度o(n)
def getMaxSortedDistance1(arr):
    # 极差
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    d = max-min
    # 构建频数统计数组
    countArr = [0] * (d+1)
    for i in range(len(arr)):
        countArr[arr[i]-min] += 1
    # 遍历统计数组，找最大连续0的两端索引
    start = 0
    end = len(countArr)-1
    for i in range(1, len(countArr)-1):
        if countArr[i] == 0 and countArr[i-1] == 1:
            start = i-1
        if countArr[i] == 0 and countArr[i+1] == 1:
            end =i+1
    return end-start


# 基于桶排序的思想，每个区间桶只装本区间极值，然后比较桶间极差
# 时间复杂度o(n)
def getMaxSortedDistance2(arr):
    class Bucket():
        def __init__(self):
            self.max = None
            self.min = None
    # 极差
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    d = max-min
    # 创建桶
    bucketNum = len(arr)
    buckets = []
    for i in range(bucketNum):
        buckets.append(Bucket())

    # 遍历原始数组，把区间极值入桶
    for i in arr:
        index = int((i-min) / d * (bucketNum-1))
        if buckets[index].min == None or i < buckets[index].min:
            buckets[index].min = i
        if buckets[index].max == None or i > buckets[index].max:
            buckets[index].max = i

    # 遍历桶，找到最大差值
    leftMax = buckets[0].max
    maxDistance = 0
    for b in buckets:
        if b.min == None:
            continue
        localDistance = b.max-b.min
        if localDistance > maxDistance:
            maxDistance = localDistance
        if b.min-leftMax > maxDistance:
            maxDistance = b.min-leftMax
        leftMax = b.max
    return maxDistance


if __name__ == "__main__":
    arr = [2,6,3,4,5,10,9]
    # print(getMaxSortedDistance1(arr))
    print(getMaxSortedDistance2(arr))