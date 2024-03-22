class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        j = 0
        ans = 0
        for i in g:
            while j<len(s) and s[j]<i:
                j+=1
            if j == len(s):return ans
            j+=1
            ans+=1
        return ans        