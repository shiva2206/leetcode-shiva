class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        d = {}
        for i in arr:
            if i not in d:
                d[i] =0
            d[i]+=1
        print(d.keys())
        l = list(d.keys())

        l.sort(key = lambda x: d[x])

        for i in range(len(l)):
            if d[l[i]]>k:
                return len(l)-i
            else:
                k-=d[l[i]]
        return 0               
