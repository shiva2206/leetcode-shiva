class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]==1:
                grid[i][j]=0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        for i in range(0,len(grid)):
            
            dfs(i,len(grid[i])-1)
            dfs(i,0)
        for j in range(len(grid[0])):
            dfs(0,j)
            dfs(len(grid)-1,j)

        ans =0 
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                ans += grid[i][j]
        return ans                