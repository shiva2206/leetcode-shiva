class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [(names[i],heights[i]) for i in range(len(names))]
        l.sort(key=lambda x : -x[1] )

        for i in range(len(l)):
            names[i] = l[i][0]
        return names