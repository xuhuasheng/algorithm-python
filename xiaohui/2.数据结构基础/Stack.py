# 基于数组list的栈
class Stack1:
    def __init__(self):
        self.__list = []

    def isEmpty(self):
        return self.__list == []

    def push(self, item):
        self.__list.append(item)

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



# 基于链表的栈
class Stack2:
    # 链表节点
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head is None
    
    def push(self, item):
        # 入栈：在链表头部向前接
        node = self.Node(item)
        node.next = self.__head
        self.__head = node

    def pop(self):
        if self.isEmpty():
            return
        else:
            top = self.__head
            self.__head = top.next
            return top.item

    def peek(self):
        return self.__head.item

