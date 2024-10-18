class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s = s|i
        s= [s]
        ans = [0]

        def dfs(i,p):
            if i == len(nums):
                if p == s[0]:
                    ans[0]+=1
                return 
            dfs(i+1,p)
            dfs(i+1,p|nums[i])
        dfs(0,0)
        return ans[0]
