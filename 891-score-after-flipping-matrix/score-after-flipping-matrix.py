class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        l = [0]*len(grid[0])
        l[0] = len(grid)
        for i in range(len(grid)):
            for j in range(1,len(grid[i])):
                l[j]+= 1 if grid[i][0] == 1 and grid[i][j]==1 or grid[i][0]==0 and grid[i][j]==0 else 0
        ans = 0
        b = 1
        for i in range(len(l)-1,-1,-1):
            ans += max(l[i],len(grid) - l[i]) * b
            b = b*2
            
        return ans