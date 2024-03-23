# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         self.ans = None
         def dfs(t):
            if not t:return False
            
            g = t.val == p.val or q.val==t.val

            x = dfs(t.left)
            y = dfs(t.right)

            if g and (x or y):
                self.ans = t
                return 
            if x and y:
                self.ans = t
                return 

            return x or y or g        
         dfs(root)
         return self.ans