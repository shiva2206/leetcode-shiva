class Solution:
    def numTilings(self, n: int) -> int:
        d={}
        def dfs(a,b):
            if a>n:return 0
            if a == b == n:return 1
            
            if b>a:
                a,b = b,a

            if (a,b) in d:return d[(a,b)]
            # if (b,a) in d:return d[(b,a)]

            m = 0

            if a==b:
                m = dfs(a+2,b+2) + dfs(a+2,b+1) + dfs(a+1,b+2) +dfs(a+1,b+1)
            else:
                m+= dfs(a,b+2) + dfs(a+1,b+2)
         
            d[(a,b)]=m%1000000007
            return d[(a,b)]
        a=  dfs(0,0)
        # print(d)
        return a
