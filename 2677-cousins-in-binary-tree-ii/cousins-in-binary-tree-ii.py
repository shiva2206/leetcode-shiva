# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        que = [root]
        root.val = 0
        while que:
            s = 0
            p = []
            for i in que:
                if i.left:
                    s+=i.left.val
                    p.append(i.left)
                if i.right:
                    s+=i.right.val 
                    p.append(i.right)
            for i in que:
                a = i.left.val if i.left else 0
                a+= i.right.val if i.right else 0
                if i.left:
                    i.left.val = s - a
                if i.right:
                    i.right.val = s-a
            que = p+[]
        return root
                