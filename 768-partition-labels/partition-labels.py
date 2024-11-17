class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,j  in enumerate(s):
            d[j] = i
        
        size = 0
        res = []
        end = 0
        for i,j in enumerate(s):
            
            size+=1
            end = max(end,d[j])
            if end == i:
                res.append(size)
                size = 0
        return res
            