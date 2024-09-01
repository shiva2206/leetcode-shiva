class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n !=len(original) :return []
        l = []
        for i in range(0,len(original),n):
            l.append(original[i:i+n])
        return l