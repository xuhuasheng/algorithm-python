# 给定一个二叉树，返回它的 前序 遍历。

#  示例:

# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preOrder(root, res)
        return res

    def preOrder(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
    # 迭代
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res