class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = set()
        for i in edges:
            if i[0] in d:return i[0]
            if i[1] in d:return i[1]
            d.add(i[0])
            d.add(i[1])
        return 