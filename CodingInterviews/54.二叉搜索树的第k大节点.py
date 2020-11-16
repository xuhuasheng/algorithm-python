class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        if k <= 0:
            return None
        self.res = None
        self.k = k     
        self.dfs(pRoot)       
        return self.res
     
    def dfs(self,root):
        if not root:
            return None
        self.dfs(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root
            return
        self.dfs(root.right)

def KthNode(pRoot, k):
    # write code here
    if not pRoot or not k :
        return
    res = []

    def midTraversal(node):
        if len(res)>=k or not node :
            return
        midTraversal(node.left)
        res.append(node)
        midTraversal(node.right)
        
    midTraversal(pRoot)
    if len(res)<k:
        return
    return res[k-1]
