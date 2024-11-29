class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
        l = [(grid[0][0],0,0)]
        if len(grid)==1 and grid[0][1]>1:return -1
        if len(grid[0])==1 and grid[1][0]>1:return -1
        if grid[0][1]>1 and grid[1][0]>1:return -1
        
        while l:
            val,x,y = heapq.heappop(l)
            if x==len(grid)-1 and y== len(grid[0])-1:return val
            print(x,y,val)
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:

                i = a+x
                j = b+y
                if i<0 or j<0 or i==len(grid) or j== len(grid[i]):continue
                if grid[i][j]<0 : continue
                m = val +1
                if m<grid[i][j]:
                    if (grid[i][j]-m)%2==1:
                        m = grid[i][j] +1
                    else:
                        m = grid[i][j]
                grid[i][j] = -float('inf') if m==0 else -m
                heapq.heappush(l,(m,i,j))
        print("joke")
        return -1
                
