# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(t):
            if not t:
                return 
            dfs(t.left)
            dfs(t.right)
            ans.append(t.val)
        dfs(root)
        return ans