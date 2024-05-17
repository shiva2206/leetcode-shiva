# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(t):
            if not t:return None
            x = dfs(t.left)
            y = dfs(t.right)

            if not x and not y and t.val == target: return None
            t.left = x 
            t.right = y
            return t
        return dfs(root)
