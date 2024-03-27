class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d={}
        def dfs(i,k):
            if i == len(prices) or k==4:return 0
            if (i,k) in d:return d[(i,k)]
            
            if k%2==0:
                d[(i,k)] = max(dfs(i+1,k),dfs(i+1,k+1) - prices[i])
            else:
                d[(i,k)] = max(dfs(i+1,k),prices[i] + dfs(i+1,k+1))

            return d[(i,k)]
        return dfs(0,0)            

