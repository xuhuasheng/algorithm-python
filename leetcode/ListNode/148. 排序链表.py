# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# 示例 1:

# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        midNode = self.getMidNode(head)
        leftHead = head
        rightHead = midNode.next
        midNode.next = None

        left = self.sortList(leftHead)
        right = self.sortList(rightHead)

        return self.mergeTwoLists(left, right)

    def getMidNode(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        p1, p2 = l1, l2
        head = ListNode(-1)
        node = head
        while p1 and p2:
            if p1.val <= p2.val:
                node.next = p1
                p1 = p1.next
            else:
                node.next = p2
                p2 = p2.next
            node = node.next
        node.next = p1 if p1 else p2
        return head.next