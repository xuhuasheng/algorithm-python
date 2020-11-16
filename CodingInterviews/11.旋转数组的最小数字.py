# 把一个数字最开始的若干个元素搬到数组的末尾，称之为数组的旋转
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素
# 例如，[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值是1

# 直接遍历法，时间复杂度o(n)，且没有利用题目条件（旋转后，两端递增，且后端小于前段）
# 比o(n)小的时间复杂度是o(logn),想到二分法

# 二分法的精髓是 2个区间指针，计算中间指针，判断后更新区间指针的一头，缩小区间范围

def getRotatedArrMin(arr):
    left = 0
    right = len(arr)-1
    mid = left
    while arr[left] >= arr[right]:
        # 若二分法最终使得左右指针相邻 则为右指针的指向
        if right - left == 1:
            mid = right
            break
        # 二分
        mid = left + (right - left)//2
        # mid落在左递增区间，则最小值在右边
        if arr[mid] >= arr[left]:
            left = mid
        # mid落在右递增区间，则最小值在左边
        elif arr[mid] <= arr[right]:
            right = mid
    return arr[mid]

if __name__ == "__main__":
    arr = [3,4,5,1,2]
    print(getRotatedArrMin(arr))