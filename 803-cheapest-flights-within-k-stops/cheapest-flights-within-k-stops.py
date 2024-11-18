class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        d = defaultdict(list)
        
        q= deque()
        for i,j,p in flights:
            d[i].append((p,j))
            if i == src:
                q.append((p,j))
        

        l = [float('inf')]*n
        l[src] = 0
        for i in range(k+1):
            w = len(q)
            for j in range(w):
                price,stop = q.popleft()
                if l[stop]>price:
                    l[stop] = price
                    for p,node in d[stop]:
                        q.append((price + p,node))
        print(l)
        return -1 if l[dst] == float('inf') else l[dst]

    

