class Solution:
    def minExtraChar(self, s: str, dic :List[str]) -> int:
        d = {}
        l =set(dic)
        def dfs(i):
            if i == len(s):return 0
            if i in d:return d[i]
            d[i] = 1+ dfs(i+1)
            t = ""
            for j in range(i,len(s)):
                t += s[j]
                if t in l:
                    d[i] = min(d[i],dfs(j+1))
            return d[i]
        return dfs(0)
        