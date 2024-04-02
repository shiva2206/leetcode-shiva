# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        def dfs(t,a,b):
            if not t: return 

            self.ans = min(self.ans,a - t.val,t.val-b)
            dfs(t.left,t.val,b)
            dfs(t.right,a,t.val)
        dfs(root,float('inf'),-float('inf'))
        return self.ans