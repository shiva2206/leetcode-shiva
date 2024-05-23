class Solution:
    def numTilings(self, n: int) -> int:
        d={}
        def dfs(a,b):
            if a>n or b>n:return 0
            if a == b == n:return 1

            if (a,b) in d:return d[(a,b)]

            m = 0

            if a==b:
                m = dfs(a+2,b+2) + dfs(a+2,b+1) + dfs(a+1,b+2) +dfs(a+1,b+1)
            elif a-b==1:
                m+= dfs(a,b+2) + dfs(a+1,b+2)
            else:
                m+= dfs(a+2,b) + dfs(a+2,b+1)
            d[(a,b)]=m%1000000007
            return d[(a,b)]
        a=  dfs(0,0)
        # print(d)
        return a
