class Solution:
    def minimumSteps(self, s: str) -> int:
       s = list(s) 
       j = len(s)-1
       ans = 0
       i = j
       while i>=0:

            while j>=0 and s[j]=='1':
                j-=1
            if i>j:
                i = j
                continue
            if s[i] =='1':
                s[i],s[j] = s[j],s[i]
                ans += j-i
                j-=1
            i-=1
       return ans

