# 栈模拟实现队列
# AB栈
# A栈：入队：入A栈  时间复杂度o(1)
# B栈：出队：先依次出A栈并依次入B栈，再出B的栈顶   
#       时间复杂度大部分情况是o(1),少数情况是o(n),均摊时间复杂度为o(1)
class StackQueue:
    def __init__(self):
        self.__stackA = Stack()
        self.__stackB = Stack()

    def isEmpty(self):
        return self.__stackA.isEmpty() and self.__stackB.isEmpty()
    
    def enQueue(self, data):
        self.__stackA.push(data)
    
    def deQueue(self):
        if self.isEmpty():
            raise Exception("队列已空")
        else:
            if self.__stackB.isEmpty():
                while not self.__stackA.isEmpty():
                    self.__stackB.push(self.__stackA.pop()) 
            return self.__stackB.pop()

class Stack():
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

if __name__ == "__main__":
    stackQueue = StackQueue()
    stackQueue.enQueue(1)
    stackQueue.enQueue(2)
    stackQueue.enQueue(3)
    print(stackQueue.deQueue())
    print(stackQueue.deQueue())
    stackQueue.enQueue(4)
    print(stackQueue.deQueue())
    print(stackQueue.deQueue())