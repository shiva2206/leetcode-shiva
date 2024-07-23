class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        l = [(i,d[i]) for i in d.keys()]
        l.sort(key = lambda x: (x[1],-x[0]))

        res = []
        for i,j in l:
            res.extend([i]*j)
        return res