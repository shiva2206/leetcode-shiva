class Solution:
    def isNStraightHand(self, hand: List[int], grp: int) -> bool:
        if len(hand)%grp:return False
        d={}
        for i in hand:
            if i not in d:
                d[i]=0
            d[i]+=1

        l = []
        for i in d:
            l.append((i,d[i]))
        heapq.heapify(l)

        while l:
            z = []
            x,y = heapq.heappop(l)
            if y>1:
                z.append((x,y-1))
            for i in range(grp-1):
                if not l:return False
                a,b = heapq.heappop(l)
                if a-1!=x:return False
                if b>1:
                    z.append((a,b-1))
                x = a
            for j in z:
                heapq.heappush(l,j)    
        return True                    

