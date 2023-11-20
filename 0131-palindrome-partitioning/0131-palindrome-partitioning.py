class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        l=[]
        def dfs(i):
            if i==len(s):
                res.append(l.copy())
                return 
            q=""
            for j in range(i,len(s)):
                q+=s[j]
                if q==q[::-1]:
                    l.append(q)
                    dfs(j+1)
                    l.pop(-1)
            return 
        dfs(0)    
        return res                 