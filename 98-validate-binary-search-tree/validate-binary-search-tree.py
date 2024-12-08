# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(t,left,right):
            if not t:return True
            return left<t.val<right and dfs(t.left,left,t.val) and dfs(t.right,t.val,right)
        return dfs(root,-float('inf'),float('inf'))