class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        
        res =[]
        for i in range(len(row)):
            res.append([])
            for j in range(len(col)):
                m = min(row[i],col[j])
                res[-1].append(m)
                row[i]-=m
                col[j]-=m
        return res