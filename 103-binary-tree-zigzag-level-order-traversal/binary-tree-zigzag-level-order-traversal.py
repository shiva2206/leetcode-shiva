# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        res =[[root.val]]
        l = [root]
        b = False
        while l:
            p = []
            ans = []
            for i in l:
                if i.left:
                    ans.append(i.left.val)
                    p.append(i.left)
                if i.right:
                    ans.append(i.right.val)
                    p.append(i.right)
            if not ans:return res
            if b:
                res.append(ans+[])
            else:
                res.append(ans[::-1]+[])
            b = not b
            l = p+[]
        return res
        