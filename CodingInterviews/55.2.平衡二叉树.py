class TreeNode:
    def __init__(self, val):
        self. val = val
        self.left = None
        self.right = None

def treeDepth(root):
    if root is None:
        return 0
    return 1 + max(treeDepth(root.left), treeDepth(root.right))

# 递归法-存在重复运算-不推荐
def isBalancedTree(root):
    if root is None:
        return True
    left = treeDepth(root.left)
    right = treeDepth(root.right)
    diff = left - right
    if diff > 1 or diff < -1:
        return False
    return isBalancedTree(root.left) and isBalancedTree(root.right)