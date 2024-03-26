# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = "z"*13

        def dfs(t,s):
            s = chr(t.val + 97) + s
            if not t.left and not t.right:
                self.res = min(self.res,s)
                return 
            if t.left:
                dfs(t.left,s)
            if t.right:
                dfs(t.right,s)
        dfs(root,"")            
        return self.res
