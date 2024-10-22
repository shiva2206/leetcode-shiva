# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        l = []
        que = [root]
        while que:
            a = 0
            p = []
            for i in que:
                if i.left:
                    p.append(i.left)
                if i.right:
                    p.append(i.right)
                a+=i.val
            que = p+[]
      
            if len(l)<k:
                heapq.heappush(l,a)
            elif l[0]<a:
                heapq.heappush(l,a)
                heapq.heappop(l)
        return -1 if len(l)<k else l[0]

