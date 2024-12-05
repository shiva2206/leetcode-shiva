class Solution:
    def minInsertions(self, s: str) -> int:
        d = {}
        def dfs(i,j):
            if i >= j:return 0
    
            if (i,j) in d:return d[(i,j)]

            if s[i] == s[j]:
                m = dfs(i+1,j-1)
            else:
                m = 1 + min(dfs(i+1,j),dfs(i,j-1))
            d[(i,j)] =m 
            return m
        return dfs(0,len(s)-1)