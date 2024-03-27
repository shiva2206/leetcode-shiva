class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        d = {}
        def dfs(i,j,z):
            if i<0 or i>=n or j<0 or j>=n or z>k:return 0
            if z == k:return 1
            if(i,j,z) in d: return d[(i,j,z)]
            # d[(i,j,z)] = 0
            m = 0
            for g in [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]:
                x  = i + g[0]
                y = j + g[1]
                m += dfs(x,y,z+1) 
            d[(i,j,z)] = m/8
            return d[(i,j,z)]
        return dfs(row,column,0)

                

