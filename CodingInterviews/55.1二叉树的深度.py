class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def treeDepth(root):
    if root is None:
        return 0
    return max(treeDepth(root.left), treeDepth(root.right)) + 1

from queue import Queue
def treeDepth2(root):
    if root is None:
        return 0
    q = Queue()
    q.put(root)
    depth = 0
    while not q.empty():
        cur_level_num = q.qsize()
        while sz:
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            cur_level_num -= 1
        depth += 1
    return depth


def minDepth(root):
    if root is None:
        return 0
    if root.left and root.right:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    elif root.left:
        return 1 + minDepth(root.left)
    elif root.right:
        return 1+ minDepth(root.left)
    else:
        return 1

from queue import Queue
def treeDepth2(root):
    if root is None:
        return 0
    q = Queue()
    q.put(root)
    depth = 0
    while not q.empty():
        cur_level_num = q.qsize()
        while sz:
            node = q.get()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            cur_level_num -= 1
        depth += 1
    return depth
    


if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.left.right.left = TreeNode(7)
    node.right.right = TreeNode(6)
    print(treeDepth2(node))