# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(t):
            if not t: return [None,None]

            x = dfs(t.left)
            y = dfs(t.right)
            t.left = None
            if not x[0]:
                if not y[0]:return [t,t]
                t.right = y[0]
                return [t,y[1]]
            t.right = x[0]
            if not y[0]:
                return [t,x[1]]
            x[1].right = y[0]
            return [t,y[1]]
        return dfs(root)
            
        dfs(root)  
                    
                