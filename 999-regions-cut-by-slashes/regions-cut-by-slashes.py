class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        l = []
        for i in range(len(grid)):
            a = ""
            b = ""
            c = ""
            for j in range(len(grid[i])):
                if grid[i][j]==" ":
                    a += "000"
                    b += "000"
                    c +="000"
                elif grid[i][j]=="/":
                    a += "001"
                    b += "010"
                    c += "100"
                else:
                    a += "100"
                    b += "010"
                    c += "001" 
                
            l.append(a)
            l.append(b)
            l.append(c)
        vis = set()
        
        def dfs(i,j):
            if i<0 or i==len(l) or j<0 or len(l[i])==j or l[i][j]!="0" or (i,j) in vis :return 
            vis.add((i,j))
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
            return 
        ans = 0
        for i in range(len(l)):

            for j in range(len(l[i])):
                if l[i][j]=="0" and (i,j) not in vis:
                    dfs(i,j)
                    ans +=1
        return ans
