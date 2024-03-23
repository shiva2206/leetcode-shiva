class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        l = []
        pq = deque()
        for i in range(len(mat)):
            l.append([])
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    l[-1].append(0)
                    pq.append((i,j))
                else:
                    l[-1].append(float('inf'))
        g=1            
        while pq:
            t = len(pq)
            for _ in range(t):
                x,y = pq.popleft()

                for k in [(0,1),(1,0),(-1,0),(0,-1)]:
                    i = x +k[0]
                    j = y + k[1]
                    if 0<=i<len(mat) and 0<=j<len(mat[i]):
                        if l[i][j] >g:
                            l[i][j] = g
                            pq.append((i,j))
            g+=1                                        
        return l                