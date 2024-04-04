class Solution:
    def maxDepth(self, s: str) -> int:
        l = 0
        m = 0

        for i in s:
            if i=="(":
                l+=1
                m = max(m,l)
            elif i==")":
                l-=1
        return m
                
