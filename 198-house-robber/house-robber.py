class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
        def dfs(i):
            if i>=len(nums):return 0
            if i in d:return d[i]
            d[i] = max(nums[i] + dfs(i+2),dfs(i+1))
            return d[i]
        return dfs(0)    