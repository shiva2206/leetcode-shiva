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
        return dfs(0,0)