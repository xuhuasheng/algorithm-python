# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node = head
        while node.next:
            nextnode = node.next
            node.next = nextnode.next
            nextnode.next = head 
            head = nextnode
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