class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        d={}
        def dfs(i,w,ali):
            if i==len(piles):return 0
            if (i,w,ali) in d:return d[(i,w,ali)]

        
            d[(i,w,ali)] = 0 if ali else float('inf')
            s = 0
            for j in range(i,min(len(piles),i + 2*w)):
                if ali:
                    s += piles[j]
                    d[(i,w,ali)] = max(d[(i,w,ali)], s + dfs(j+1,max(w,j+1-i),False))
                else:
                    d[(i,w,ali)] = min(d[(i,w,ali)], dfs(j+1,max(w,j+1-i), True))    
            return d[(i,w,ali)]
        return dfs(0,1,True)    