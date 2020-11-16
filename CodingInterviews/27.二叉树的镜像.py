# 题目：实现二叉树的镜像
# 递归
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def mirrorBinaryTree(root):
    if root is None:
        return
    if root.leftChild is None and root.rightChild is None:
        return
    # 交换左右子节点
    root.leftChild, root.rightChild = root.rightChild, root.leftChild
    # 若左子树非空 则递归左子树
    if root.leftChild is not None:
        mirrorBinaryTree(root.leftChild)
    # 若右子树非空 则递归右子树
    if root.rightChild is not None:
        mirrorBinaryTree(root.rightChild)
    