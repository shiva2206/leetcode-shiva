class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        l = [(1 if grid[0][0]==1 else 0,0,0)]

        while l:
            res,x,y = heapq.heappop(l)

            if x==len(grid)-1 and y==len(grid[0])-1: return res

            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                i = a + x
                j = b + y
                if i<0 or j<0 or i == len(grid) or j==len(grid[0]) :continue
                if grid[i][j]==-1:continue
                m = grid[i][j]
                grid[i][j] = -1
                heapq.heappush(l,(m+res,i,j))
        return -1