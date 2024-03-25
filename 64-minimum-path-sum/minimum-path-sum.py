class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        d={}
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]):
                if i==len(grid)-1 and j == len(grid[i]) -1:return grid[-1][-1]
                if (i,j) in d:return d[(i,j)]

                d[(i,j)] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
                return d[(i,j)]
            return float('inf')
        return dfs(0,0)