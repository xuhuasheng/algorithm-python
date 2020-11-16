# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def postOrder(root, res):
            if root is None: return
            postOrder(root.left, res)
            postOrder(root.right, res)
            res.append(root.val)
        
        res = []
        postOrder(root, res)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = []
        prev = None

        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right and node.right != prev:
                
                stack.append(node)
                node = node.right
            else:
                res.append(node.val)
                prev = node
                node = None
        return res