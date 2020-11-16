import queue

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


class BFS:
    @staticmethod
    def levelOrderTraversal(root):
        q = queue.Queue()
        node = root
        q.put(node)
        while q.empty() is not True:
            n = q.get()
            print(n.data)
            if n.leftChild is not None:
                q.put(n.leftChild)
            if n.rightChild is not None:
                q.put(n.rightChild)

if __name__ == "__main__":
    treeList = [3,2,9,None,None,10,None,None,8,None,4]
    treeNode = createBinaryTree(treeList)
    print("层序遍历：")
    BFS.levelOrderTraversal(treeNode)
