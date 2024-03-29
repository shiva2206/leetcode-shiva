# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d=defaultdict(lambda : defaultdict(list))

        def dfs(t,x,y):
            if not t:return 
            d[x][y].append(t.val)
            dfs(t.left,x-1,y+1)
            dfs(t.right,x+1,y+1)
        dfs(root,0,0)
        res = []
        for i in d:
            for j in d[i]:
                d[i][j].sort()

        l = list(d.keys())
        l.sort()
        for i in l:
            p = list(d[i].keys())
            p.sort()
            ans = []
            for j in p:
                ans.extend(d[i][j])

            res.append(ans)
        return res

