class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for i,j,k in roads:
            d[i].append((k,j))
            d[j].append((k,i))


        arr = [0]*n
        dis = [float('inf')]*n
        arr[0] = 1
        pq = [(0,0)]
        # heapq.heapify(pq)
        # dis[0] = 0
        mod = 1000000007
        while pq:
            x,y = heapq.heappop(pq)
            if x>dis[y]:continue
            dis[y] = x
            for k in d[y]:
                m = x + k[0]
                if m < dis[k[1]]:
                    heapq.heappush(pq,(m,k[1]))
                    arr[k[1]] = arr[y]
                    dis[k[1]] = m
                elif m == dis[k[1]] :
                    # heapq.heappush(pq,(m,k[1]))
                    arr[k[1]] += arr[y]
        return arr[n-1]%mod              

