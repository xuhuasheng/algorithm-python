# 二叉树的层序遍历，队列
import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printBinaryTree(root):
    if root is None:
        return None
    q = queue.Queue()
    prtList = []
    q.put(root)
    while not q.empty():
        node = q.get()
        prtList.append(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return prtList

if __name__ == "__main__": 
    node = TreeNode(8)
    node.left = TreeNode(6)
    node.right = TreeNode(10)
    node.left.left = TreeNode(5)
    node.left.right = TreeNode(7)
    node.right.left = TreeNode(9)
    node.right.right = TreeNode(11)
    print(printBinaryTree(node))