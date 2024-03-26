# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(t,s):
            if not t:return 0
            
            s = s+str(t.val)
            if not t.left and not t.right:
                return int(s)
            x = dfs(t.left,s)
            y = dfs(t.right,s)

            return x + y 
        return dfs(root,"")    
