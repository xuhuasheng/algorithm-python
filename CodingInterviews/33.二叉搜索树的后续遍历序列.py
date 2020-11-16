# 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。
# 假设输入的数组的任意两个数字都互不相同。
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verifySquenceOfBST(arr):
    if arr is None or len(arr) <= 0:
        return False
    # 后序遍历的最后一个是root
    root = arr[-1]
    # 左子树根节点索引
    leftroot = -1
    # 搜索左子树根节点
    for i in range(len(arr)-1):
        if arr[i] < root:
            leftroot = i
            continue
        break
    # 左子树
    if leftroot < 0:
        leftTree = None
    else:
        leftTree = arr[ : leftroot+1]
    # 右子树
    if leftroot < len(arr)-2:
        rightTree = arr[leftroot+1 : len(arr)-1]
    else:
        rightTree = None
    # 如果有右子树，判断右子树是否会小于根节点
    if rightTree is not None:
        for node in rightTree:
            if node < root:
                return False
    # 递归左子树
    left = True
    if leftTree is not None:
        left = verifySquenceOfBST(leftTree)
    right = True
    # 递归右子树
    if rightTree is not None:
        right = verifySquenceOfBST(rightTree)

    return left and right

if __name__ == "__main__":
    arr = [5,7,6,9,11,10,8] # True
    arr2 = [4,6,7,5] # True
    arr3 = [7,4,6,5] # False
    # print(verifySquenceOfBST(arr))
    print(verifySquenceOfBST(arr2))

