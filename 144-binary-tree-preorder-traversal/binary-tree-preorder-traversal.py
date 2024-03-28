# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res = []

        s = [root]
        while s:
            x = s.pop()
            res.append(x.val)
            if x.right:
                s.append(x.right)
            if x.left:
                s.append(x.left)
        return res