# 二叉树
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# 从线性的list（前序遍历格式）创建二叉树（非线性的链表）
def createBinaryTree(treeList):
    if len(treeList) == 0 or treeList is None:
        return None
    data = treeList.pop(0) # 返回并删除第一个元素
    node = None
    if data is not None:
        node = TreeNode(data)
        node.leftChild = createBinaryTree(treeList)
        node.rightChild = createBinaryTree(treeList)
    return node

# 深度优先搜索
class DFS:
    # 前序遍历
    @staticmethod
    def preOrderTraveral(node):
        if node is None:
            return
        print(node.data)
        DFS.preOrderTraveral(node.leftChild)
        DFS.preOrderTraveral(node.rightChild)

    # 中序遍历
    @staticmethod
    def inOrderTraveral(node):
        if node is None:
            return
        DFS.inOrderTraveral(node.leftChild)
        print(node.data)
        DFS.inOrderTraveral(node.rightChild)
    
    # 后序遍历
    @staticmethod
    def postOrderTraveral(node):
        if node is None:
            return
        DFS.postOrderTraveral(node.leftChild)
        DFS.postOrderTraveral(node.rightChild)
        print(node.data)


if __name__ == "__main__":
    treeList = [3,2,9,None,None,10,None,None,8,None,4]
    treeNode = createBinaryTree(treeList)
    print("前序遍历：")
    DFS.preOrderTraveral(treeNode)
    print("中序遍历：")
    DFS.inOrderTraveral(treeNode)
    print("后序遍历：")
    DFS.postOrderTraveral(treeNode)