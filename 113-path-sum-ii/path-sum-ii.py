# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], tar: int) -> List[List[int]]:
        res =[]
        l = []
        def dfs(t,s):
            if not t:
                return 
            l.append(t.val) 
            s+=t.val
            if not t.left and not t.right:
                if s == tar:
                    res.append(l.copy())
                l.pop()
                return 
            if t.left:
                dfs(t.left,s)
            if t.right:    
                dfs(t.right,s)
            l.pop()
            return 
        dfs(root,0)
        return res    