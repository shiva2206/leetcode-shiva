class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        d = {}

        def dfs(n):
            if n==1:return True
            if n == 0:return False

            if n in d: return d[n]
            d[n] = False

            j = 1
            while j*j<=n:
                if not dfs(n- j*j):
                    d[n] = True 
                    return True
                j+=1
            return False
        return dfs(n)            

