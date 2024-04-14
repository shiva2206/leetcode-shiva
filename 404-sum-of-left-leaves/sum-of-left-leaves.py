# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(t,p):
            if not t:return 0

            if not t.left and not t.right:
                if p: return t.val
                return 0
            return dfs(t.left,True) + dfs(t.right,False)
        return dfs(root,False)