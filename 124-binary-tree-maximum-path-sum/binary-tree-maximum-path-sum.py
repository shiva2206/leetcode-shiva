# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')
        def dfs(t):
            if not t:return 0

            x = dfs(t.left)
            y = dfs(t.right)
            self.ans = max(self.ans,x + t.val,y + t.val,x + y + t.val,t.val)
            return max(max(x,y) + t.val,t.val)
        dfs(root)
        return self.ans