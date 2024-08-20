class Solution:
    def minSteps(self, n: int) -> int:
        
        d ={}
        def dfs(i,j):
            if i == n:return 0
            if i>n:return float('inf')
            if (i,j) in d:return d[(i,j)]
            d[(i,j)] = float('inf')
            d[(i,j)] = 1 + min(dfs(i,i),dfs(i+j,j))
            return d[(i,j)]
        return dfs(1,0)