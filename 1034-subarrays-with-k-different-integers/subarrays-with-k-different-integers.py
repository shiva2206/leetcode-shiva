class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
       

        def dfs(t):
            d ={}
            i= 0 
            ans = 0
        
            for j in range(len(s)):
                d[s[j]] = d.get(s[j],0) +1
                while len(d)> t:
                    d[s[i]]-=1
                    if d[s[i]] == 0:
                        d.pop(s[i])
                    i+=1
                ans += j-i+1
            return ans
        return dfs(k) - dfs(k-1)

        