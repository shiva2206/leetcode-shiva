class Solution:
    def rob(self, nums: List[int]) -> int:
       
        a = 0
        b = 0
        for i in range(len(nums)-1,-1,-1):
            c = max(a,nums[i] + b)
            a,b = c,a

        return a
        