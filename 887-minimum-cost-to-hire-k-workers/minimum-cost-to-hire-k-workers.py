class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        pair=[]
        for i in range(len(wage)):
            pair.append([wage[i]/quality[i],quality[i]])

        pair.sort()

        maxh=[]
        m=float('inf')
        s=0
        for i in range(len(wage)):
            s=s+pair[i][1]
            heapq.heappush(maxh,-pair[i][1])
            if i<k-1:continue
            m=min(m,s*pair[i][0])
            s=s+heapq.heappop(maxh)
        return m        
        