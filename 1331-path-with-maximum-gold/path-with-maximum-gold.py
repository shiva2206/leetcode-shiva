class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        ans = 0
        def dfs(i,j):
            if i<0 or i==len(grid) or j<0 or j==len(grid[i]) or grid[i][j]==0:return 0
            a = grid[i][j]
            grid[i][j] = 0
            t = max(dfs(i,j+1),dfs(i,j-1),dfs(i-1,j),dfs(i+1,j))
            grid[i][j] = a

            return t + a
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]!=0:
                    ans = max(ans, dfs(i,j))
        return ans
            