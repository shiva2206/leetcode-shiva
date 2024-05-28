class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        ans = 0

        a = 0

        i = 0
        for j in range(len(s)):
            a =a + abs(ord(s[j]) - ord(t[j]))
            
            while a>maxCost:
                a = a - abs(ord(s[i]) - ord(t[i]))
                i+=1
            ans = max(ans,j-i+1)
        return ans