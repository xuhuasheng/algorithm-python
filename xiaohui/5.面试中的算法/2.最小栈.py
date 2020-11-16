# 基于list实现的栈
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

# 最小栈
# A栈：数据栈
# B栈：栈顶永远是当前最小数据
class MinStack:
    def __init__(self):
        self.__stackA = Stack()
        self.__stackB = Stack()

    def isEmpty(self):
        return self.__stackA.isEmpty()

    def push(self, data):
        self.__stackA.push(data)
        if self.__stackB.isEmpty() or data <= self.__stackB.peek():
            self.__stackB.push(data)
    
    def pop(self):
        if self.__stackA.pop() == self.__stackB.peek():
            self.__stackB.pop()
        return self.__stackA.pop()

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.__list[-1]

    def getMin(self):
        if self.__stackB.isEmpty():
            return
        else:
            return self.__stackB.peek()

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(4)
    minStack.push(9)
    minStack.push(7)
    minStack.push(3)
    minStack.push(8)
    minStack.push(5)
    print(minStack.getMin())
    minStack.pop()
    minStack.pop()
    minStack.pop()
    print(minStack.getMin())
