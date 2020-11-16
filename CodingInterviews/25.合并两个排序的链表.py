# 题目：输入两个递增排序的链表合并这两个链表，并使新链表中的节点仍然是递增排序的。
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedNode(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    # 确定头节点 以及p1p2
    if head1.data <= head2.data:
        head = Node(head1.data)
        p1 = head1.next
        p2 = head2
    else:
        head = Node(head2.data)
        p1 = head1
        p2 = head2.next
    # 前节点初始化为头节点
    preNode = head
    # 只要两链表都没到尾
    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            node = Node(p1.data)
            p1 = p1.next
        else:
            node = Node(p2.data)
            p2 = p2.next
        preNode.next = node
        preNode = node
    # 当链表1到尾
    if p1 is None:
        # 链表2继续
        while p2 is not None:
            node = Node(p2.data)
            p2 = p2.next
            preNode.next = node
            preNode = node
    # 当链表2到尾
    if p2 is None:
        # 链表1继续
        while p1 is not None:
            node = Node(p1.data)
            p1 = p1.next
            preNode.next = node
            preNode = node
    # 记住尾节点加None
    preNode.next = None
    return head

# 正序建立链表
def buildLinkedNode(arr):
    if len(arr) == 0:
        return None
    # 头节点
    head = Node(arr[0])
    preNode = head
    if len(arr) > 1:
        for i in range(1, len(arr)):
            node = Node(arr[i])
            preNode.next = node
            preNode = node
    preNode.next = None
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
    arr1 = [1,3,5,6,7,15]
    arr2 = [4,5,6,8,9]
    head1 = buildLinkedNode(arr1)
    head2 = buildLinkedNode(arr2)
    print(outputLinkedNode(head1))
    print(outputLinkedNode(head2))
    head3 = mergeSortedNode(head1, head2)
    print(outputLinkedNode(head3))
