class Solution:
    def nearestExit(self, maze: List[List[str]], ent: List[int]) -> int:
        deq = deque()
        deq.append((ent[0],ent[1]))
        t = 0
        vis = set()
        vis.add((ent[0],ent[1]))
        while deq:
            p = len(deq)
            print(deq)
            for _ in range(p):
                x,y = deq.popleft()
                for k in [(0,1),(1,0),(-1,0),(0,-1)]:
                    i = x+ k[0]
                    j = y + k[1]
                    if 0<=i<len(maze) and 0<=j<len(maze[i]) and (i,j) not in vis and maze[i][j]=='.':
                        # print(i,j)
                        if i  == 0 or i == len(maze)-1 or j ==0 or j== len(maze[i])-1:return t+1
                        deq.append((i,j))
                        vis.add((i,j))
            t+=1
        return -1                 