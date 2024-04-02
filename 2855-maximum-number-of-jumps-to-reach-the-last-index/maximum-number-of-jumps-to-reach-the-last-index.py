class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        d = {}
        
        def dfs(i):
            if i >= len(nums)-1:return 0
            if i in d:return d[i]
            d[i] = -inf

            for j in range(i+1,len(nums)):
                m = abs(nums[j] - nums[i])
                # print(m,target, abs(nums[j] - nums[i]) <=target)
                if abs(nums[j] - nums[i]) <=target:
                   
                    d[i] = max(d[i],1+dfs(j))
            return d[i]
        a = dfs(0) 
        # print(d)
        return a if a!=-inf else -1