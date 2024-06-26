class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:return grid[0][0]
        pq = [(grid[0][0],0,0)]
        vis = {(0,0):grid[0][0]}
        while pq:
            t,i,j = heapq.heappop(pq)
            for k in [(0,1),(1,0),(0,-1),(-1,0)]:
                x = k[0] + i
                y = k[1] + j
                if 0<=x<len(grid) and 0<=y<len(grid[x]):
                    m = max(t,grid[x][y])
                    if (x,y) not in vis or vis[(x,y)]>m:
                        if x == len(grid)-1 and y == len(grid[i])-1:return m

                        vis[(x,y)] = m
                        heapq.heappush(pq,(m,x,y))
        return                  

        