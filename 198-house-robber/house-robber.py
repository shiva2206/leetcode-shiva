class Solution:
    def rob(self, nums: List[int]) -> int:
       
        l = [0]*(len(nums)+2)
        for i in range(len(nums)-1,-1,-1):
            l[i] = max(nums[i] + l[i+2],l[i+1])
        return l[0]
        