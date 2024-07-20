class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        i = len(row)-1
        j = len(col) -1
        res = [[0]*len(col) for i in range(len(row))]
        while i>=0 and j>=0:
            if row[i]>=col[j]:
                res[i][j] = col[j]
                row[i]-=col[j]
                j-=1
            else:
                res[i][j] = row[i]
                col[j]-=row[i]
                i-=1
        return res