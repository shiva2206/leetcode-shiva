class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            
            m= 4
            grid[i][j]=-1
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                x = i+a
                y = j+b
                if x<0 or y<0 or x == len(grid) or y==len(grid[i]):
                    continue
                elif grid[x][y]!=0:
                    m-=1
                if grid[x][y]==1:
                    m+=dfs(x,y)
            return m
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0