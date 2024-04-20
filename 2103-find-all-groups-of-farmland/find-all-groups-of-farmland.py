class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        

        res =[]
        def dfs(i,j,n):
            if i<0 or j<0 or i==len(land) or j==len(land[i]) or land[i][j]!=1:return 
            land[i][j]=n;

            dfs(i+1,j,n)
            dfs(i-1,j,n)
            dfs(i,j+1,n)
            dfs(i,j-1,n)
        n=2
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j]==1:
                    dfs(i,j,n)
                    res.append([i,j,i,j])
                    n+=1             
                elif land[i][j]!=0:
                    q = land[i][j]-2
                    res[q][2] = i
                    res[q][3] = j
        return res

