class Solution:
    def tribonacci(self, n: int) -> int:
        d={}
        def dfs(i):
            if i<=0:return 0
            if i in [1,2]:return 1
            if i in d:return d[i]
            d[i] = dfs(i-2) + dfs(i-1) + dfs(i-3)
            return d[i]
        return dfs(n)