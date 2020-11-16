# 输入一颗二叉树的根节点和一个整数，按打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
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
    def size(self):
        return len(self.__list)
    def get(self, idx):
        if idx < self.size() and idx >=0:
            return self.__list[idx]
        else:
            raise Exception("out of range")

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findPath(root, num):
    if root is None:
        return None
    # 存储路径的栈
    path = Stack()
    sum = 0
    search(root, num, path, sum)


def search(root, num, path, sum):
    sum += root.val
    path.push(root.val)
    isLeaf = root.left is None and root.right is None
    # 如果是叶节点 且 当前路径之和满足要求
    # 则访问并输出栈元素，注意不要弹出栈
    if sum == num and isLeaf:
        pathList = []
        for i in range(path.size()):
            pathList.append(path.get(i))
        print(pathList)  
    else:
        # 如果有左节点，遍历左节点
        if root.left:
            search(root.left, num, path, sum) 
        # 如果有右节点，遍历右节点
        if root.right:
            search(root.right, num, path, sum)  
    # 在返回父节点之前，在路径上删除当前节点,并减去当前节点值
    path.pop()
    sum -= root.val

if __name__ == "__main__":
    node = TreeNode(10)
    node.left = TreeNode(5)
    node.right = TreeNode(12)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(7)
    findPath(node, 22)