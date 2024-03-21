class Solution:
    def stoneGameIII(self, ston: List[int]) -> str:
        d={}
        q = sum(ston)
        def dfs(i):
            if i==len(ston):return 0
            if i in d:return d[i]

            d[i] = -float('inf') 
            s = 0
            for j in range(i,min(i+3,len(ston))):
                # if ali:
                    s+=ston[j]
                    d[i] = max(d[i],s - dfs(j+1))
                # else:
                    # d[(i,ali)] = min(d[(i,ali)], dfs(j+1,True))    
            return d[i]
        ans = dfs(0)
        # print(d)
        if ans >0:return "Alice"
        elif ans<0: return "Bob"
        return "Tie"        