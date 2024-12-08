# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(t):
            if not t:return 0
            left = dfs(t.left)
            right = dfs(t.right)
            self.ans = max(self.ans,left+right)
            return max(left,right)+1
        dfs(root)
        return self.ans