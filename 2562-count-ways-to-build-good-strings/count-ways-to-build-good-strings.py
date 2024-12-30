class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        
        d = {}
        def dfs(c):
            if c>high:return 0
            m = 1 if low<=c<=high else 0
            if c in d:return d[c]
            m += (dfs(c+one) + dfs(c+zero))%1000000007
            d[c] = m
            return m
        return dfs(0)