# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], tar: int) -> int:
        self.res = 0

        def dfs(t,s):
            if not t:return
            s += t.val
            if s == tar:
                self.res+=1
            x = dfs(t.left,s)
            y = dfs(t.right,s)

        def ggg(t):
            if not t:return 
            dfs(t,0)
            ggg(t.left)
            ggg(t.right)
        ggg(root)
        return self.res


