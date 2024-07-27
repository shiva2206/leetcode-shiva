class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
         
        d =defaultdict(list)
        for x,y,z in zip(original,changed,cost):
            d[x].append((z,y))
        
        def dijstra(c):
            hp = [(0,c)]
            res ={}
            while hp:
                z,y = heapq.heappop(hp)
                if y in res:continue
                res[y] = z 
                for a,b in d[y]:
                    heapq.heappush(hp,(a+z,b))
            return res
        allcosts = {c : dijstra(c) for c in set(source)}

        res =0
        for i in range(len(source)):
            if source[i]==target[i]: continue
            if source[i] not in allcosts or target[i] not in allcosts[source[i]]: return -1
            res += allcosts[source[i]][target[i]]
        return res
