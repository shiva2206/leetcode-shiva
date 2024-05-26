class Solution:
    def checkRecord(self, n: int) -> int:
        
        d = {}
        def dfs(i,a,l):
            if l==3 or a==2:return 0
            if i == n:
                return 1 
            if (i,a,l) in d:return d[(i,a,l)]
            d[(i,a,l)] = (dfs(i+1,a,0) + dfs(i+1,a+1,0) + dfs(i+1,a,l+1))%1000000007
            return d[(i,a,l)]
        # return dfs(0,0,0)

        c = [[0] * 4 for i in range(3)]
        f = [[0] * 4 for i in range(3)]
        for i in range(2):
            for j in range(3):
                f[i][j] = 1
        
        for i in range(n-1,-1,-1):
            for a in range(1,-1,-1):
                for l in range(2,-1,-1):
                    c[a][l] = (f[a][0] + f[a+1][0] + f[a][l+1])%1000000007
            
            for k in range(3):
                f[k] = c[k] +[]
        return c[0][0]

