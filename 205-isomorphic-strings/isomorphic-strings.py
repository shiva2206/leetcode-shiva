class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        if len(s)!=len(t):return False

        d = {}
        has = set()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:return False
                
            else:
                if t[i] in has:return False
                d[s[i]] = t[i]
                has.add(t[i])
        return True
             
