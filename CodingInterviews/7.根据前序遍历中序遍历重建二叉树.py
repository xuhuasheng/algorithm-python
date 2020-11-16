class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def reconstructTree(preOrder, inOrder):
    if len(preOrder) == 0 or len(inOrder) == 0:
        return None
    # 1.前序遍历序列的第一个为根节点
    root = preOrder[0]
    node = TreeNode(root)
    # 2.在中序遍历序列里找根节点的位置
    # 中序遍历的根节点左边为左子树，右边为右子树
    # 以此确定左右子树的所含节点的个数
    midIdx = inOrder.index(preOrder[0])
    leftNum = midIdx
    rightNum = len(inOrder)-1-midIdx
    # 3.给根节点挂左右子树的根节点
    # 左子树
    if leftNum > 0:
        # 从原序列中确定左子树的前中遍历序列 递归 返回左子树根节点
        node.left = reconstructTree(preOrder[1 : leftNum+1], inOrder[0 : midRootIndex])
    # 右子树
    if rightNum > 0:
        # 从原序列中确定右子树的前中遍历序列 递归 返回右子树根节点
        node.right = reconstructTree(preOrder[leftNum+1 :], inOrder[midRootIndex+1 :])
    return node

# 深度优先搜索
class DFS:
    # 前序遍历
    @staticmethod
    def preOrderTraveral(node):
        if node is None:
            return
        print(node.data)
        DFS.preOrderTraveral(node.left)
        DFS.preOrderTraveral(node.right)

if __name__ == "__main__":
    preOrder = [1,2,4,7,3,5,6,8]
    inOrder = [4,7,2,1,5,3,8,6]
    head = reconstructTree(preOrder, inOrder)
    DFS.preOrderTraveral(head)