class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def dfs(i,j,n,tar):
            if tar == len(grid)*len(grid[0]) - 1:return True
            
            for k in [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]:
                x = k[0] + i
                y = k[1] + j

                if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):continue
                q = (n+1)%(len(grid)*len(grid[0]))
                if grid[x][y] == q:
                    return dfs(x,y,q,tar+1)
            return False
        return dfs(0,0,grid[0][0],0)    
