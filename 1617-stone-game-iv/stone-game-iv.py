class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def dfs(i,k):
            if i ==1:return k==0
            j = 1
            while j*j<=i:
                if j*j==i:return k==0
                if k==0:
                    if dfs(i-j*j,1): return True
                else:
                    if not dfs(i-j*j,0): return False
                j+=1    
            return k==1
        w = dfs(n,0)
        # print(d)
        return w                

