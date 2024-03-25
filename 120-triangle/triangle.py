class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        d = {}
        def dfs(i,j):
           if 0<=i<len(tri) and 0<=j<=i :
                if (i,j) in d: return d[(i,j)]
                d[(i,j)] = tri[i][j] + min(dfs(i+1,j),dfs(i+1,j+1))

                return d[(i,j)]
           return 0
        return dfs(0,0)        
