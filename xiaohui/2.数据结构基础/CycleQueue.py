import numpy as np

class CycleQueue:
    def __init__(self, capacity):
        self.__array = np.zeros(capacity, dtype=np.int)
        self.__front = 0
        self.__rear = 0

    def enQueue(self, data):
        if (self.__rear+1)%self.__array.size == self.__front:
            raise Exception("队列已满")
        self.__array[self.__rear] = data
        self.__rear = (self.__rear+1)%len(self.__array)

    def deQueue(self):
        if self.__front == self.__rear:
            raise Exception("队列已空")
        deQueueData = self.__array[self.__front]
        self.__front = (self.__front+1)%len(self.__array)
        return deQueueData

    def output(self):
        i = self.__front
        while i != self.__rear:
            print(self.__array[i])
            i = (i+1)%self.__array.size


if __name__ == "__main__":
    myQueue = CycleQueue(6)
    myQueue.enQueue(1)
    myQueue.enQueue(3)
    myQueue.enQueue(4)
    myQueue.output()
    myQueue.deQueue()
    myQueue.deQueue()
    myQueue.output()

