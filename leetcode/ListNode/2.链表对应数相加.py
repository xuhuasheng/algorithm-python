# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        node = head
        n1 = l1
        n2 = l2
        carry = 0
        while n1 or n2:
            sum = 0
            if n1:
                sum += n1.val
                n1 = n1.next
            if n2:
                sum += n2.val
                n2 = n2.next
            if carry:
                sum += 1
            node.next = ListNode(sum%10)
            carry = 1 if sum > 9 else 0
            node = node.next
        if carry:
            node.next = ListNode(1)
        return head.next