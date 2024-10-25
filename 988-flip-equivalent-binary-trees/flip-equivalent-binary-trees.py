# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      

      

        def dfs(x,y):
            if not x and not y:return True
            if not x or not y:return False
            if x.val!=y.val:return False
            return dfs(x.left,y.left) and dfs(x.right,y.right) or dfs(x.right,y.left) and dfs(x.left,y.right)
        return dfs(root1,root2)