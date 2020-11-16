class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 判断链表是否有环
# 时间复杂度：o(n)
# 空间复杂度：o(1)
def isCycle(head):
    # 快慢指针
    p1 = head   # 慢指针 一次走1步
    p2 = head   # 快指针 一次走2步
    # 只要快指针没走到头
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:    # 相遇 被追及
            return True
    return False

# 环长度
def cycleLength(head):
    # 快慢指针
    p1 = head   # 慢指针 一次走1步
    p2 = head   # 快指针 一次走2步
    cnt = 0
    # 只要快指针没走到头
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        cnt += 1     # 前进次数
        if p1 == p2:    # 相遇 被追及
            length = 2*cnt - 1*cnt  # 此时p2比p1多走一圈
            return length   
    return 0

# 入环点
# p1从头出发 p2从首次相遇点出发，速度都是一次走一步
# 当再次相遇，此时为入环点
def cycleEntry(head):
    # 快慢指针
    p1 = head   # 慢指针 一次走1步
    p2 = head   # 快指针 一次走2步
    firstmeet = None
    # 只要快指针没走到头
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:    # 相遇 被追及
            firstmeet = p1
            break
    
    cycleEntry = None
    p1 = head       # 从头出发
    p2 = firstmeet  # 从相遇点出发
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next
        if p1 == p2:
            cycleEntry = p1
            return cycleEntry



if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(7)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(8)
    node7 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4
    print("是否存在环：{}".format(isCycle(node1)))
    print("环长：{}".format(cycleLength(node1)))
    print("入环点：{}".format(cycleEntry(node1)))