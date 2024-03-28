class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d =defaultdict(int)
        i =0
        ans=0
        m=0
        for j in range(len(s)):
            d[s[j]]+=1
            m = max(m,d[s[j]])

            while k <j-i+1 - m:
                d[s[i]]-=1
                i+=1
            ans = max(ans,j-i+1)
        return ans