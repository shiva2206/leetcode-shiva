# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res =[]

        s = []
        while True:
            if root:
                s.append(root)
                root = root.left
            else:
                if not s:break
                root = s.pop()
                res.append(root.val)
                root = root.right     
        return res
