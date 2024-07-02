class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            if i not in d:
                d[i]=0
            d[i]+=1
        g = {}
        for i in nums2:
            if i not in g:
                g[i]=0
            g[i]+=1
        res = []
        for i in d:
            if i in g:
                res.extend([i]*min(d[i],g[i]))
        return res