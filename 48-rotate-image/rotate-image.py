class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0 
        t = 0
        b = len(mat)-1
        r = len(mat[0])-1

        while l<r:
            for i in range(r-l):
                top = mat[t][l+i]
            
                mat[t][l+i] = mat[b-i][l]
                mat[b-i][l] = mat[b][r-i]
                mat[b][r-i] = mat[t+i][r]
                mat[t+i][r] = top
            l+=1
            r-=1
            t+=1
            b-=1
        return 

