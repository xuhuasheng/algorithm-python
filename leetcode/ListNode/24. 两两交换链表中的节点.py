# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例 1：


# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：

# 输入：head = []
# 输出：[]
# 示例 3：

# 输入：head = [1]
# 输出：[1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 法1：递归
# time:  o(n)
# space: o(n) 栈空间
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: 
            return None
        if head and head.next is None:
            return head
        nextNode = head.next
        head.next = self.swapPairs(nextNode.next)
        nextNode.next = head
        return nextNode
        
# 法2：非递归
# time:  o(n)
# space: o(1) 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0) # 辅助头节点
        dummyHead.next = head
        prevNode = dummyHead
        while prevNode.next and prevNode.next.next:
            # 待交换的节点
            node1 = prevNode.next
            node2 = prevNode.next.next
            # 提前连接
            prevNode.next = node2
            # 交换
            node1.next = node2.next
            node2.next = node1
            # 交换后，更新前一个节点
            prevNode = node1
        return dummyHead.next

# 法3：拆分、合并
# time:  o(n)
# space: o(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None 
        # 间隔拆分成两条链表
        headA, headB = self.splitListNode(head)
        # 交替合并（先B后A）
        return self.mergeTwoListNode(headA, headB)

    def splitListNode(self, head: ListNode) -> ListNode:
        if not head: return None
        pA, pB = head, head.next
        headA, headB = pA, pB
        while pA.next and pB.next:
            pA.next = pA.next.next
            pA = pA.next
            pB.next = pB.next.next
            pB = pB.next
        # 尾部处理
        if pA and pB and pB.next is None:
            pA.next = None
        return headA, headB

    def mergeTwoListNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None:
            return headB
        if headB is None:
            return headA
        pA, pB = headA, headB
        head = headB
        while pA and pB:
            # 交替合并（先B后A）
            nextNodeB = pB.next
            pB.next = pA
            pB = nextNodeB

            nextNodeA = pA.next
            if pB is not None:
                pA.next = pB
            pA = nextNodeA
        return head


