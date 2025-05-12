# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        ans = []
        
        s = [root]
        while s:
            t = s.pop()
            ans.append(t.val)
            if t.right:
                s.append(t.right)
            if t.left:
                s.append(t.left)
        return ans