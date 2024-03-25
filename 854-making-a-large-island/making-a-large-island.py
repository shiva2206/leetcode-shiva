class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        d={0:0}
        
        n = 2
        def dfs(i,j,n):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]==1:
                grid[i][j] = n 
                return 1 + dfs(i+1,j,n) + dfs(i-1,j,n) + dfs(i,j+1,n) + dfs(i,j-1,n)
            return 0    
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:    
                    d[n] = dfs(i,j,n)
                    ans = max(ans,d[n])
                    n+=1
        def ret(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]!=0 and grid[i][j] not in vis:
                vis.add(grid[i][j])
                return d[grid[i][j]]

            return 0    
        print(d)    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    vis = set()
                    ans= max(ans,1 + ret(i+1,j) + ret(i-1,j) + ret(i,j+1) + ret(i,j-1))
        return ans                    
