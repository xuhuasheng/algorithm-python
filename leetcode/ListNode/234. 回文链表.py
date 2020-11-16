# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1->2
# 输出: false
# 示例 2:

# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time： o(n)
# space: o(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        node = head
        while node:
            res.append(node.val)
            node = node.next 
        return res == res[::-1]

# time： o(n)
# space: o(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None: return True
        # 快慢指针获得中点
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        # 中点为头 进行翻转
        # 1.偶数情况
        #         mid
        # 1->2->3->3->2->1->N
        # 1->2->3->3<-2<-1
        #          |
        #          N
        # 2.奇数情况
        #      mid
        # 1->2->3->2->1->N
        # 1->2->3<-2<-1
        #       |
        #       N
        rightHead = self.reverseList(p1)
        p1, p2 = head, rightHead
        p1_pre = None
        while p1 and p2 and p1 != p2:
            if p1.val != p2.val:
                return False
            p1_pre = p1
            p1 = p1.next
            p2 = p2.next
        # 恢复输入链表
        p1_pre.next = self.reverseList(rightHead)
        return True

    # 翻转链表
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