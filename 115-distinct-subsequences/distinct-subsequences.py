class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        d = {}
        def dfs(i,j):
            if j == len(t):return 1
            if i == len(s):return 0
            if(i,j) in d:return d[(i,j)]
            m = 0
            if s[i] == t[j]:
                m = dfs(i+1,j+1)
            m += dfs(i+1,j)
            d[(i,j)] =m
            return m
        d = [[0]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s)+1):
            d[i][len(t)] = 1
        
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                
                m = 0
                if s[i] == t[j]:
                    m = d[i+1][j+1]
                m+= d[i+1][j]
                d[i][j] = m
        return d[0][0]


        