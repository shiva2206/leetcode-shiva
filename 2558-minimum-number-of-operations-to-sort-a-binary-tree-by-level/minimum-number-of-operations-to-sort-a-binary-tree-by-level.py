# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        que = [root]
        ans = 0
        while que:
            p = []
            v = []
            for i in que:
                if i.left:
                    p.append(i.left)
                    v.append(i.left.val)
                if i.right:
                    p.append(i.right)
                    v.append(i.right.val)
            if p:
                z = v+[]
                v.sort()
                d = {}
                for i,j in enumerate(p):
                    d[j.val] = i
                c = 0
                for i in range(len(p)):
                    if i != d[v[i]]:
                        t = d[v[i]]
                        d[v[i]],d[z[i]] = i,d[v[i]]
                        z[t],z[i] = z[i],z[t]
                        c+=1
                    
                print(c)
                ans+=c
            que = p+[]
        return ans