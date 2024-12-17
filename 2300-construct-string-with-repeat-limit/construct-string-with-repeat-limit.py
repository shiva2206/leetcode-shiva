class Solution:
    def repeatLimitedString(self, s: str, rep: int) -> str:
        
        d = {}
        for i in s:
            p = ord(i)
            if p not in d:
                d[p]=0
            d[p]+=1
        
        hp = [(-i,d[i]) for i in d]
        heapq.heapify(hp)

        res = ""
        while hp:

            a,val1 = heapq.heappop(hp)
            fir = chr(-a)
            m = min(rep,val1)
            res += fir*m
            val1 = val1 - m
            if val1>0 and hp:
                b,val2 = heapq.heappop(hp)
                sec = chr(-b)
                res += sec
                if val2>1:
                    heapq.heappush(hp,(b,val2-1))
                heapq.heappush(hp,(a,val1))
        return res
