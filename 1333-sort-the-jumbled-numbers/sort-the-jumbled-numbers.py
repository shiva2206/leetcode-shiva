class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}

        for i in nums:
            s = 0
            for j in str(i):
                s = s*10
                s += mapping[int(j)]
            if s not in d:
                d[s] =[]
            d[s].append(i)
        res = []
        for i in sorted(d.keys()):
            res.extend(d[i])
        return res