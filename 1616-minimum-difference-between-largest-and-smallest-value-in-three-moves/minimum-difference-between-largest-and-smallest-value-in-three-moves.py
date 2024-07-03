class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=4: return 0
        a = nums[-1] - nums[3]
        a = min(a,nums[-2]-nums[2])
        a = min(a,nums[-3]-nums[1]) 
        a= min (a,nums[-4]-nums[0])

        return a