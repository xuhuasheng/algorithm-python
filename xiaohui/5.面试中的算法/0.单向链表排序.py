class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedNodeSort:
    @staticmethod
    def linkedNodeSort2(head, last):
        if head is None or head == last:
            return 
        head, pivotNode = LinkedNodeSort.partition2(head, last)
        LinkedNodeSort.linkedNodeSort2(head, pivotNode)
        LinkedNodeSort.linkedNodeSort2(pivotNode.next, last)
    # 节点的链接不改变，只交换节点的值
    @staticmethod
    def partition2(head, last):
        pivot = head.data
        mark = head
        curNode = head.next
        while curNode is not last:
            if curNode.data < pivot:
                mark = mark.next
                mark.data, curNode.data = curNode.data, mark.data
            curNode = curNode.next
        head.data, mark.data = mark.data, head.data
        return head, mark
# =========================================================
    # 下面是交换节点的做法 但是有问题
    @staticmethod
    def linkedNodeSort1(head, last):
        if head is None or head == last:
            return head
        head, pivotNode = LinkedNodeSort.partition1(head, last)
        head = LinkedNodeSort.linkedNodeSort1(head, pivotNode)
        pivotNode.next = LinkedNodeSort.linkedNodeSort1(pivotNode.next, last)
        return head
    @staticmethod
    def partition1(head, last):
        pivot = head.data
        pivotNode = head
        curNode = head
        while curNode.next is not last:
            if curNode.next.data < pivot:
                nextNode = curNode.next
                nextnextNode = nextNode.next
                nextNode.next = head
                head = nextNode
                curNode.next = nextnextNode
            else: 
                curNode = curNode.next
        return head, pivotNode

    

def getLinkedNode(arr):
    nextNode = None
    for i in range(len(arr)-1, -1, -1):
        node = Node(arr[i])
        if i == len(arr)-1:
            node.next = None
        node.next = nextNode
        nextNode = node
    head = nextNode
    return head

def printLinkedNode(head):
    temp = head
    nodeList = []
    while temp is not None:
        nodeList.append(temp.data)
        temp = temp.next
    print(nodeList)

if __name__ == "__main__":
    arr = [4,7,6,5,3,2,8,1]
    head = getLinkedNode(arr)
    printLinkedNode(head)
    LinkedNodeSort.linkedNodeSort2(head, None)
    print("")
    # print(arr.sort())
    printLinkedNode(head)
    
    

    