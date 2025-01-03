class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = [0]
        vow = "aeiouAEIOU"
        for i in range(len(words)):
            m=0
            if words[i][0] in vow and words[i][-1] in vow:
                m = 1
            l.append(m+l[-1])
        res = []
        for i,j in queries:
            res.append(l[j+1]-l[i])
        return res
