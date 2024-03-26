class Solution:
    def maxPerformance(self, n: int, speed: List[int], eff: List[int], k: int) -> int:
        l = []
        for i in range(n):
            l.append((speed[i],eff[i]))
        l.sort(key = lambda x : -x[1])    
        pq = []
        m = 0
        s = 0
        for i in range(n):
            if len(pq) == k:
                s -= heapq.heappop(pq)
            s += l[i][0]
            m = max(m,s*l[i][1])
            heapq.heappush(pq,l[i][0]) 
        return m %(1000000007)      
