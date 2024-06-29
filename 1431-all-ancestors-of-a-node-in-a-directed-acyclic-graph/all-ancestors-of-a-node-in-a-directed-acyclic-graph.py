class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = {}
        for i,j in edges:
            if j not in d:
                d[j]=[]
            if i not in d:
                d[i]=[]
            
            d[j].append(i)
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i]=set()
            if i not in d:return set()
            for k in d[i]:
                dp[i].add(k)
                dp[i]|=dfs(k)
            return dp[i]
        res =[]
        for i in range(n):
            dfs(i)
            
            res.append(list(sorted(dp[i])))
        return res

