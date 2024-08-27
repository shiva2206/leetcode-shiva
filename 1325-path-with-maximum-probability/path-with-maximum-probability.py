class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d={i:[] for i in range(n)}
        
        for i in range(len(edges)):
            d[edges[i][0]].append((edges[i][1],succProb[i]))
            d[edges[i][1]].append((edges[i][0],succProb[i]))

        minheap=[(-1,start)]
        vis=set()
        while minheap:
        
            q,p=heapq.heappop(minheap)
            if p==end:
                return -q   
            vis.add(p)
            for j in d[p]:
                if j[0] in vis:
                    continue
                heapq.heappush(minheap,(q*j[1],j[0]))

        return 0                


        