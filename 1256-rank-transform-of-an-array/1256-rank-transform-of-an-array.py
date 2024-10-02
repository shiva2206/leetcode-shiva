class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        l = arr+[]
        l.sort()
        m = 1
        for i in l:

            if i not in d:
                d[i]=m
                m+=1
        for i,j in enumerate(arr):
            arr[i] = d[j]
        return arr 
