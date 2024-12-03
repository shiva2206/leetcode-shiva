# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
        
        def allequal(x,y):
            if not x and not y:return True
            if not x or not y or x.val!=y.val:return False
            return allequal(x.left,y.left) and allequal(x.right,y.right)
        self.head =y
        def dfs(x,y):
            if not x and not y:return True
            if not x or not y:return False
            if x.val==y.val: 
                if allequal(x.left,y.left) and allequal(x.right,y.right):return True
            return dfs(x.left,self.head) or dfs(x.right,self.head)
        return dfs(x,y)