class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        d ={}
        def dfs(i,j):
            if j == len(t):return 1
            if len(s) - i <len(t)- j or i == len(s) : return 0
            if(i,j) in d: return d[(i,j)]

            d[(i,j)] = dfs(i+1,j)
            if s[i] == t[j]:
                d[(i,j)] += dfs(i+1,j+1)
            return d[(i,j)]
        return dfs(0,0)