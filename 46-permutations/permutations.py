class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if i ==len(nums):
                res.append(nums.copy())
                return 
            
            for x in range(i,len(nums)):
                nums[i],nums[x] = nums[x],nums[i]
                dfs(i+1)
                nums[i],nums[x] = nums[x],nums[i]
        dfs(0)
        return res