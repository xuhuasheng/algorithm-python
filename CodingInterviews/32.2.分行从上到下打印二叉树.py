import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTreeNode(root):
    if root is None:
        return 
    q = queue.Queue()
    # 当前层要打印的个数
    toBePrinted = 1
    # 下一层要打印的个数
    nextLevelNodes = 0
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.data, end=" ")
        # 每打印一个，当前层减一
        toBePrinted -= 1
        # 子节点如队列 下一层个数+1
        if node.left:
            q.put(node.left)
            nextLevelNodes += 1
        if node.right:
            q.put(node.right)
            nextLevelNodes += 1
        # 当前层打印完毕
        if toBePrinted == 0:
            print()
            toBePrinted = nextLevelNodes
            nextLevelNodes = 0

if __name__ == "__main__":
    node = TreeNode(8)
    node.left = TreeNode(6)
    node.right = TreeNode(10)
    node.left.left = TreeNode(5)
    node.left.right = TreeNode(7)
    node.right.left = TreeNode(9)
    node.right.right = TreeNode(11)
    printTreeNode(node)