# 序列化和反序列化二叉树
# 前序遍历
# 遇到空节点用$表示

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 二叉树序列化
# 输入：二叉树
# 输出：二叉树前序遍历的字符串
def serialize(root):
    arr = []
    def DFS(root, arr):
        if root is None:
            arr.append('#')
            return
        arr.append(str(root.val))
        serialize(root.left, arr)
        serialize(root.right, arr)
    DFS(root, arr)
    return ','.join(arr)


# 二叉树反序列化
# 输入：二叉树前序遍历的字符串
# 输出：二叉树
def deserialize(s):
    arr = s.split(',')
    def DFS(arr):
        if len(arr) <= 0:
            return None
        val = arr.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = deserialize(arr)
            root.right = deserialize(arr)
        return root
    return DFS(arr)