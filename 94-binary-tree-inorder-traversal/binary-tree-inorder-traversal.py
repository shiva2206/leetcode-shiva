# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        ans = []
        s = [(root,1)]

        while s :
            t,x = s.pop()
            if x == 1:
                s.append((t,x+1))
                if t.left:
                    s.append((t.left,1))

            elif x == 2:
                ans.append(t.val)
                if t.right:
                    s.append((t.right,1))
        return ans
                
                
