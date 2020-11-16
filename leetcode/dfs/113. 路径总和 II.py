# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, sum, track, res):
            # 终止条件
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                res.append(track[:])
                return
            
            # 做选择
            if root.left:
                sum -= root.val
                track.append(root.left.val)
                dfs(root.left, sum, track, res)
                # 撤销选择
                sum += root.val
                track.pop()
            if root.right:
                sum -= root.val
                track.append(root.right.val)
                dfs(root.right, sum, track, res)
                # 撤销选择
                sum += root.val
                track.pop()
                
        if not root:
            return []
        track = []
        track.append(root.val)
        res = []
        dfs(root, sum, track, res)
        return res