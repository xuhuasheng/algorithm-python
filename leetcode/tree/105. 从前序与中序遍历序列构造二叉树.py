# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0: return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        rootIdx = inorder.index(rootVal)
        leftNum = rootIdx
        root.left = self.buildTree(preorder[1:leftNum+1], inorder[0:rootIdx])
        root.right = self.buildTree(preorder[leftNum+1:], inorder[rootIdx+1:])
        return root