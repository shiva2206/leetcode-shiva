class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # d = {}
        # def dfs(i,j):
        #     if j == amount:
        #         return 1
        #     if j>amount or i==len(coins):
        #         return 0
        #     if (i,j) in d:
        #         return d[(i,j)]
            
        #     d[(i,j)] = dfs(i,j + coins[i]) + dfs(i+1,j)
        #     return d[(i,j)]
        # return dfs(0,0)
        if amount ==0:return 1
        d = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]   
        for i in range(len(coins)-1,-1,-1):
            for j in range(amount-1,-1,-1):
                if j+coins[i]>amount:
                    x = 0
                elif j+coins[i]==amount:
                    x=1
                else:
                    x = d[i][j+coins[i]]
                d[i][j] = x + d[i+1][j]
        return d[0][0]