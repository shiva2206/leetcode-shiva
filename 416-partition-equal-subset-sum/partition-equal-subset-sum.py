class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 :return False
        s = s//2
        d =set()
        def dfs(i,s):
            if i==len(nums):return s==0
            if  (i,s) in d:return False
            d.add((i,s))
            return dfs(i+1,s - nums[i]) or dfs(i+1,s)
        return dfs(0,s)    