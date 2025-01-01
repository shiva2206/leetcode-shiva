class Solution:
    def maxScore(self, s: str) -> int:
        
        tot = 0
        for i in s:
            tot+= int(i)
        
        ans = 0
        c = 0
        for i in range(len(s)-1):
            c+= int(s[i])
            ans = max(i+1 - c + tot - c,ans)
        return ans
