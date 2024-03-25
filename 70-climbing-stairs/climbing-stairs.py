class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def dfs(i):
            if i==n:return 1
            if i>n:return 0
            if i in d:return d[i]
            d[i] = dfs(i+1) + dfs(i+2)
            return d[i]
        return dfs(0)    