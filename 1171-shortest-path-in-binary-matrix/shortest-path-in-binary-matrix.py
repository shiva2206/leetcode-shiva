class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:return -1
        vis = set([(0,0)])
        if grid[0][0]==0 and len(grid)==1:return 1
        deq = deque()
        deq.append((0,0))
        t = 1

        while deq:
            p = len(deq)
            for _ in range(p):
                x,y = deq.popleft()
                
                for k in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                    i = x+k[0]
                    j = y + k[1]
                    if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]==0 and (i,j) not in vis:
                        # print(i,j,t)
                        if i == len(grid)-1 and j==len(grid[i])-1:return t+1    
                        vis.add((i,j))
                        deq.append((i,j))
            t+=1
        return -1

