class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d = set()
        def dfs(i,j):
            if j == len(p):return len(s)==i
            if i == len(s):
                return p[j] == '*' and dfs(i,j+1)
            if (i,j) in d:return False
            d.add((i,j))
            m = False
            if s[i] == p[j]:    
                m = dfs(i+1,j+1)
            elif p[j]=='?':
                m = dfs(i+1,j+1)
            elif p[j] == '*':
                m = dfs(i+1,j) or dfs(i,j+1)
            return m  
        return dfs(0,0)          
