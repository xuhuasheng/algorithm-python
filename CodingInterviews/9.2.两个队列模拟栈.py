from queue import Queue

# 两个队列实现栈 
# 互为暂存
# 入栈：初始时，随机入一队列；之后，入非空队列尾
# 出栈：把非空队列前n-1出队再入队到另一空队列，再出队n
class QueueStack:
    def __init__(self):
        self.__qA = Queue()
        self.__qB = Queue()

    def isEmpty(self):
        return self.__qA.empty() and self.__qB.empty()

    def push(self, data):
        if self.isEmpty():
            self.__qA.put(data)
        else:
            if self.__qA.empty():
                self.__qB.put(data)
            else:
                self.__qA.put(data)

    def pop(self):
        if not self.__qA.empty():
            for i in range(self.__qA.qsize-1):
                self.__qB.put(self.__qA.get())
            return self.__qA.get()
        if not self.__qB.empty():
            for i in range(self.__qB.qsize-1):
                self.__qA.put(self.__qB.get())
            return self.__qB.get()

    def peek(self):
        if not self.__qA.empty():
            for i in range(self.__qA.qsize-1):
                self.__qB.put(self.__qA.get())
            peek = self.__qA.get()
            self.__qB.put(peek)
            return peek
        if not self.__qB.empty():
            for i in range(self.__qB.qsize-1):
                self.__qA.put(self.__qB.get())
            peek = self.__qB.get()
            self.__qA.put(peek)
            return peek
