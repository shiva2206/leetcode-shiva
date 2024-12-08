class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        i = 0
        j = len(nums)-1

        while i<=j:
            m = (j+i)//2

            left = nums[m-1] if m-1>=0 else -float('inf')
            right = nums[m+1] if m+1<len(nums) else -float('inf')
            if left<nums[m]<right:
                i = m+1
            elif left>nums[m]>right:
                j = m-1
            elif left>nums[m]<right:
                j = m-1
            else:
                return m

        return -1
