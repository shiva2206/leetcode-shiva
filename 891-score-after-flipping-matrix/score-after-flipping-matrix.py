class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        a = 2**(len(grid[0])-1) * len(grid)
        ans = 0 
        for j in range(1,len(grid[0])):
            c = 0
            ans <<=1
            for i in range(len(grid)):
                c +=1 if grid[i][j] == grid[i][0] else 0
            ans += max(c,len(grid)-c)
        return a + ans