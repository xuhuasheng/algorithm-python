def findGreatestSimOfSubArray(arr):
    if arr is None or len(arr) <= 0:
        return 0
    curSum = 0
    greatestSum = arr[0]
    for i in arr:
        if curSum <= 0:
            curSum = i
        else:
            curSum += i
        if curSum > greatestSum:
            greatestSum = curSum
    return greatestSum
