# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

#  

# 示例 1：

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：

# 输入：lists = []
# 输出：[]
# 示例 3：

# 输入：lists = [[]]
# 输出：[]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        head = ListNode(-1)
        tail = head
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        tail.next = p1 if p1 else p2
        return head.next

    # // 法1
    # // 顺序合并
    # // 时间复杂度：o(k^2 n)
    # // 空间复杂度：o(1)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = None
        for ln in lists:
            ans = self.mergeTwoLists(ans, ln)
        return ans

    # // 法2
    # // 分治合并
    # // 时间复杂度：o(kn * logk)
    # // 空间复杂度：o(logk) 递归用到的栈空间
    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l+r)//2
        return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid+1, r))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists)-1)
