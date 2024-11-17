class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,j  in enumerate(s):
            d[j] = i
        
        ans = 0
        res = []
        
        
        end = 0
        for i,j in enumerate(s):
            
            ans+=1
            end = max(end,d[j])
            if end == i:
                res.append(ans)
                ans = 0
        return res
            