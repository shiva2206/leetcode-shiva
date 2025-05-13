class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        l = []
        def dfs(i):
            if i == len(s):
                ans.append(l.copy())
                return 
            q = ""
            for j in range(i,len(s)):
                q += s[j]
                if q == q[::-1]:
                    l.append(q)
                    dfs(j+1)
                    l.pop()
        
        dfs(0)
        return ans

