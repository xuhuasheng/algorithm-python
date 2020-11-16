class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self, data):
        if self.isEmpty():
            return
        return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return
        return self.__list[-1]

# 双栈：
# A栈：数据栈
# B栈：最小栈，栈顶永远是当前最小值
class MinStack:
    def __init__(self):
        self.__stackA = Stack()
        self.__stackB = Stack()
    def isEmpty(self):
        return self.__stackA.isEmpty() and self.__stackB.isEmpty()
    def push(self, data):
        self.__stackA.push(data)
        if self.__stackB.isEmpty() or data < self.__stackB.peek():
            self.__stackB.push(data)
    def pop(self):
        if self.__stackA.isEmpty():
            return
        else:
            data = self.__stackA.pop()
            if data == self.__stackB.peek():
                self.__stackB.pop()
            return data
    def min(self):
        if self.__stackB.isEmpty():
            return
        else:
            return self.__stackB.peek()
    def peek(self):
        if self.__stackA.isEmpty():
            return
        else:
            return self.__stackA.peek()
            
