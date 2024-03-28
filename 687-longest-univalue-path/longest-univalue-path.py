# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
         
        # if not root:return 0
        self.ans = 0
        def dfs(t):
            if not t:return 0
            x = 0
            y = 0
            if t.left:
                if t.left.val == t.val:
                    x =dfs(t.left)
                else:
                    dfs(t.left)
            if t.right:
                if t.right.val == t.val:
                    y= dfs(t.right)
                else:
                    dfs(t.right)
            self.ans = max(self.ans,1+x,1+y,1+x+y) 
            return max(x,y)+1
        dfs(root)
        return max(0,self.ans-1)                           

