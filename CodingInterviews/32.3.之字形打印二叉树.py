# 题目:请实现一个函数安照之字形顺序打印二叉树，即第一行按照从左往右打印，
# 第二行按照从右往左打印，第三行再从左往右打印，以此类推

# 轮流反向打印：用两个栈，分别存储奇偶层
def printTreeNode(root):
    if root is None:
        return
    stackA = Stack()
    stackB = Stack()
    level = [stackA, stackB]
    current = 0
    next = 1
    level[current].push(root)
    while not stackA.isEmpty() or not stackB.isEmpty():
        node = level[current].pop()
        print(node.data, end=" ")
        if current == 0:
            if node.left:
                level[next].push(node.left)
            if node.right:
                level[next].push(node.right)
        else:
            if node.right:
                level[next].push(node.right)
            if node.left:
                level[next].push(node.left)
        # 一层打印完
        if level[current].isEmpty():
            print()
            # current 和 next 互换
            current = 1 - current
            next = 1 - next

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.__list[-1]

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

if __name__ == "__main__": 
    node = TreeNode(8)
    node.left = TreeNode(6)
    node.right = TreeNode(10)
    node.left.left = TreeNode(5)
    node.left.right = TreeNode(7)
    node.right.left = TreeNode(9)
    node.right.right = TreeNode(11)
    printTreeNode(node)