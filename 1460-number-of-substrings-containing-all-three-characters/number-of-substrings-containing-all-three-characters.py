class Solution:
    def numberOfSubstrings(self, s: str) -> int:
       d = {}
       ans = 0
       i=0
       for j in range(len(s)):
            if s[j] not in d:
                d[s[j]]=0
            d[s[j]]+=1

            while len(d) == 3:
                ans += len(s) - j
                d[s[i]]-=1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i+=1
       return ans            

                
            



            
