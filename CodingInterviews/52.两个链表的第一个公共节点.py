# 输入两个链表，找出它们的第一个公共结点。

# 两个指针一直转
# 时间复杂度o(m+n)
def FindFirstCommonNode3(pHead1 , pHead2 ):
    if pHead1 is None or pHead2 is None:
        return None

    p1 = pHead1
    p2 = pHead2
    # 两个指针在各自的链表上循环跑，直到相等
    while p1 != p2:
        p1 = p1.next if p1 is not None else pHead2           
        p2 = p2.next if p2 is not None else pHead1
    return p1

# 两个辅助栈
# 时间复杂度o(m+n)
# 空间复杂度o(m+n)
def findFirstCommonNode(root1:Node, root2:Node):
    if not root1 or not root2:
        return None
    s1 = Stack()
    s2 = Stack()
    node = root1
    while node:
        s1.push(node.val)
        node = node.next
    node = root2
    while node:
        s2.push(node.val)
        node = node.next
    firstComNode = None
    while not s1.isEmpty() or s2.isEmpty():
        if s1.peek() == s2.peek():
            firstComNode = s1.peek()
            s1.pop()
            s2.pop()
        else:
            break
    return firstComNode

# 双指针法
# 时间复杂度o(m+n)
# 空间复杂度o(1)
def findFirstCommonNode2(root1:Node, root2:Node):
    len1, len2 = 0, 0
    node = root1
    while node:
        len1 += 1
        node = node.next
    node = root2
    while node:
        len2 += 1
        node = node.next
    d = len1 - len2 if len1 > len2 else len2 - len1
    p1 = root1
    p2 = root2
    if len1 > len2:
        for i in range(d):
            p1 = p1.next
    else:
        for i in range(d):
            p2 = p2.next
    while p1 and p2:
        if p1.val == p2.val:
            return p1.val
        p1 = p1.next
        p2 = p2.next
    return None

# 递归法建立链表
def buildListNode(arr):
    if len(arr) == 0:
        return None
    root = Node(arr.pop(0))
    root.next = buildListNode(arr)
    return root

def buildListNode2(arr):
    root = Node(arr[0])
    preNode = root
    for i in range(1, len(arr)):
        node = Node(arr[i])
        preNode.next = node
        preNode = node
    preNode.next = None
    return root

def printListNode(root):
    res = []
    node = root
    while node:
        res.append(node.val)
        node = node.next
    print(res)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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
        return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return
        return self.__list[-1]

if __name__ == "__main__":
    arr1 = [1,2,3,6,7]
    arr2 = [4,5,6,7]
    root1 = buildListNode2(arr1)
    printListNode(root1)
    root2 = buildListNode2(arr2)
    printListNode(root2)
    print(findFirstCommonNode2(root1, root2))