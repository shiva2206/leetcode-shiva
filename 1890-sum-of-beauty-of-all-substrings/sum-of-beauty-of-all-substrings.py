class Solution:
    def beautySum(self, s: str) -> int:
        
        
        ans = 0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                if s[j] not in d:
                    d[s[j]]=0
                d[s[j]]+=1
                ans += max(d.values()) - min(d.values()) 
                # print(d)
        return ans