# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(t1,t2):
            if not t1:return t2==None
            if not t2:return t1==None
            return t1.val == t2.val and dfs(t1.left,t2.right) and dfs(t1.right,t2.left)
        return dfs(root,root)
