class Solution:
    def minSteps(self, n: int) -> int:
        
        d={}
        def dfs(i,p):
            if i==n:return 0
            if i>=n: return float('inf')

            if (i,p) in d:return d[(i,p)]

            if p==0:
                d[(i,p)]=2+dfs(i+i,i)
            else:    
                d[(i,p)]=1+min(dfs(i+p,p),1+dfs(i+i,i))
            return d[(i,p)]
        return dfs(1,0)  