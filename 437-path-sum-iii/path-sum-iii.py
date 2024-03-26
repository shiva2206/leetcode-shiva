# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], tar: int) -> int:
        d = defaultdict(int)
        d[0]=1
        self.ans = 0
        def dfs(t,s):
            if not t: return 
            s += t.val
            self.ans += d[s - tar]
            d[s]+=1
            dfs(t.left,s )
            dfs(t.right,s)
            d[s]-=1
        dfs(root,0)
        return self.ans    
