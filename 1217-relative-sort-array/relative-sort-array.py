class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = []
        d = Counter(arr1)

        for i in arr2:
            l.extend([i]*d[i])
            d.pop(i)
        
        for i in sorted(d.keys()):
            l.extend([i]*d[i])
        return l
