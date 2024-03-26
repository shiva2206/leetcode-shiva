class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for x,y,z in flights:
            adj[x].append((y,z))

        dis = [float('inf')]*n

        deq = deque()
        deq.append((src,0))
        dis[src] = 0
        t = 0
        while deq and t<=k:
            # print()
            # print(deq,dis)
            p = len(deq)
            for _ in range(p):
                x,y = deq.popleft()
                for i,j in adj[x]:
                    m = j + y
                    if m<dis[i]:
                        dis[i] = m
                        deq.append((i,m))
            t+=1            
        return dis[dst] if dis[dst] !=float('inf') else -1
            