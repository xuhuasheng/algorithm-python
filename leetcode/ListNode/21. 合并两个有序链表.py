# // 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# //  

# // 示例：

# // 输入：1->2->4, 1->3->4
# // 输出：1->1->2->3->4->4

# // // 来源：力扣（LeetCode）
# // // 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# // // 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #     // 非递归
    # // 时间复杂度：o(m+n)
    # // 空间复杂度：o(m+n) 
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is None and l2 is None: return None
        # if l1 and not l2: return l1
        # if l2 and not l1: return l2
        if not l1 or not l2:
            return l1 if l1 else l2
        p1 = l1
        p2 = l2
        head = ListNode(-1)
        node = head
        while p1 and p2:
            if p1.val <= p2.val:
                temp = ListNode(p1.val)
                p1 = p1.next
            else:
                temp = ListNode(p2.val)
                p2 = p2.next
            node.next = temp
            node = temp
        # if p1 is None:
        #     node.next = p2
        # if p2 is None:
        #     node.next = p1 
        node.next = p1 if p1 else p2
        return head.next
    # // 递归
    # // https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
    # // 时间复杂度：o(m+n)
    # // 空间复杂度：o(m+n) (递归调用栈的空间)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
