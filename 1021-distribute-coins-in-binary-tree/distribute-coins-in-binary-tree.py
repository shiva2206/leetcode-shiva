# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        
        def dfs(t):
            if not t:return 0
            x = dfs(t.left)
            y = dfs(t.right)
            ans[0]+= abs(t.val -1 + x + y)

            return x + y + t.val -1
        dfs(root)
        return ans[0]