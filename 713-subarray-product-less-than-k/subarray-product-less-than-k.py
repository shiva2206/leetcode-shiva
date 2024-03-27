class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k in [0,1]:return 0
        s = 1
        i = 0
        ans = 0
        for j in range(len(nums)):
            s = s*nums[j]
            while s>=k and i<len(nums):
                s = s//nums[i]
                i+=1
            if i<=j:
                ans += (j-i+1)
        return ans