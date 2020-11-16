
# 字典序算法：
# 原则：尽量保持高位不变，低位在最小的范围内变换顺序
# 1.从后向前查看逆序区域，找到逆序区的边界
# 2.边界前一位和逆序区中大于它的最小数交换（在逆序区从后往前，只要大于它的即满足交换条件）
# 3.把原来的逆序区转为顺序
def findNearestNumber(num):
    numArr = num2arr(num)
    # 1.从后向前查看逆序区域，找到逆序区的边界
    index = findChangeBorder(numArr)
    # 全为逆序，没有比它大的了
    if index == 0:
        return None
    # 2.边界前一位和逆序区中大于它的最小数交换
    exchangeHead(numArr, index)
    # 3.把原来的逆序区转为顺序
    reverse(numArr, index)
    return arr2num(numArr)

def num2arr(num):
    temp = num
    digtNum = 0
    while temp > 0:
        temp = temp // 10
        digtNum += 1
    arr = []
    div = 10**(digtNum-1)
    temp = num
    while temp > 0:
        digt = temp // div
        temp = temp % div
        div = div // 10
        arr.append(digt)
    return arr

def num2arr2(num):
    arr = []
    temp = num
    while temp:
        digit = temp % 10   # 除10取余得低位
        temp //= 10         # 整除10更新
        arr.insert(0, digit)    # list前插
    return arr

def arr2num(arr):
    num = 0
    multi = 1
    for i in range(len(arr)-1, -1, -1):
        num += arr[i] * multi
        multi = multi * 10
    return num

def arr2num2(arr):
    num = 0
    for i in arr:
        num *= 10
        num += i
    return num

def findChangeBorder(numArr):
    for i in range(len(numArr)-1, 0, -1):
        if numArr[i] > numArr[i-1]:
            return i
    return 0

def exchangeHead(numArr, index):
    head = numArr[index-1]
    for i in range(len(numArr)-1, index-1, -1):
        if numArr[i] > head:
            numArr[i], numArr[index-1] = numArr[index-1], numArr[i]
            break
            
def reverse(numArr, index):
    # 法1
    i = index
    j = len(numArr)-1
    while i<j:
        numArr[i], numArr[j] = numArr[j], numArr[i]
        i += 1
        j -= 1
    
    # 法2
    # tail = numArr[index:]
    # tail.reverse()
    # numArr = numArr[:index] + tail

    return numArr
def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n == 0 or n == 1:
        return None
    border = 0
    for i in range(n-1, 0, -1):
        if nums[i] > nums[i-1]:
            border = i 
    if border!=0:
        head = nums[border-1]
        for i in range(n-1, border-1, -1):
            if nums[i] > head:
                nums[i], nums[border-1] = nums[border-1], nums[i]
                break
        i = border
        j = n-1
    while i<j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
if __name__ == "__main__":
    num = 123
    arr = num2arr2(num)
    i = arr2num2(arr)
    # print(findNearestNumber(num))
    nextPermutation(arr)
    print(arr)