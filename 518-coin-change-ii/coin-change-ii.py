class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = {}
        def dfs(i,j):
            if j == amount:
                return 1
            if j>amount or i==len(coins):
                return 0
            if (i,j) in d:
                return d[(i,j)]
            
            d[(i,j)] = dfs(i,j + coins[i]) + dfs(i+1,j)
            return d[(i,j)]
        return dfs(0,0)