class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:return nums[0]
        d = {}
        
        def dfs(i):
            if i>=len(nums):return 0
            if i in d:return d[i]
            d[i] = max(nums[i] + dfs(i+2),dfs(i+1))
            return d[i]
        p = nums.pop()
        ans = dfs(0)
        d={}
        nums.append(p)
        ans = max(ans,dfs(1))
        return ans