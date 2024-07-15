class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        
        d={}
        def dfs(i,j):
            if i == len(mat):return 0
            if j==-1 or j == len(mat[i]):return float('inf')
            if (i,j) in d:return d[(i,j)]
            d[(i,j)] = mat[i][j] + min(dfs(i+1,j-1),dfs(i+1,j),dfs(i+1,j+1))
            return d[(i,j)]
        m = float('inf')
        for i in range(len(mat[0])):
            m = min(m,dfs(0,i))
        return m