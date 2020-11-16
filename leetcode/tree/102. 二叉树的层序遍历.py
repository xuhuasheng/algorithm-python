# // 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# //  

# // 示例：
# // 二叉树：[3,9,20,null,null,15,7],

# //     3
# //    / \
# //   9  20
# //     /  \
# //    15   7
# // 返回其层次遍历结果：

# // [
# //   [3],
# //   [9,20],
# //   [15,7]
# // ]

# // 来源：力扣（LeetCode）
# // 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
# // 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        q = []
        node = root
        q.append(node)
        ans = []
        level = []
        curlevelnum = 1
        nextlevenum = 0
        while len(q):
            n = q.pop(0)
            level.append(n.val)
            curlevelnum -= 1
            if n.left:
                q.append(n.left)
                nextlevenum += 1
            if n.right:
                q.append(n.right)
                nextlevenum += 1
            if curlevelnum == 0:
                ans.append(level)
                curlevelnum = nextlevenum
                nextlevenum = 0
                level = []
        return ans

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        q = []
        ans = []
        q.append(root)
        while len(q):
            curlevelnum = len(q)
            level = []
            for _ in range(curlevelnum):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans