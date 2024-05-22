class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l = []
        def dfs(i):
            if i == len(s):
                res.append(l.copy())
                return 
            q = ""
            for k in range(i,len(s)):
                q = q+s[k]
                if q == q[::-1]:
                    l.append(q)
                    dfs(k+1)
                    l.pop()
            return 
        dfs(0)
        return res