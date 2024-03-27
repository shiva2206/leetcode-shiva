class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        d = {}
        def dfs(i,k):
            if i == len(prices):return 0 
            if (i,k) in d:return d[(i,k)]

            m = dfs(i+1,k)
            if k==0:
                m = max(m, dfs(i+1,1) - prices[i])
            else:
                m = max(m,dfs(i+1,0) + prices[i] - fee)
            d[(i,k)] = m
            return m
        return dfs(0,0)