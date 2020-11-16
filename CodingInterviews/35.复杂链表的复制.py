

class ComplexListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.sibling = None
# method3
# 时间复杂度o(n)
# 空间复杂度o(1)
def copyComplexListNode3(head):
    if head is None:
        return None
    # 1.复制节点N到N'，把N'接到N的后面
    node = head
    while node:
        cloneNode = ComplexListNode(node.val)
        cloneNode.next = node.next
        node.next = cloneNode
        node = cloneNode.next
    # 2.连接sibling
    node = head
    while node:
        cloneNode = node.next
        if node.sibling:
            # 副本节点的sibling 就是源节点的sibling的next
            cloneNode.sibling = node.sibling.next
        node = node.next.next
    # 3.拆分链表;奇数位置为原始链表；偶数位置为复制链表
    node = head
    cloneHead = head.next
    cloneNode = cloneHead
    while node.next.next:
        node.next = node.next.next
        cloneNode.next = cloneNode.next.next
        node = node.next
        cloneNode = cloneNode.next
    node.next = None
    cloneNode.next = None
    return cloneHead


# method2
# 时间复杂度o(n)
# 空间复杂度o(n)
def copyComplexListNode2(head):
    if head is None:
        return None
    # 1.复制链表主线o(n)
    nodeMap = {}
    node = head
    cloneHead = ComplexListNode(head.val)
    cloneNode = cloneHead
    preCloneNode = cloneHead
    nodeMap[head] = cloneHead
    while node.next:
        cloneNode = ComplexListNode(node.next.val)
        preCloneNode.next = cloneNode
        preCloneNode = cloneNode
        # 建立源节点和副本节点的映射
        nodeMap[node.next] = cloneNode
        node = node.next
    preCloneNode.next = None
    # 2.sibling的复制o(n)
    node = head
    cloneNode = cloneHead
    while node is not None:
        if node.sibling:
            # 通过映射直接连接sibling的副本
            cloneNode.sibling = nodeMap[node.sibling]
        node = node.next
        cloneNode = cloneNode.next
    return cloneHead

# method1
# 时间复杂度：O(n^2)
# 空间复杂度：o(1)
def copyComplexListNode(head):
    if head is None:
        return None
    # 1.复制链表主线o(n)
    node = head
    copiedNode = ComplexListNode(node.val)
    copiedHead = copiedNode
    preNode = copiedHead
    while node.next is not None:
        copiedNode = ComplexListNode(node.next.val)
        preNode.next = copiedNode
        preNode = copiedNode
        node = node.next
    preNode.next = None
    # 2.sibling的复制o(n^2)
    node = head
    copiedNode = copiedHead
    # 从头遍历源链o(n)
    while node is not None:
        # 如果源节点有sibling
        if node.sibling:
            # 从头搜索链表的拷贝o(n)
            tempNode = copiedHead
            while tempNode is not None:
                # 给节点拷贝连接sibling的拷贝
                if tempNode == node.sibling:
                    copiedNode.sibling = tempNode
                    break
        node = node.next
        copiedNode = copiedNode.next
    return copiedHead

    