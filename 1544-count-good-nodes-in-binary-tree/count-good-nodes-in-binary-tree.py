# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def dfs(t,m):
            if not t:return 0
            if t.val>=m:
                self.res+=1
            dfs(t.left,max(t.val,m))
            dfs(t.right,max(t.val,m))
        dfs(root,root.val)
        return self.res

