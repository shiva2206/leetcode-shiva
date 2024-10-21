class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        d=set()
        def dfs(i):
            if i==len(s):return 0
            q = ""
            m = 0
            for j in range(i,len(s)):
                q = q+s[j]
                if q not in d:
                    d.add(q)
                    m = max(m,1+dfs(j+1))
                    d.remove(q)
            return m 
        return dfs(0)