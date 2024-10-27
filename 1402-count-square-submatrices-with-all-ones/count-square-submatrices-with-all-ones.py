class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        s = 0
        for i in range(len(matrix)):
            s+= matrix[i][0]
        
        for j in range(1,len(matrix[0])):
            s+=matrix[0][j]
    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) +1
                    s += matrix[i][j]
        print(matrix)
        return s
