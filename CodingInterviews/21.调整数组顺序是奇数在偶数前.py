# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序。
# 使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# 单边循环法
# 时间复杂度o(n)
# 空间复杂度o(1)
def reorderOddEven1(arr):
    border = None   #指向奇数末尾边界
    occurOdd = False
    for i in range(len(arr)):
        # 偶数
        if (arr[i] & 0x1) == 0:
            continue
        # 奇数
        else:
            # 第一次出现奇数
            if not occurOdd:
                arr[0], arr[i] = arr[i], arr[0]
                border = 0
                occurOdd = True
            # 出现过奇数
            else:
                border += 1 # 此时指向边界后第一个偶数
                arr[border], arr[i] = arr[i], arr[border]

# 双边循环法
# 时间复杂度o(n)
# 空间复杂度o(1)
def reorderOddEven2(arr):
    left = 0
    right = len(arr)-1
    while left != right:
        while left < right and (arr[right] & 0x1) == 0:
            right -= 1
        while left < right and (arr[left] & 0x1) == 1:
            left += 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    reorderOddEven2(arr)
    print(arr)
        
