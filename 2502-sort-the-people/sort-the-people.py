class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [(i,heights[i]) for i in range(len(names))]
        l.sort(key=lambda x : -x[1] )

        for i in range(len(l)):
            heights[i] = names[l[i][0]]
        return heights