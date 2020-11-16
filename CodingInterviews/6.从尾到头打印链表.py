# 先遍历的后输出，反向操作想到栈
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    def size(self):
        return len(self.__list)

# 栈实现
def printListReverse(head:Node):
    stack = Stack()
    node = head
    arr = []
    while node is not None:
        stack.push(node.data)
        node = node.next
    while not stack.isEmpty():
        arr.append(stack.pop())
    return arr

# 递归实现
def printListReverse2(head:Node):
    if head is not None:
        if head.next is not None:
            printListReverse2(head.next)
        print(head.data)

def buildLinkedNode(arr):
    if len(arr) == 0:
        return None
    # 头节点
    head = Node(arr[0])
    preNode = head
    if len(arr) > 1:
        for i in range(1, len(arr)):
            node = Node(arr[i])
            preNode.next = node
            preNode = node
    preNode.next = None
    return head

if __name__ == "__main__":
    arr = [1,2,3,4]
    head = buildLinkedNode(arr)
    print(printListReverse(head))