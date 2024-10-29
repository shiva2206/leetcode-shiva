class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        

        d ={}
        def dfs(i,j):
            if j == len(grid[0])-1:return 1
            if (i,j) in d:return d[(i,j)]
            m = 1
            if i-1>=0 and grid[i][j]<grid[i-1][j+1]:
                m = 1 + dfs(i-1,j+1)
            if i+1<len(grid) and grid[i][j]<grid[i+1][j+1]:
                m = max(m,1 + dfs(i+1,j+1))
            if grid[i][j]<grid[i][j+1]:
                m = max(m,1+ dfs(i,j+1))
            d[(i,j)] = m
            return m
        ans = 0
        for i in range(len(grid)):
            ans = max(ans,dfs(i,0))
        return max(ans-1,0)