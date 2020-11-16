# 如果一个链表包含环，然后找出环的入口节点

# 1.是否存在环：快慢双指针
# 2.求环长：第一个相遇时，快指针比慢指针走的步数
# 3.入环节点：倒数第k（环长）个节点
            # 也是p1从相遇点出发，p2从head出发，相同速度相遇的点

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 时间复杂度：o(n)
# 时间复杂度：o(1)
def entryNode(head):
    if head is None:
        return None
    p1 = head
    p2 = head
    cnt = 0
    meetintNode = None
    entryNode = None
    isCycle = False
    while p2.next is not None and p2.next.next is not None:
        p2 = p2.next.next
        p1 = p1.next
        cnt += 1
        if p1 == p2:
            isCycle = True
            meetingNode = p1
    if isCycle:
        p2 = meetingNode
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                entryNode = p1
    return entryNode

# 时间复杂度：o(n)
# 空间复杂度：o(n)
def EntryNodeOfLoop(self, pHead):
        # write code here
        #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next
    