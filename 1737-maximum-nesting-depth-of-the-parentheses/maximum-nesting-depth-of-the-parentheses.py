class Solution:
    def maxDepth(self, s: str) -> int:
        l = []
        m = 0

        for i in s:
            if i=="(":
                l.append(i)
                m = max(m,len(l))
            elif i==")":
                l.pop()
        return m
                
