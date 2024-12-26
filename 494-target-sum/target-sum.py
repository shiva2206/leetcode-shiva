class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = {}
        def dfs(i,s):
            if i==len(nums):return 1 if s == target else 0   
            if (i,s) in d:return d[(i,s)]
            d[(i,s)] = dfs(i+1,s - nums[i]) + dfs(i+1,s+nums[i])
            return d[(i,s)]
        return dfs(0,0)
            