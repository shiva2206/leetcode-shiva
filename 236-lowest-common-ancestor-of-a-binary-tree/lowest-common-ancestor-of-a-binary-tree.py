# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(t):
            if not t:return None
            if t.val == p.val or t.val == q.val:
                return t
            left = dfs(t.left)
            right = dfs(t.right)
            if not left:return right
            if not right:return left
            
            return t
        return dfs(root)