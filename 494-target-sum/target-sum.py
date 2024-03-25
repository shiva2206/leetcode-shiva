class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d={}
        def dfs(i,j):
            if i == len(nums): return 1 if j==target else 0
            if (i,j) in d:return d[(i,j)]

            d[(i,j)] = dfs(i+1,j - nums[i]) + dfs(i+1,j+nums[i])
            return d[(i,j)]
        return dfs(0,0)   