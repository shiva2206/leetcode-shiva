class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        deq =deque()
        tot=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    deq.append((i,j))
                elif grid[i][j]==1:
                    tot+=1
        if tot==0:return 0
        ans = 0
        # print(tot,deq)
        while deq:
            p = len(deq)
            for xx in range(p):
                i,j = deq.popleft()
                for k in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x = i + k[0]
                    y = j + k[1]
                    if 0<=x< len(grid) and 0<=y<len(grid[x]):
                        if grid[x][y]==1:
                            grid[x][y]=2
                            deq.append((x,y))
                            tot-=1
                            if tot==0:return ans+1

            ans+=1
            # print(ans,grid)                
        return -1 if tot!=0 else ans               