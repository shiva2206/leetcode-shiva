class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = 0 
        tot = 0

        for i in range(len(nums)-1):
            tot+= nums[i]
            if tot>=s - tot:
                ans+=1
        return ans
            