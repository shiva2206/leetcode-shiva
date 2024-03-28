class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums +[1]
        d ={}
        def dfs(i,j):
            if i>j:return 0
            if (i,j) in d:return d[(i,j)]
            m = 0
            for k in range(i,j+1):
                m= max(m,nums[i-1]*nums[k]*nums[j+1] + dfs(i,k-1) + dfs(k+1,j))
            d[(i,j)] = m 
            return m
        return dfs(1,len(nums)-2)