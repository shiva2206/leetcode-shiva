# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]
        def dfs(t):
            if not t:
                return 0
            
            l = max(dfs(t.left),0)
            r = max(dfs(t.right),0)
            res[0] = max(res[0],t.val + l + r)
            return t.val + max(l,r)
        dfs(root)
        return res[0]