# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        # 快指针提前n步
        while n:
            p1 = p1.next
            n -= 1
        if p1 is None:
            # 快指针到头了，即倒数第n个就是第一个元素
            head = head.next
        else:
            # 快指针没到头，此时快慢指针同时移动
            while p1.next:
                p1 = p1.next
                p2 = p2.next
            # 此时慢指针指向要删除元素的前一个元素
            p2.next = p2.next.next
        return head