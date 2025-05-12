class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = []
        def dfs(i,s):
            if i == len(nums):
                l.append(s.copy())
                return 
            for j in range(i,len(nums)):
                s[i],s[j] = s[j],s[i]
                dfs(i+1,s)
                s[i],s[j] = s[j],s[i]
        dfs(0,nums)
        return l