# 在o(1)时间内删除链表节点
# 给定单向链表的头指针和一个节点指针，在o(1)时间内删除该节点指针


# 删除单向链表中的节点node的两种方法：
# 1.从头遍历链表o(n)，找该节点node的前一个节点preNode, 让preNode.next = preNode.next.next
# 2.不用从头遍历o(1),直接找该节点node的下一个节点nextNode，让node.data = nextNode.data, node.next = nextNode.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 平均时间复杂度o(1)
def deleteNode(head, toBeDeleted):
    if head is None or toBeDeleted is None:
        return
    # 时间复杂度o(1)
    if toBeDeleted.next is not None:
        nextNode = toBeDeleted.next
        toBeDeleted.data = nextNode.data
        toBeDeleted.next = nextNode.next 
    elif head == toBeDeleted:
        head = None
    # 链表中有多个节点，删除为节点，这时需要从头遍历o(n)
    else:
        temp = head
        while temp.next is not toBeDeleted:
            temp = temp.next
        temp.next = None

def buildLinkedNode(arr):
    if len(arr) == 0:
        return None
    node = Node(arr[len(arr)-1])
    node.next = None
    head = node
    if len(arr) >= 2:
        for i in range(len(arr)-2, -1, -1):
            node = Node(arr[i])
            node.next = head
            head = node
    return head

def outputLinkedNode(head):
    if head is None:
        return []
    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    return arr

def getNode(head, index):
    if head is None or index < 0:
        return None
    if index == 0:
        return head
    temp = head
    for i in range(index):
        if temp.next is None:
            return None
        temp = temp.next
    return temp

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    head = buildLinkedNode(arr)
    print(outputLinkedNode(head))
    print(getNode(head, 2).data)
    deleteNode(head, getNode(head, 2))
    print(outputLinkedNode(head))

    
    