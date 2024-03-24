class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        d = defaultdict(list)
        for i,j,z in times:
            d[i].append((z,j)) 

        res = [-1]* (n+1)
        pq = [(0,k)]
        res[k]=0
        m= -1
        while pq:
            # print(pq,res)
            x,y = heapq.heappop(pq)
            
            for i,j in d[y]:
                if res[j]==-1 or x+i<res[j]:
                    heapq.heappush(pq,(x+i,j))
                    res[j] = x+i
                    
        for i in res[1:]:
            if i==-1:return -1
            m = max(m,i)
        return m    