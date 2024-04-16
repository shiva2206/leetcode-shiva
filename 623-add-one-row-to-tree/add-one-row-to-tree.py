# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            t = TreeNode(val)
            t.left = root
            return t
        def dfs(t,p):
            if not t:return 
            if p+1 == depth:
                x = t.left
                y = t.right

                t.left = TreeNode(val)
                t.right = TreeNode(val)
                t.left.left = x
                t.right.right = y
                return  
             

            dfs(t.left,p+1)
            dfs(t.right,p+1)
        dfs(root,1)

        return root    


