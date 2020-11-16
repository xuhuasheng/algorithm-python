# 给定一个二叉树，原地将它展开为一个单链表。

#  

# 例如，给定二叉树

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrder(root, arr):
            if root is None:
                return
            arr.append(root)
            preOrder(root.left, arr)
            preOrder(root.right, arr)

        arr = []
        preOrder(root, arr)
        for i in range(1, len(arr)):
            pre = arr[i-1]
            cur = arr[i]
            pre.left = None
            pre.right = cur