# 题目：定义一个函数输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

# 法1;遍历链表，入队列
#       出队列，反向建立链表
# 时间复杂度o(n)
# 空间复杂度o(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 遍历节点，把节点的next指向当前head，然后自己当head
# 时间复杂度o(n)
# 空间复杂度o(1)
def reverseListedNode(head):
    if head is None:
        return None
    node = head
    nextNode = None
    while node.next is not None:
        nextNode = node.next
        node.next = nextNode.next
        nextNode.next = head
        head = nextNode
    return head

# 递归
def reverseList(self, head: ListNode) -> ListNode:
    if head is None: 
        return None
    node = head 
    nextnode = node.next
    if nextnode is None: 
        return node
    newhead = self.reverseList(nextnode)
    nextnode.next = node 
    node.next = None
    return newhead

def buildListedNode(arr):
    if len(arr) == 0:
        return None
    node = Node(arr[-1])
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
    arr = [1,2,3,4,5,6,7,8]
    head = buildListedNode(arr)
    print(outputLinkedNode(head))
    head = reverseListedNode(head)
    print(outputLinkedNode(head))

        