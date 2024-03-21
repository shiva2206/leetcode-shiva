class Solution:
    def stoneGameIII(self, ston: List[int]) -> str:
        d={}
        q = sum(ston)
        def dfs(i,ali):
            if i==len(ston):return 0
            if (i,ali) in d:return d[(i,ali)]

            d[(i,ali)] = -float('inf') if ali else float('inf')
            s = 0
            for j in range(i,min(i+3,len(ston))):
                if ali:
                    s+=ston[j]
                    d[(i,ali)] = max(d[(i,ali)],s + dfs(j+1,False))
                else:
                    d[(i,ali)] = min(d[(i,ali)], dfs(j+1,True))    
            return d[(i,ali)]
        ans = dfs(0,True)
        # print(d)
        if ans >q-ans:return "Alice"
        elif ans<q-ans: return "Bob"
        return "Tie"        