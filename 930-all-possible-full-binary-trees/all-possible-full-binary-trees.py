# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0:return []

        d = {}
        def dfs(i):
            if i==0:return []
            if i==1:return [TreeNode(0)]
            if i in d:return d[i]
            d[i] =[]
         
            for j in range(1,i,2):
                left = dfs(j)
                right = dfs(i-j-1)
                for x in left:
                    for y in right:
                        t = TreeNode(0)
                        t.left = x
                        t.right = y
                        d[i].append(t)
            return d[i]
        return dfs(n)