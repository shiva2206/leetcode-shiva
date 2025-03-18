class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        d = 0
        ans = 0
        i=0
        for j in range(len(nums)):

            while d&nums[j]!=0:
                d = d - nums[i]
                i+=1
            d = d| nums[j]            
            ans = max(ans,j-i+1)
            
            
        return ans
