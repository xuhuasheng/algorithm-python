# 编写一个程序，找到两个单链表相交的起始节点。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 双指针交替游走
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        while p1 != p2:
            # 如果 pA 到了末尾，则 pA = headB 继续遍历
            # 如果 pB 到了末尾，则 pB = headA 继续遍历
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

    # 双指针异步游走
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        lenA = 0
        lenB = 0
        # headA的长度
        while p1:
            lenA += 1
            p1 = p1.next
        # headB的长度
        while p2:
            lenB += 1
            p2 = p2.next
        # 长的那一条先走diff步
        p1 = headA
        p2 = headB
        diff = abs(lenA - lenB)
        if lenA > lenB:
            while diff:
                p1 = p1.next
                diff -= 1
        elif lenA < lenB:
            while diff:
                p2 = p2.next
                diff -= 1
        # 再一起走
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None