class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        j = 0
        for i in range(len(s)):
            if j == len(t):
                return 0
            if s[i]==t[j]:
                j+=1
        return len(t) - j