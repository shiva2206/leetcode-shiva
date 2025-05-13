class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        s = []

        def dfs(i):
            if i == len(nums):
                l.append(s.copy())
                return 
            s.append(nums[i])
            dfs(i+1)
            s.pop()
            x = i+1
            while x<len(nums) and nums[i] == nums[x]:
                x+=1
            dfs(x)
        dfs(0)
        return l