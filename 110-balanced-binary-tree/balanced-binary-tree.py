# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(t):
            if not t or not self.ans:return 0
            x = dfs(t.left)
            y = dfs(t.right)
            if abs(x - y)>1:
                self.ans = False
                return 0
            return max(x,y)+1
        dfs(root)
        return self.ans
