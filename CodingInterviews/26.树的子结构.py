# 题目：输入两颗二叉树a和b，判断b是不是a的子结构。

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def hasSubtree(root1, root2):
    res = False
    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            res = doesTree1HaveTree2(root1, root2)
        if res is not True:
            res = hasSubtree(root1.leftChild, root2)
        if res is not True:
            res = hasSubtree(root1.rightChild, root2)
    return res

def doesTree1HaveTree2(root1, root2):
    # root2已经没有子节点了，root2遍历完毕
    if root2 is None:
        return True
    # root2没有遍历完毕，但root1没有子节点了，说明两个子结构不同
    if root1 is None:
        return False
    # 两个子结构的根节点不同，直接否决
    if root1.data != root2.data:
        return False
    # 在上面没有做出判断之后，递归两个的左子树和右子数
    return doesTree1HaveTree2(root1.leftChild, root2.leftChild) and doesTree1HaveTree2(root1.rightChild, root2.rightChild)