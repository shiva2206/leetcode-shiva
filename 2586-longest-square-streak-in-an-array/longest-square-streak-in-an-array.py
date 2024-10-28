class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
     
       
        d = {}
        for i in nums:
            d[i] = 1
        ans = -1
        for i in sorted(d.keys()):
            
            m = i**2
            if m in d:
                d[m]+=d[i]
                
                ans = max(ans,d[m])
        print(d)
        return ans