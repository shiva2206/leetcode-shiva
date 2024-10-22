# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d ={}
        def dfs(t,i):
            if not t:
                return 
            if i not in d:
                d[i]=0
            d[i] += t.val
            dfs(t.left,i+1)
            dfs(t.right,i+1)
        dfs(root,0)
        if len(d)<k:return -1
        l = []
        print(d)
        for i in d.keys():
            if len(l)<k:
                heapq.heappush(l,d[i])
            elif l[0]<d[i]:
                heapq.heappush(l,d[i])
                heapq.heappop(l)
        return l[0]

