class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        d = {}
        def dfs(i):
            if i ==len(nums):return 0
            if i in d:
                return d[i]
            d[i] = 1
            for k in range(i+1,len(nums)):
                if nums[i]<nums[k]:
                    d[i] = max(1+dfs(k),d[i])
            return d[i]
        res = 0
        for i in range(len(nums)):
            res = max(dfs(i),res)
        return res