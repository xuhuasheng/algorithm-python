# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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