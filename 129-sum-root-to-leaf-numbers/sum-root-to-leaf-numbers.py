# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(t,p):
            if not t:
                return 0
            if not t.left and not t.right:
                return p*10 + t.val
            m = 0    
            if t.left:    
                m = dfs(t.left,p*10 + t.val)    
            if t.right:
                m+=dfs(t.right,p*10 +t.val)
            return m
        return dfs(root,0)
