# 删除链表中重复的节点
# 前：1, 2, 3, 3, 4, 4, 5
# 后：1, 2, 5

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteDuplication(head):
    if head is None:
        return
    preNode = None
    node = head
    while node is not None:
        nextNode = node.next
        needDel = False
        if nextNode is not None and nextNode.data == node.data:
            needDel = True
        if not needDel:
            preNode = node
            node = nextNode
        else:
            val = node.data
            while node is not None and node.data == val:
                nextNode = node.next
                node = nextNode
            if preNode is None:
                head = nextNode
            else:
                preNode.next = nextNode
            node = nextNode
    return head

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

if __name__ == "__main__":
    arr = [1,1,2,3,4,4,5,5]
    head = buildLinkedNode(arr)
    head = deleteDuplication(head)
    print(outputLinkedNode(head))


                
 