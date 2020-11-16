# 数组中的逆序对
# 题目描述
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

def inversePairs(data):
    # 声明全局变量 并初始化0
    global cnt 
    cnt = 0
    mergeSort(data)
    return cnt % 1000000007

# 归并排序，在排序过程中统计逆序对
# 时间复杂度：o(nlogn)
# 空间复杂度：o(n)
def mergeSort(arr):
    # 申明全局变量 作用域涵盖所有递归
    global cnt
    # 递归的终点条件 只有一个元素 start==end
    if len(arr) <= 1:
        return arr
    # 归：递归分治排序
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    # 并：合并排序好的两部分
    pL, pR = 0, 0
    res = []
    while pL < len(left) and pR < len(right):
        if left[pL] < right[pR]:
            res.append(left[pL])
            pL += 1
        else:
            # 存在逆序对
            res.append(right[pR])
            pR += 1
            cnt += len(left)- pL
    res += right[pR:]
    res += left[pL:]
    return res

if __name__ == "__main__":
    arr = [7,8,6,4]
    print(inversePairs(arr))