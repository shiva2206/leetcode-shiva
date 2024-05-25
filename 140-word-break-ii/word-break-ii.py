class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        l = []
        dic = set(wordDict)
        def dfs(i):
            if i == len(s):
                if l:
                    res.append(" ".join(l))
                return 
            q = ""
            for j in range(i,len(s)):
                q += s[j]
                if q in dic:
                    l.append(q)
                    dfs(j+1)
                    l.pop()
            return 
        dfs(0)
        return res

