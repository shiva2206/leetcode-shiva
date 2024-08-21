class Solution:
    def strangePrinter(self, s: str) -> int:
        d={}
        def dfs(i,j):
            
            if i==j:return 1
            if i>j:return 0
            if (i,j) in d: return d[(i,j)]
        
            d[(i,j)]=float('inf')
            
            for k in range(i,j+1):
                d[(i,j)]=min(d[(i,j)], dfs(i,k) + dfs(k+1,j))
            if s[i]==s[j]:
                d[(i,j)]-=1   
            return d[(i,j)]
        
        dfs(0,len(s)-1)            
        print(d)
        return dfs(0,len(s)-1)
            