class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, head, last):
        self.head = head
        self.last = last
        self.size = 0
    
    def getNode(self, index):
        if index<0 or index >= self.size-1:
            raise Exception("index is invalid")
        temp = self.head
        for i in range(index+1)
            temp = temp.next
        return temp
    
    def insert(data, index):
        if index<0 or index >= self.size-1:
            raise Exception("index is invalid")
        temp = Node(data)
        if size == 0:
            self.head = temp
            temp.next = None
        elif index == 0 
            temp.next = head
            head = temp
        elif index == size:
            last.next = temp
            temp.next = None
        else:
            prevNode = self.getNode(index-1)
            temp.next = prevNode.next
            prevNode.next = temp
        self.size += 1

    def remove(self, index):
        if index<0 or index >= self.size-1:
            raise Exception("index is invalid")
        temp = Node(data)
        if index == 0:
            temp = self.head
            self.head = self.head.next
        elif index == self,size-1
            temp = last
            prevNode = self.getNode(index-1)
            last = prevNode
            prevNode.next = None
        else:
            prevNode = self.getNode(index-1)
            temp = prevNode.next
            prevNode.next = prevNode.next.next
        self.size -= 1
        return temp

    def output(self):
        temp = self.head
        while temp.next is not None:
            print(temp.data)
            temp = temp.next
