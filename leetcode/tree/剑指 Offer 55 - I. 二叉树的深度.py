# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

# 例如：

# 给定二叉树 [3,9,20,null,null,15,7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 非递归 BFS 用队列实现
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            curLevelNum = len(q)
            for i in range(curLevelNum):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return depth
