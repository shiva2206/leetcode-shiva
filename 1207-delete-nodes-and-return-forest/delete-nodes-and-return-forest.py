# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:return []
        res = []
        head = TreeNode(-1)
        delist = set(to_delete)
        delist.add(-1)
        head.left =root
        def dfs(t):
            if not t:return False
            if dfs(t.left):
                t.left = None
            if dfs(t.right):
                t.right=None


            if t.val in delist:
                if t.left:
                    res.append(t.left)
                if t.right:
                    res.append(t.right)
                return True
            return False    
        dfs(head)
        return res

