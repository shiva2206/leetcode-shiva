class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d={}
        def dfs(i,j):
            if j<0:return float('inf')
            if i == len(coins):return 0 if j==0 else float('inf')
            if (i,j) in d: return d[(i,j)]
            d[(i,j)] = min(1 + dfs(i,j-coins[i]) , dfs(i+1,j))
            return d[(i,j)]
        return dfs(0,amount) if dfs(0,amount)!=float('inf') else -1   
