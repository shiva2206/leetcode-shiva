class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        d = {}
        pq = []
        for i in hand:
            if i not in d:
                d[i]= 1
                heapq.heappush(pq,i)
            else:
                d[i]+=1
        
        while pq:
            x = pq[0]
            for i in range(groupSize):
                y = x + i
                if y not in d: return False
                d[y]-=1
                if d[y]==0:
                    d.pop(y)
            while pq and pq[0] not in d:
                # d.pop(pq[0])
                heapq.heappop(pq)
        return True

