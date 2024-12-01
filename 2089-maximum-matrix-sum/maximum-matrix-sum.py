class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = float('inf')
        c = True
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]<0:
                    c = not c
                ans += abs(matrix[i][j])
                m = min(m,abs(matrix[i][j]))
        
        return ans if c else ans - 2*m