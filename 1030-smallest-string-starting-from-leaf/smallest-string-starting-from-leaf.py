# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.ans = "z"*13
        def dfs(t,s):
            if not t:return 
            p = chr(97 + t.val)+s

            if not t.left and not t.right:
                if self.ans>p:
                    self.ans = p
            if t.left:
                dfs(t.left,p)
            if t.right:
                dfs(t.right,p)
        dfs(root,"")
        return self.ans

            