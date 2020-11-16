import numpy as np
# 桶排序：类似于计数排序，用“桶”区间，是线性时间复杂度的排序方法
# 时间复杂度：o(n)
# 空间复杂度：o(n)
class BucketSort:
    @staticmethod
    def bucketSort(arr):
        # 1.遍历原始数组o(n)，求最大值和最小值，计算差值
        # max = np.max(arr)
        # min = np.min(arr)
        max = arr[0]
        min = arr[0]
        for i in arr:
            if i > max:
                max = i
            if i < min:
                min = i
        d = max-min
        # 2.创建桶o(n) 桶的数量=元素的数量
        bucketNum = len(arr)
        bucketList = []
        for i in range(bucketNum):
            bucketList.append([])
        # 3.遍历原始数组o(n)，将每个元素放入桶中
        # 除最后一个桶只包含max外，前面的各个桶的区间=(max-min)/(桶的数量-1)
        for i in range(len(arr)):
            bucketIndex = int((arr[i]-min) / d * (bucketNum-1))
            bucketList[bucketIndex].append(arr[i])
        # 4.对每个桶内部进行排序 所以桶的时间复杂度之和为o(n)
        for bucket in bucketList:
            list.sort(bucket) # 底层采用TimSort 时间复杂度o(nlogn)

        # 5.输出全部元素 o(n)
        sortedArray = [0] * len(arr)
        index = 0
        for b in bucketList:
            for i in b:
                sortedArray[index] = i
                index += 1
        return sortedArray

if __name__ == "__main__":
    arr = [4.12,6.421,0.0023,3.0,2.123,8.123,4.12,10.09]
    print(arr)
    arr1 = BucketSort.bucketSort(arr)
    print(arr1)