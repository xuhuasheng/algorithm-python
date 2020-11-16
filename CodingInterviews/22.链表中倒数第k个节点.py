# 题目：输入一个链表，输出该链表中倒数第k个节点。
# 为了符合大多数人的习惯,链表的为节点是倒数第1个节点

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 双指针：p1先走k-1步，p2再开始走，保持相距k-1
# 当p1走到尾时，p2刚好在倒数第k个节点
# 时间复杂度o(n)
# 空间复杂度o(1)
def findKthToTail(head, k):
    if head is None or k <= 0:
        return None
    p1 = head
    p2 = head
    cnt = 0
    p2Start = False
    while p1.next is not None:
        cnt += 1
        p1 = p1.next
        if p2Start:
            p2 = p2.next
        if cnt == k-1:
            p2Start = True
    # p1走到链表尾，p1刚好在head
    if cnt == k-1:
        return head
    # p1走到尾，p1还不够启动条件
    if cnt < k-1:
        return None
    return p2

def buildLinkedNode(arr):
    if len(arr) == 0:
        return None
    node = Node(arr[len(arr)-1])
    node.next = None
    head = node
    if len(arr) >= 2:
        for i in range(len(arr)-2, -1, -1):
            node = Node(arr[i])
            node.next = head
            head = node
    return head

def outputLinkedNode(head):
    if head is None:
        return []
    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    head = buildLinkedNode(arr)
    node = findKthToTail(head, 9)
    print(node.data)