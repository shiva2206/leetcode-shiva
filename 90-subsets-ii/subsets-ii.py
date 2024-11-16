class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        s = []
        nums.sort()
        def dfs(i):
            if i==len(nums):
                res.append(s.copy())
                return 
            s.append(nums[i])
            dfs(i+1)
            s.pop()

            x = i
            while x+1<len(nums) and nums[x+1]==nums[i]:
                x+=1
            dfs(x+1)
        dfs(0)
        return res

    