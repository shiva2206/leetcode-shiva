class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    m = 4
                    for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                        x = a+ i
                        y = b+j

                        if x<0 or y<0 or x==len(grid) or y == len(grid[i]):
                            continue
                        elif grid[x][y]==1:
                            m-=1
                    ans+=m
        return ans
