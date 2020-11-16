# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

# 双指针
# 时间复杂度：o(n)
def findNumWithSum(arr, sum):
    left = 0
    right = len(arr)-1
    while left != right:
        tmp = arr[left] + arr[right]
        if tmp == sum:
            return arr[left], arr[right]
        elif tmp < sum:
            left += 1
        else:
            right -= 1
    return None

if __name__ == "__main__":
    arr=[1,2,4,7,11,15]
    sum = 15
    print(findNumWithSum(arr, sum))